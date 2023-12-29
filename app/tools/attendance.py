""" Attendance functions"""

import logging
import requests
import os
from datetime import datetime, timezone
from dotenv import load_dotenv

logger = logging.getLogger("uvicorn")
load_dotenv()

# Date time format example is 2023-11-25T13:00:00-03:00
SAIACONF_START_TIME = datetime.strptime(
    os.getenv("SAIACONF_START_TIME"), "%Y-%m-%dT%H:%M:%S%z"
)
SAIACONF_END_TIME = datetime.strptime(
    os.getenv("SAIACONF_END_TIME"), "%Y-%m-%dT%H:%M:%S%z"
)


def record_saiaconf_attendance(lead_id: str):
    """
    Record attendance for all students in the database.
    """
    current_utc_time = datetime.now(timezone.utc)
    logger.info(
        f"Current UTC time is {current_utc_time}, checking if it's saiaconf time, between {SAIACONF_START_TIME} and {SAIACONF_END_TIME}"
    )
    if (
        current_utc_time >= SAIACONF_START_TIME
        and current_utc_time <= SAIACONF_END_TIME
    ):
        logger.info(f"Recording attendance for {lead_id}")
        url = "https://cms.saia.ar/items/events"
        payload = {
            "lead": lead_id,
            "channel": "live",
            "message": "qr scanned on saiaconf",
        }
        headers = {"content-type": "application/json"}

        response = requests.request("POST", url, json=payload, headers=headers)
        logger.info(response.text)

        name_req = requests.get(
            f"https://cms.saia.ar/items/leads/{lead_id}", headers=headers
        )
        logger.info(name_req.json())
        first_name = name_req.json()["data"]["first_name"]
        family_name = name_req.json()["data"]["family_name"]

        return f"{first_name} {family_name}  >>> HABILITADO"
    else:
        return "<h1>DESHABILITADO</h1>"
