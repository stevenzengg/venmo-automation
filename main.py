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
    youtube_amount = 4.07
    now = datetime.now()
    # Optionally override month/year via env (set by manual workflow_dispatch).
    # Each falls back to today's value for scheduled/cron runs.
    month_override = os.environ.get("PAYMENT_MONTH")
    year_override = os.environ.get("PAYMENT_YEAR")
    month = month_override.strip() if month_override and month_override.strip() else str(now.month)
    year = year_override.strip() if year_override and year_override.strip() else str(now.year)
    date = month + "/" + year
    spotify_family = ["JERRY", "PRACHI", "SAHIL", "ROHAN", "SREYA"]
    youtube_family = ["PATO"]
    description = "spotify {date}".format(date = date)
    youtube_description = "youtube premium {date}".format(date = date)

    


    for member in spotify_family:
        user = venmo_client.user.get_user_by_username(os.environ.get(member))
        try:
            time.sleep(random.uniform(5, 10))  # jittered delay
            venmo_client.payment.request_money(amount = amount, note = description, target_user_id = user.id, privacy_setting=PaymentPrivacy.PRIVATE)
            print("Success: {member}".format(member = member))
        except Exception as e:
                print(e)

    for member in youtube_family:
        user = venmo_client.user.get_user_by_username(os.environ.get(member))
        try:
            time.sleep(random.uniform(5, 10))  # jittered delay
            venmo_client.payment.request_money(amount = youtube_amount, note = youtube_description, target_user_id = user.id, privacy_setting=PaymentPrivacy.PRIVATE)
            print("Success: {member}".format(member = member))
        except Exception as e:
                print(e)
    
    # icloud payment
    icloud_description = "icloud dues for {date}".format(date = date)
    user = venmo_client.user.get_user_by_username(os.environ.get("JAKE"))
    try:
        time.sleep(random.uniform(5, 10))  # jittered delay
        venmo_client.payment.send_money(amount = 1.99, note = icloud_description, target_user_id = user.id, privacy_setting=PaymentPrivacy.PRIVATE)
        print("Success: {member}".format(member = member))
    except Exception as e:
        if "not enough balance" in str(e).lower():
            # Fallback: pay from bank instead
            try:
                venmo_client.payment.send_money(amount = 1.99, note=icloud_description, target_user_id=user.id, funding_source_id=os.environ.get("PAYMENT_ID_1"), privacy_setting=PaymentPrivacy.PRIVATE)
                print("Success: {member} (bank fallback)".format(member=member))
            except Exception as bank_error:
                print("Bank fallback failed:", bank_error)
        else:
            print(e)
main()
