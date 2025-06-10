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
    amount = 3.54
    friendship_amount = 1
    now = datetime.now()
    date = str(now.month) + "/" + str(now.year)
    spotify_family = ["JERRY", "PRACHI", "SAHIL", "ROHAN", "SREYA"]
    friendship_family = ["JAKE", "SARAH"]
    friendship_description = "friendship dues for {date}".format(date = date)
    description = "spotify {date}".format(date = date)
    


    for member in spotify_family:
        user = venmo_client.user.get_user_by_username(os.environ.get(member))
        try:
            time.sleep(random.uniform(5, 10))  # jittered delay
            venmo_client.payment.request_money(amount = amount, note = description, target_user_id = user.id, privacy_setting=PaymentPrivacy.PRIVATE)
            print("Success: {member}".format(member = member))
        except Exception as e:
                print(e)

    for member in friendship_family:
        user = venmo_client.user.get_user_by_username(os.environ.get(member))
        try:
            time.sleep(random.uniform(5, 10))  # jittered delay
            venmo_client.payment.request_money(amount = friendship_amount, note = friendship_description, target_user_id = user.id, privacy_setting=PaymentPrivacy.PRIVATE)
            print("Success: {member}".format(member = member))
        except Exception as e:
                print(e)
    
    # icloud payment
    icloud_description = "icloud dues for {date}".format(date = date)
    user = venmo_client.user.get_user_by_username(os.environ.get("JAKE"))
    try:
        time.sleep(random.uniform(5, 10))  # jittered delay
        venmo_client.payment.pay_money(amount = 1.99, note = icloud_description, target_user_id = user.id, privacy_setting=PaymentPrivacy.PRIVATE)
        print("Success: {member}".format(member = member))
    except Exception as e:
            print(e)

main()
