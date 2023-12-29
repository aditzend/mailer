import requests
import json
import os
import logging


logger = logging.getLogger("uvicorn")


def get_leads_paginated():
    """Gets all leads from https://cms.saia.ar/items/leads/?page=i"""
