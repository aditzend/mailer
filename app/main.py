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
    send_emails_with_path_template,
)
from tools.notion_retriever import get_funnel_data

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


# Define a Pydantic model for the request body
class EmailData(BaseModel):
    template_path: str
    subject: str
    from_label_text: str
    success_label_text: str


@app.post("/v1/send_emails_with_path_template")
async def send_emails_with_path_template_wrapper(email_data: EmailData):
    """
    Send emails with path template
    """
    result = await send_emails_with_path_template(
        template_path=email_data.template_path,
        subject=email_data.subject,
        from_label_text=email_data.from_label_text,
        success_label_text=email_data.success_label_text,
    )
    return result
