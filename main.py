# main.py

import os
from venmo_api import Client, PaymentPrivacy
import datetime
from datetime import datetime
import time
import random

TOKEN_KEY = 'VENMO_ACCESS_TOKEN'

def main():
    # load the access token from environ
    access_token = os.environ.get(TOKEN_KEY)
    if access_token is None:
        raise ValueError('[!] EVERYTHING IS BROKEN WE CANT GET ACCESSS AHHHHHH')

    venmo_client = Client(access_token=access_token)
    youtube_amount = 4.07
    now = datetime.now()
    date = str(now.month) + "/" + str(now.year)
    youtube_family = ["PATO"]
    youtube_description = "youtube premium {date}".format(date = date)

    for member in youtube_family:
        print(os.environ.get(member))
        user = venmo_client.user.get_user_by_username(os.environ.get(member))
        try:
            time.sleep(random.uniform(5, 10))  # jittered delay
            venmo_client.payment.request_money(amount = youtube_amount, note = youtube_description, target_user_id = user.id, privacy_setting=PaymentPrivacy.PRIVATE)
            print("Success: {member}".format(member = member))
        except Exception as e:
                print(e)
main()
