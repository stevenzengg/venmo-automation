# main.py

import os
from venmo_api import Client, PaymentPrivacy
import datetime
from datetime import datetime

TOKEN_KEY = 'VENMO_ACCESS_TOKEN'

def main():
    # load the access token from environ
    access_token = os.environ.get(TOKEN_KEY)
    if access_token is None:
        raise ValueError('[!] EVERYTHING IS BROKEN WE CANT GET ACCESSS AHHHHHH')

    venmo_client = Client(access_token=access_token)
    spotify_family = ["JERRY", "PRACHI", "SAHIL", "ROHAN", "SREYA"]
    amount = 3.34
    now = datetime.now()
    date = str(now.month) + "/" + str(now.year)
    for member in spotify_family:
        user = venmo_client.user.get_user_by_username(os.environ.get(member))
        description = "spotify {date}".format(date = date)
        try:
            venmo_client.payment.request_money(amount = amount, note = description, target_user_id = user.id, privacy_setting=PaymentPrivacy.PRIVATE)
            print("Success: {member}".format(member = member))
        except Exception as e:
                print(e)

main()
