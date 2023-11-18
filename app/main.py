"""Main functions"""
import os

import schedule
import asyncio

import aioschedule as schedule
import time
import threading
import logging
import sentry_sdk
from fastapi import FastAPI
from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel, Field
from dotenv import load_dotenv
from tools.mail_senders import (
    send_plain_email,
    send_html_email,
    send_standard_invites,
    send_templated_emails,
)
from tools.notion_retriever import get_funnel_data
from tools.file_cleaners import transform_and_save_xlsx

load_dotenv()
logger = logging.getLogger("uvicorn")


# SENTRY
SENTRY_DSN = os.getenv("SENTRY_DSN")
# SENTRY_TRACES_SAMPLE_RATE = float(str(os.getenv("SENTRY_TRACES_SAMPLE_RATE")))
# SENTRY_PROFILES_SAMPLE_RATE = float(
#     str(os.getenv("SENTRY_PROFILES_SAMPLE_RATE"))
# )
sentry_sdk.init(
    dsn=SENTRY_DSN,
    # Set traces_sample_rate to 1.0 to capture 100%
    # of transactions for performance monitoring.
    # We recommend adjusting this value in production.
    # traces_sample_rate=SENTRY_TRACES_SAMPLE_RATE,
    # Set profiles_sample_rate to 1.0 to profile 100%
    # of sampled transactions.
    # We recommend adjusting this value in production.
    # profiles_sample_rate=SENTRY_PROFILES_SAMPLE_RATE,
)

app = FastAPI()


async def job():
    """Do this"""
    await send_standard_invites()


# Schedule the job to run every day at 10:30 AM


# @app.get("/sentry-debug")
# async def trigger_error():
#     """Simulate an error to test Sentry."""
#     division_by_zero = 1 / 0


@app.get("/version")
async def versioner():
    """
    Gives the branch version and comments
    """
    version = {
        "date": "2023-09-13",
        "branch": "0.0.1",
        "version": "0.0.1",
        "comments": "basic html mail sender",
    }
    logger.info(f"Version requested : {version}")
    return version


class Mail(BaseModel):
    """
    Mail model
    """

    sender: str
    receiver: str
    subject: str
    body: str = Field(..., max_length=10000000000000)


@app.post("/v1/sendmail")
async def sendmail(mail: Mail):
    """
    Send a mail
    """
    result = send_plain_email(mail)
    return result


@app.post("/v1/sendhtmlmail")
async def sendmail(mail: Mail):
    """
    Send a mail
    """
    result = send_html_email(mail)
    return result


@app.post("/v1/getfunneldata")
async def getfunneldata():
    """
    Get funnel data
    """
    result = get_funnel_data()
    return result


@app.post("/v1/send_invites")
async def send_invites():
    """
    Send invites
    """
    result = await send_standard_invites()
    return result


# create a pydantic class named SendTemplatedEmail for the request body
# template_path, subject, from_label_text, success_label_text
class SendTemplatedEmailsBody(BaseModel):
    """
    SendTemplatedEmails model
    """

    template_path: str
    subject: str
    from_label_text: str
    success_label_text: str


@app.post("/v1/send_templated_emails")
async def send_t_emails(send_t_emails_body: SendTemplatedEmailsBody):
    """
    Send templated email
    """
    # extract the file name from the request body
    template_path = send_t_emails_body.template_path
    subject = send_t_emails_body.subject
    from_label_text = send_t_emails_body.from_label_text
    success_label_text = send_t_emails_body.success_label_text
    result = await send_templated_emails(
        template_path, subject, from_label_text, success_label_text
    )
    return result


# create a pydantic class for the request body
class Xlsx(BaseModel):
    """
    Xlsx model
    """

    file_name: str


@app.post("/v1/transform_xlsx")
async def transform_xlsx(xlsx: Xlsx):
    """
    Transform xlsx
    """
    # extract the file name from the request body
    file_name = xlsx.file_name
    result = await transform_and_save_xlsx(file_name="i0")
    return result
