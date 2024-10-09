import pytz, random, string  
from datetime import date 
from terabox import API, URL
from shortzy import Shortzy

# utils.py
from shared import check_verification, check_token, get_token

TOKENS = {}
VERIFIED = {}

async def get_verify_shorted_link(link):
    shortzy = Shortzy(api_key=API, base_site=URL)
    link = await shortzy.convert(link)
    return link

