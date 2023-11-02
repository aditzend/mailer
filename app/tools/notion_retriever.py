import requests
import json
import os
import logging


logger = logging.getLogger("uvicorn")

NOTION_API_KEY = os.getenv("NOTION_API_KEY")
NOTION_ONBOARDING_FUNNEL_ID = os.getenv("NOTION_ONBOARDING_FUNNEL_ID")
NOTION_ONBOARDING_SUBMISSIONS_ID = os.getenv(
    "NOTION_ONBOARDING_SUBMISSIONS_ID"
)


def get_funnel_data():
    """Reads all funnel activities"""
    logger.info("Getting funnel data from Notion")
    res = requests.post(
        url="https://api.notion.com/v1/databases/"
        + NOTION_ONBOARDING_FUNNEL_ID
        + "/query",
        headers={
            "Authorization": "Bearer " + NOTION_API_KEY,
            "Content-Type": "application/json",
            "Notion-Version": "2022-06-28",
        },
        data=json.dumps({}),
        timeout=15,
    )
    logger.info(f"Funnel data from Notion : {res}")
    if res.ok:
        return {"status": "OK", "data": res.json()}
    else:
        return {
            "status": "Error getting funnel data",
        }


async def get_send_standard_invite_contacts():
    """Gets all contacts from Notion that are labeled as 'Send standard invite'"""
    logger.info("Getting contacts from Notion")
    NOTION_API_KEY = os.getenv("NOTION_API_KEY")
    NOTION_ONBOARDING_SUBMISSIONS_ID = os.getenv(
        "NOTION_ONBOARDING_SUBMISSIONS_ID"
    )
    try:
        res = requests.post(
            url=f"https://api.notion.com/v1/databases/{NOTION_ONBOARDING_SUBMISSIONS_ID}/query",
            headers={
                "Authorization": "Bearer " + NOTION_API_KEY,
                "Content-Type": "application/json",
                "Notion-Version": "2022-06-28",
            },
            data=json.dumps(
                {
                    "filter": {
                        "property": "Funnel position",
                        "select": {
                            "equals": "Send standard invite",
                        },
                    }
                }
            ),
            timeout=15,
        )
        logger.info(f"Contacts from Notion : {res}")
        return res.json()
    except requests.exceptions.RequestException as error:
        logger.error(error)
        return {"status": "Error getting contacts"}


async def mark_contact_as_standard_invite_sent(id: str):
    """Patch a contact as 'Standard invite sent'"""
    logger.info("Patching contact as 'Standard invite sent'")
    NOTION_API_KEY = os.getenv("NOTION_API_KEY")
    NOTION_ONBOARDING_SUBMISSIONS_ID = os.getenv(
        "NOTION_ONBOARDING_SUBMISSIONS_ID"
    )
    try:
        res = requests.patch(
            url="https://api.notion.com/v1/pages/" + id,
            headers={
                "Authorization": "Bearer " + NOTION_API_KEY,
                "Content-Type": "application/json",
                "Notion-Version": "2022-06-28",
            },
            data=json.dumps(
                {
                    "properties": {
                        "Funnel position": {
                            "select": {
                                "name": "Standard invite sent",
                            },
                        }
                    }
                }
            ),
            timeout=15,
        )
        logger.info(f"Contacts from Notion : {res}")
        return res.json()
    except requests.exceptions.RequestException as error:
        logger.error(error)
        return {"status": "Error patching contact"}
