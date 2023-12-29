"""Mail senders"""

import os
import json
import requests
import ssl
import qrcode
import logging
from dotenv import load_dotenv
from html_templates.black_transactional import template_roon, template_test
from html_templates.saiaconf import template_saiaconf_1
from tools.notion_retriever import (
    get_send_standard_invite_contacts,
    mark_contact_as_standard_invite_sent,
    get_contacts_by_tag,
    patch_contact_as,
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
            receiver_name = contact["properties"]["First name"]["rich_text"][0][
                "plain_text"
            ]
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
    logger.info(f"Trying to send templated email to everyone at {from_label_text}")

    try:
        contacts = await get_contacts_by_tag(tag=from_label_text)
        for contact in contacts["results"]:
            try:
                receiver_email = contact["properties"]["Email"]["email"]
                receiver_name = contact["properties"]["Name"]["rich_text"][0][
                    "plain_text"
                ]
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
                    receiver_name=receiver_name, gcs=gcs
                )
                hydrated_body = body_template.substitute(
                    receiver_name=receiver_name, gcs=gcs
                )

                # # Create a Mail object
                mail = Mail(
                    from_email=Email("saiaconf@saia.ar"),
                    to_emails=To(receiver_email),
                    subject=hydrated_subject,
                    html_content=Content("text/html", hydrated_body),
                )

                # # Send the email
                try:
                    logger.info(f"Sending email to {receiver_name} {receiver_pronouns}")
                    email_job = sg.client.mail.send.post(request_body=mail.get())
                    logger.info(f"Sendgrid response : {email_job.status_code}")
                    if email_job.status_code == 202:
                        # Change funnel position in Notion if the email was sent
                        patch = await patch_contact_as(
                            new_tag=success_label_text, id=contact["id"]
                        )
                        logger.info(
                            f"Email sent to {receiver_email}, patch response: {patch}"
                        )
                except Exception as e:
                    logger.error(e)
            except IndexError as e:
                logger.error(f"Index Error: {e}")

    except KeyError as error:
        logger.error(error)
        return {
            "status": "Error getting contacts",
        }


async def make_qr_ticket(id: str):
    """Make QR ticket"""
    logger.info(f"Trying to make QR ticket for {id}")
    try:
        # Create QR code instance
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        # Add data
        qr.add_data(f"https://mailer.saia.ar/saiaconfattendance?id={id}")
        qr.make(fit=True)
        # Create an image from the QR Code instance
        img = qr.make_image(fill_color="black", back_color="white")
        # Save it somewhere, change the extension as needed:
        img.save(f"../data/qr/{id}.png")
        logger.info(f"QR ticket created for {id}")
        return f"https://assets.saia.ar/saia/conf/qrtickets/{id}.png"
    except Exception as e:
        logger.error(e)
        return "https://assets.saia.ar/saia/conf/qrtickets/qr.png"


async def send_cms_templated_emails(
    template_name: str, subject: str, saiaconf_stream: bool
):
    """Send templated email"""
    logger.info(
        f"Trying to send templated email to everyone at stream = {saiaconf_stream}"
    )
    url = "https://cms.saia.ar/items/leads/"
    true_params = {
        "meta": "filter_count",
        "filter": '{"saiaconf_stream": {"_eq": true}}',
    }
    false_params = {
        "meta": "filter_count",
        "filter": '{"saiaconf_stream": {"_eq": false}}',
    }

    # filter = 'meta=filter_count&filter={"saiaconf_stream": { "_eq": false }}'
    # if saiaconf_stream:
    #     filter = 'https://cms.saia.ar/items/leads?meta=filter_count&filter={ "saiaconf_stream": { "_eq": true }}'

    try:
        total_count = requests.get(
            url=url, params=true_params if saiaconf_stream else false_params, timeout=15
        ).json()["meta"]["filter_count"]
        total_pages = total_count // 25 + 1
        logger.info(f"Total pages: {total_pages}")
        #################
        # TODO borrar esto en prod
        # total_pages = 1
        #################
        for page in range(1, total_pages + 1):
            logger.info(
                f"\n\n\n*************** Page: {page} of {total_pages} *****************\n\n\n"
            )
            true_params = {
                "page": page,
                "filter": '{"saiaconf_stream": {"_eq": true}}',
            }
            false_params = {
                "page": page,
                "filter": '{"saiaconf_stream": {"_eq": false}}',
            }
            contacts = requests.get(
                url=url,
                params=true_params if saiaconf_stream else false_params,
            ).json()
            for contact in contacts["data"]:
                logger.info(f"Contact: {contact}")
                contact_id = contact["id"]
                # qr_image = await make_qr_ticket(contact_id)
                receiver_email = contact["email"]
                receiver_name = contact["first_name"]
                subject_template = Template(subject)
                # load template from local storage
                template_path = f"../data/templates/{template_name}.html"
                # load file contents into a string
                with open(template_path, "r") as template_file:
                    body_template = template_file.read()
                body_template = Template(body_template)
                hydrated_subject = subject_template.substitute(
                    receiver_name=receiver_name
                )
                hydrated_body = body_template.substitute(
                    receiver_name=receiver_name,
                    qr_url=f"https://assets.saia.ar/saia/conf/qrtickets/{contact_id}.png",
                )

                # TODO: remove this
                # receiver_email = "pross888@gmail.com"
                # # Create a Mail object
                mail = Mail(
                    from_email=Email("saiaconf@saia.ar"),
                    to_emails=To(receiver_email),
                    subject=hydrated_subject,
                    html_content=Content("text/html", hydrated_body),
                )

                # # Send the email
                try:
                    logger.info(f"Sending email to {receiver_name} {contact_id}")
                    email_job = sg.client.mail.send.post(request_body=mail.get())
                    logger.info(f"Sendgrid response : {email_job.status_code}")
                    if email_job.status_code == 202:
                        # Change funnel position in Notion if the email was sent
                        logger.info(f"Email sent to {receiver_email}")
                        event = requests.post(
                            "https://cms.saia.ar/items/events/",
                            json={
                                "channel": "email",
                                "lead": contact_id,
                                "message": "qr ticket",
                            },
                        )
                        logger.info(
                            f"Contact ID: {contact_id} > event: {event.status_code}"
                        )
                except Exception as e:
                    logger.error(e)

    except Exception as e:
        logger.error(e)


