# views.py
from django.conf import settings
from django.http import JsonResponse, Http404
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django_daraja.mpesa.core import MpesaClient

from .models import *

mpesa_client = MpesaClient()


def payment_view(request):
    template_name = 'payments/payment_view.html'
    phone_number = '254114827103'  # Replace with customer phone number
    amount = 1  # Amount to be paid
    account_reference = 'Christian Outreach Church'
    transaction_desc = 'Payment for Service'

    callback_url = settings.CALLBACK_URL
    response = mpesa_client.stk_push(phone_number, amount, account_reference, transaction_desc, callback_url)

    if hasattr(response, 'json'):
        response_dict = response.json()
    else:
        # If it's a custom response type, extract necessary fields
        response_dict = {
            'status': 'Payment initiated',
            'message': str(response),  # Convert response object to string if needed
        }

    return render(request, template_name)

@csrf_exempt
def payment_callback(request):
    # Process the callback data from M-Pesa here
    data = request.body.decode('utf-8')
    # Perform your logic, e.g., update the payment status in your database
    return JsonResponse({"ResultCode": 0, "ResultDesc": "Accepted"})


def request_service_view(request):
    if request.method == 'POST':
        service = request.POST.get('service')
        phone_number = request.POST.get('phone_number')
        amount = 1000  # Set a predefined amount or vary based on service
        account_reference = 'ServiceUpgrade'
        transaction_desc = f'Request for {service} service'
        callback_url = request.build_absolute_uri('/payments/callback/')

        # Initiate M-Pesa STK Push
        response = mpesa_client.stk_push(
            phone_number,
            amount,
            account_reference,
            transaction_desc,
            callback_url
        )

        if response['ResponseCode'] == '0':
            return JsonResponse({"status": "Payment initiated. Check your phone to complete payment."})
        else:
            return JsonResponse({"status": "Failed to initiate payment. Try again later."})

    return render(request, 'dashboard/pages-invoice.html')


@csrf_exempt
def payment_callback(request):
    data = request.body.decode('utf-8')
    # Log or process callback data (e.g., update payment status in your database)
    return JsonResponse({"ResultCode": 0, "ResultDesc": "Accepted"})


def invoice_view(request, transaction_id):
    # Fetch transaction details from the database (or session)
    try:
        transaction = get_transaction_details(transaction_id)  # Define this function
    except Transaction.DoesNotExist:
        raise Http404("Transaction not found")

    # Render the invoice page with the transaction details
    return render(request, 'payments/invoice.html', {'transaction': transaction})
