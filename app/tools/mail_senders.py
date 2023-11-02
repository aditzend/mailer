"""Mail senders"""

import os
import json
import requests
import ssl
import logging
from dotenv import load_dotenv
from html_templates.black_transactional import template_roon, template_test
from tools.notion_retriever import (
    get_send_standard_invite_contacts,
    mark_contact_as_standard_invite_sent,
)

logger = logging.getLogger("uvicorn")
load_dotenv()

SMTP_HOST = os.getenv("SMTP_HOST")
SMTP_PORT = os.getenv("SMTP_PORT")
SMTP_USER = os.getenv("SMTP_USER")
SMTP_PASSWORD = os.getenv("SMTP_PASSWORD")
SMTP_SENDER = os.getenv("SMTP_SENDER")
MAILGUN_DOMAIN = os.getenv("MAILGUN_DOMAIN")
MAILGUN_API_KEY = os.getenv("MAILGUN_API_KEY")


def send_plain_email(Mail: dict):
    """Sends an email to test everything is working"""
    logger.info(f"Sending plain email to {Mail.receiver}")

    res = requests.post(
        url="https://api.mailgun.net/v3/saia.ar/messages",
        auth=("api", MAILGUN_API_KEY),
        data={
            "from": Mail.sender,
            "to": [Mail.receiver],
            "subject": Mail.subject,
            "text": Mail.body,
        },
        timeout=15,
    )
    logger.info(f"Mailgun response : {res}")
    if res.ok:
        return {
            "status": "OK",
        }
    else:
        return {
            "status": "Error sending email",
        }


def send_html_email(Mail: dict):
    """Send html instead of plain text"""
    logger.info(f"Sending html email to {Mail.receiver}")
    hydrated_template = template_roon.substitute(
        main_header=Mail.body, respondent_id="Td94j33", message="Hola"
    )

    res = requests.post(
        url="https://api.mailgun.net/v3/saia.ar/messages",
        auth=("api", MAILGUN_API_KEY),
        data={
            "from": Mail.sender,
            "to": [Mail.receiver],
            "subject": Mail.subject,
            "html": hydrated_template,
        },
        timeout=15,
    )

    logger.info(f"Mailgun response : {res}")
    if res.ok:
        return {
            "status": "OK",
        }
    else:
        return {
            "status": "Error sending email",
        }


async def send_standard_invites():
    """Send invites to the onboarding funnel"""
    logger.info("Sending invites to the onboarding funnel")
    # hydrated_template = template_roon.substitute(
    #     main_header=Mail.body, respondent_id="Td94j33", message="Hola"
    # )

    try:
        contacts = await get_send_standard_invite_contacts()
        for contact in contacts["results"]:
            receiver_email = contact["properties"]["Email"]["email"]
            receiver_name = contact["properties"]["Name"]["rich_text"][0][
                "plain_text"
            ]
            receiver_last_name = contact["properties"]["Last name"][
                "rich_text"
            ][0]["plain_text"]
            receiver_id = contact["properties"]["ID"]["unique_id"]["number"]
            receiver_id_prefix = contact["properties"]["ID"]["unique_id"][
                "prefix"
            ]
            receiver_pronouns = contact["properties"]["Pronouns"]["select"][
                "name"
            ]
            receiver_code = f"{receiver_id_prefix}-{receiver_id}"

            welcome_treatment = "Bienvenida"
            associate_treatment = "socia"

            if receiver_pronouns == "he/him (el)":
                welcome_treatment = "Bienvenido"
                associate_treatment = "socio"

            if (
                receiver_pronouns != "she/her (ella)"
                and receiver_pronouns != "he/him (el)"
            ):
                welcome_treatment = "Bienvenide"
                associate_treatment = "socie"

            hydrated_template = template_roon.substitute(
                main_header=f"{welcome_treatment} {receiver_name} ",
                message=(
                    " Este es tu código de"
                    f" {associate_treatment}. Va a ser tu forma de"
                    " identificarte dentro de SAIA."
                ),
                code=receiver_code,
            )

            logger.info(
                "Trying to send invite to"
                f" {receiver_name} {receiver_last_name} [{receiver_pronouns}]"
                f" ({receiver_email}) {receiver_id_prefix}-{receiver_id}"
            )

            try:
                # Send email to current contact
                res = requests.post(
                    url=(
                        f"https://api.mailgun.net/v3/{MAILGUN_DOMAIN}/messages"
                    ),
                    auth=("api", MAILGUN_API_KEY),
                    data={
                        "from": SMTP_SENDER,
                        "to": [receiver_email],
                        "subject": (
                            f"{welcome_treatment} a SAIA {receiver_name}"
                        ),
                        "html": hydrated_template,
                    },
                    timeout=15,
                )
                # Change funnel position in Notion if the email was sent
                if res.ok:
                    patch = await mark_contact_as_standard_invite_sent(
                        contact["id"]
                    )
                else:
                    logger.error(f"Mailgun response : {res}")
                    return {
                        "status": "Error sending email",
                    }

            except requests.exceptions.RequestException as error:
                logger.error(error)
                return {
                    "status": "Error sending email",
                }

        return {"status": "finished"}
    except KeyError as error:
        logger.error(error)
        return {
            "status": "Error getting contacts",
        }
