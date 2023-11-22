"""Mail senders"""

import os
import json
import requests
import ssl
import logging
from dotenv import load_dotenv
from html_templates.black_transactional import template_roon, template_test
from html_templates.saiaconf import template_saiaconf_1
from tools.notion_retriever import (
    get_send_standard_invite_contacts,
    mark_contact_as_standard_invite_sent,
)
from string import Template
import sendgrid
import os
from sendgrid.helpers.mail import Mail, Email, To, Content

logger = logging.getLogger("uvicorn")
load_dotenv()

SENDGRID_API_KEY = os.getenv("SENDGRID_API_KEY")
FROM_EMAIL = os.getenv("FROM_EMAIL")

sg = sendgrid.SendGridAPIClient(api_key=SENDGRID_API_KEY)


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
            receiver_name = contact["properties"]["Name"]["rich_text"][0]["plain_text"]
            receiver_last_name = contact["properties"]["Last name"]["rich_text"][0][
                "plain_text"
            ]
            receiver_id = contact["properties"]["ID"]["unique_id"]["number"]
            receiver_id_prefix = contact["properties"]["ID"]["unique_id"]["prefix"]
            receiver_pronouns = contact["properties"]["Pronouns"]["select"]["name"]
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
                # Send email to current contact using Sendgrid
                message = Mail(
                    from_email=FROM_EMAIL,
                    to_emails=receiver_email,
                    subject=f"{welcome_treatment} a SAIA {receiver_name}",
                    html_content=hydrated_template,
                )
                res = sg.send(message)
                # res = requests.post(
                #     url=(
                #         f"https://api.mailgun.net/v3/{MAILGUN_DOMAIN}/messages"
                #     ),
                #     auth=("api", MAILGUN_API_KEY),
                #     data={
                #         "from": SMTP_SENDER,
                #         "to": [receiver_email],
                #         "subject": (
                #             f"{welcome_treatment} a SAIA {receiver_name}"
                #         ),
                #         "html": hydrated_template,
                #     },
                #     timeout=15,
                # )
                # Change funnel position in Notion if the email was sent
                if res.status_code == 202:
                    patch = await mark_contact_as_standard_invite_sent(contact["id"])
                else:
                    logger.error(f"Sendgrid response : {res.status_code}")
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


async def send_templated_emails(
    template_name: str, subject: str, from_label_text: str, success_label_text: str
):
    """Send templated email"""
    logger.info(f"Trying to send templated email to {subject}")

    try:
        contacts = await get_contacts_by_tag(tag=from_label_text)
        for contact in contacts["results"]:
            receiver_email = contact["properties"]["Email"]["email"]
            receiver_name = contact["properties"]["Name"]["rich_text"][0]["plain_text"]
            receiver_last_name = contact["properties"]["Last name"]["rich_text"][0][
                "plain_text"
            ]
            receiver_id = contact["properties"]["ID"]["unique_id"]["number"]
            receiver_id_prefix = contact["properties"]["ID"]["unique_id"]["prefix"]
            receiver_pronouns = contact["properties"]["Pronouns"]["select"]["name"]
            receiver_code = f"{receiver_id_prefix}-{receiver_id}"

            gcs = "a"

            if receiver_pronouns == "he/him (el)":
                gcs = "o"

            if (
                receiver_pronouns != "she/her (ella)"
                and receiver_pronouns != "he/him (el)"
            ):
                gcs = "e"

            subject_template = Template(subject)
            # load template from local storage
            template_path = f"../data/templates/{template_name}.html"
            # load file contents into a string
            with open(template_path, "r") as template_file:
                body_template = template_file.read()
            body_template = Template(body_template)
            hydrated_subject = subject_template.substitute(
                receiver_name="Alexander", gcs=gcs
            )
            hydrated_body = body_template.substitute(receiver_name="Alexander", gcs="o")

            # # Create a Mail object
            mail = Mail(
                from_email=Email("sysadmin@saia.ar"),
                to_emails=To("alexanderditzend@gmail.com"),
                subject=hydrated_subject,
                html_content=Content("text/html", hydrated_body),
            )

            # # Send the email
            try:
                sg.client.mail.send.post(request_body=mail.get())
            except Exception as e:
                logger.error(e)

    except KeyError as error:
        logger.error(error)
        return {
            "status": "Error getting contacts",
        }
