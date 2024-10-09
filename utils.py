import pytz, random, string  
from datetime import date 
from terabox import API, URL
from shortzy import Shortzy

# utils.py
from shared import check_verification

TOKENS = {}
VERIFIED = {}

async def get_verify_shorted_link(link):
    shortzy = Shortzy(api_key=API, base_site=URL)
    link = await shortzy.convert(link)
    return link

async def check_token(bot, userid, token):
    user = await bot.get_users(userid)
    if user.id in TOKENS.keys():
        TKN = TOKENS[user.id]
        if token in TKN.keys():
            is_used = TKN[token]
            if is_used == True:
                return False
            else:
                return True
    else:
        return False

async def get_token(bot, userid, link):
    user = await bot.get_users(userid)
    token = ''.join(random.choices(string.ascii_letters + string.digits, k=7))
    TOKENS[user.id] = {token: False}
    link = f"{link}verify-{user.id}-{token}"
    shortened_verify_url = await get_verify_shorted_link(link)
    return str(shortened_verify_url)