# fmt: off
async def create_qr_tickets():
    """Send templated email"""
    logger.info(
        f"Trying to create QR tickets for those who come to the event and did not receive an email"
    )
    url = "https://cms.saia.ar/items/leads/"
    params = {
        "meta": "filter_count",
        "filter": '{"_and": [{"events": {"_none": {"message": {"_eq": "qr ticket"}}}},{"saiaconf_stream": {"_eq": false}}]}'
    }

    # filter = 'meta=filter_count&filter={"saiaconf_stream": { "_eq": false }}'
    # if saiaconf_stream:
    #     filter = 'https://cms.saia.ar/items/leads?meta=filter_count&filter={ "saiaconf_stream": { "_eq": true }}'

    try:
        res = requests.get(url=url, params=params, timeout=15).json()
        # logger.info(f"Response: {res}")
        total_count = res["meta"]["filter_count"]
        total_pages = total_count // 25 + 1
        logger.info(f"Total pages: {total_pages}")
        #################
        # TODO borrar esto en prod
        # total_pages = 1
        #################
        for page in range(1, total_pages + 1):
            logger.info(
                f"\n\n\n*************** Page: {page} of {total_pages} *****************\n\n\n"
            )

            params = {
                "page": page,
                "filter": '{"_and": [{"events": {"_none": {"message": {"_eq": "qr ticket"}}}},{"saiaconf_stream": {"_eq": false}}]}'
            }
            contacts = requests.get(
                url=url,
                params=params,
            ).json()
            for contact in contacts["data"]:
                logger.info(f"Contact: {contact}")
                contact_id = contact["id"]
                qr_image = await make_qr_ticket(contact_id)
                receiver_email = contact["email"]
                receiver_name = contact["first_name"]
                try:
                    event = requests.post(
                        "https://cms.saia.ar/items/events/",
                        json={
                            "channel": "email",
                            "lead": contact_id,
                            "message": "qr created",
                        },
                    )

                except Exception as e:
                    logger.error(e)

    except Exception as e:
        logger.error(e)


async def send_remaining_qr_invites(
    template_name: str, subject: str, event_message: str, test_mode: bool
):
    """Send remaining QR invites"""
    logger.info(
        f"Trying to remaining QR invites"
    )
    url = "https://cms.saia.ar/items/leads/"
    meta_params = {
        "meta": "filter_count",
        "filter": '{"_and": [{"events": {"_none": {"message": {"_eq": "qr ticket"}}}},{"events": {"_none": {"message": {"_eq": "qr ticket sent by email"}}}},{"saiaconf_stream": {"_eq": false}}]}'
    }


    # filter = 'meta=filter_count&filter={"saiaconf_stream": { "_eq": false }}'
    # if saiaconf_stream:
    #     filter = 'https://cms.saia.ar/items/leads?meta=filter_count&filter={ "saiaconf_stream": { "_eq": true }}'

    try:
        total_count = requests.get(
            url=url, params=meta_params, timeout=15
        ).json()["meta"]["filter_count"]
        total_pages = total_count // 25 + 1
        logger.info(f"Total pages: {total_pages}")
        if test_mode:
            total_pages = 1

        for page in range(1, total_pages + 1):
            logger.info(
                f"\n\n\n*************** Page: {page} of {total_pages} *****************\n\n\n"
            )
            page_params = {
                "page": page,
                "filter": '{"_and": [{"events": {"_none": {"message": {"_eq": "qr ticket"}}}},{"events": {"_none": {"message": {"_eq": "qr ticket sent by email"}}}},{"saiaconf_stream": {"_eq": false}}]}'
            }
      
            contacts = requests.get(
                url=url,
                params=page_params,
            ).json()
            for contact in contacts["data"]:
                logger.info(f"Contact: {contact}")
                contact_id = contact["id"]
                receiver_email = contact["email"]
                receiver_name = contact["first_name"]
                subject_template = Template(subject)
                # load template from local storage
                template_path = f"../data/templates/{template_name}.html"
                # load file contents into a string
                with open(template_path, "r") as template_file:
                    body_template = template_file.read()
                body_template = Template(body_template)
                hydrated_subject = subject_template.substitute(
                    receiver_name=receiver_name
                )
                hydrated_body = body_template.substitute(
                    receiver_name=receiver_name,
                    qr_url=f"https://assets.saia.ar/saia/conf/qrtickets/{contact_id}.png",
                )

                # TODO: remove this if not testing
                if test_mode: 
                    receiver_email = "pross888@gmail.com"

                # # Create a Mail object
                mail = Mail(
                    from_email=Email("🎙️ SAIAConf<saiaconf@saia.ar>"),
                    to_emails=To(receiver_email),
                    subject=hydrated_subject,
                    html_content=Content("text/html", hydrated_body),
                )

                # # Send the email
                try:
                    logger.info(f"Sending email to {receiver_name} {contact_id}")
                    email_job = sg.client.mail.send.post(request_body=mail.get())
                    logger.info(f"Sendgrid response : {email_job.status_code}")
                    if email_job.status_code == 202:
                        # Change funnel position in Notion if the email was sent
                        logger.info(f"Email sent to {receiver_email}")
                        event = requests.post(
                            "https://cms.saia.ar/items/events/",
                            json={
                                "channel": "email",
                                "lead": contact_id,
                                "message": event_message,
                            },
                        )
                        logger.info(
                            f"Contact ID: {contact_id} > event: {event.status_code}"
                        )
                except Exception as e:
                    logger.error(e)

    except Exception as e:
        logger.error(e)




