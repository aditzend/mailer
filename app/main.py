"""Main functions"""
import os
import logging

# import sentry_sdk
from fastapi import FastAPI
from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel, Field
from dotenv import load_dotenv

load_dotenv()
logger = logging.getLogger("uvicorn")


# SENTRY
# SENTRY_DSN = os.getenv("SENTRY_DSN")
# SENTRY_TRACES_SAMPLE_RATE = float(str(os.getenv("SENTRY_TRACES_SAMPLE_RATE")))
# SENTRY_PROFILES_SAMPLE_RATE = float(
#     str(os.getenv("SENTRY_PROFILES_SAMPLE_RATE"))
# )
# sentry_sdk.init(
#     dsn=SENTRY_DSN,
#     # Set traces_sample_rate to 1.0 to capture 100%
#     # of transactions for performance monitoring.
#     # We recommend adjusting this value in production.
#     traces_sample_rate=SENTRY_TRACES_SAMPLE_RATE,
#     # Set profiles_sample_rate to 1.0 to profile 100%
#     # of sampled transactions.
#     # We recommend adjusting this value in production.
#     profiles_sample_rate=SENTRY_PROFILES_SAMPLE_RATE,
# )

app = FastAPI()


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
        "date": "2023-09-05",
        "branch": "main",
        "version": "0.0.1",
        "comments": "pdf endpoint",
    }
    logger.info(f"Version requested : {version}")
    return version
