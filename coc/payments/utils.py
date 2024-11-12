# payments/utils.py
import requests
from django.conf import settings
# payments/utils.py
import base64
import datetime


def stk_push(phone_number, amount):
    access_token = get_access_token()
    url = f"{settings.MPESA_BASE_URL}/mpesa/stkpush/v1/processrequest"

    timestamp = datetime.datetime.now().strftime('%Y%m%d%H%M%S')
    password = base64.b64encode(
        f"{settings.MPESA_SHORTCODE}{settings.MPESA_PASSKEY}{timestamp}".encode()
    ).decode('utf-8')

    headers = {"Authorization": f"Bearer {access_token}"}
    payload = {
        "BusinessShortCode": settings.MPESA_SHORTCODE,
        "Password": password,
        "Timestamp": timestamp,
        "TransactionType": "CustomerPayBillOnline",
        "Amount": amount,
        "PartyA": phone_number,
        "PartyB": settings.MPESA_SHORTCODE,
        "PhoneNumber": phone_number,
        "CallBackURL": settings.CALLBACK_URL,
        "AccountReference": "Ref123",
        "TransactionDesc": "Payment"
    }

    response = requests.post(url, json=payload, headers=headers)
    return response.json()


def get_access_token():
    url = f"{settings.MPESA_BASE_URL}/oauth/v1/generate?grant_type=client_credentials"
    response = requests.get(url, auth=(settings.MPESA_CONSUMER_KEY, settings.MPESA_CONSUMER_SECRET))

    if response.status_code == 200:
        return response.json()['access_token']
    else:
        raise Exception("Failed to get access token")