async def send_remaining_stream_invites(
    template_name: str, subject: str, event_message: str, test_mode: bool
):
    """Send remaining stream invites"""
    logger.info(
        f"Trying to send remaining stream invites"
    )
    url = "https://cms.saia.ar/items/leads/"
    meta_params = {
        "meta": "filter_count",
        "filter": '{"_and": [{"events": {"_none": {"message": {"_eq": "stream link sent by email"}}}},{"events": {"_none": {"message": {"_eq": "qr ticket sent by email"}}}},{"saiaconf_stream": {"_eq": true}}]}'
    }


    # filter = 'meta=filter_count&filter={"saiaconf_stream": { "_eq": false }}'
    # if saiaconf_stream:
    #     filter = 'https://cms.saia.ar/items/leads?meta=filter_count&filter={ "saiaconf_stream": { "_eq": true }}'

    try:
        total_count_request = requests.get(
            url=url, params=meta_params, timeout=15
        ).json()
        logger.info(f"Response: {total_count_request}")
        total_count = total_count_request["meta"]["filter_count"]
        total_pages = total_count // 25 + 1
        logger.info(f"Total pages: {total_pages}")
        if test_mode:
            total_pages = 1

        for page in range(1, total_pages + 1):
            logger.info(
                f"\n\n\n*************** Page: {page} of {total_pages} *****************\n\n\n"
            )
            page_params = {
                "page": page,
                "filter": '{"_and": [{"events": {"_none": {"message": {"_eq": "stream link sent by email"}}}},{"events": {"_none": {"message": {"_eq": "qr ticket sent by email"}}}},{"saiaconf_stream": {"_eq": true}}]}'
            }
      
            contacts = requests.get(
                url=url,
                params=page_params,
            ).json()
            for contact in contacts["data"]:
                logger.info(f"Contact: {contact}")
                contact_id = contact["id"]
                receiver_email = contact["email"]
                receiver_name = contact["first_name"]
                subject_template = Template(subject)
                # load template from local storage
                template_path = f"../data/templates/{template_name}.html"
                # load file contents into a string
                with open(template_path, "r") as template_file:
                    body_template = template_file.read()
                body_template = Template(body_template)
                hydrated_subject = subject_template.substitute(
                    receiver_name=receiver_name
                )
                hydrated_body = body_template.substitute(
                    receiver_name=receiver_name,
                )

                if test_mode: 
                    receiver_email = "pross888@gmail.com"

                # # Create a Mail object
                mail = Mail(
                    from_email=Email("🎙️ SAIAConf<saiaconf@saia.ar>"),
                    to_emails=To(receiver_email),
                    subject=hydrated_subject,
                    html_content=Content("text/html", hydrated_body),
                )

                # # Send the email
                try:
                    logger.info(f"Sending email to {receiver_name} {contact_id}")
                    email_job = sg.client.mail.send.post(request_body=mail.get())
                    logger.info(f"Sendgrid response : {email_job.status_code}")
                    if email_job.status_code == 202:
                        # Change funnel position in Notion if the email was sent
                        logger.info(f"Email sent to {receiver_email}")
                        event = requests.post(
                            "https://cms.saia.ar/items/events/",
                            json={
                                "channel": "email",
                                "lead": contact_id,
                                "message": event_message,
                            },
                        )
                        logger.info(
                            f"Contact ID: {contact_id} > event: {event.status_code}"
                        )
                except Exception as e:
                    logger.error(e)

    except Exception as e:
        logger.error(e)
