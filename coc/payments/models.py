from django.db import models

class Transaction(models.Model):
    transaction_id = models.CharField(max_length=255)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    phone_number = models.CharField(max_length=20)
    status = models.CharField(max_length=20)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Transaction {self.transaction_id}"

    def get_transaction_details(transaction_id):
        try:
            transaction = Transaction.objects.get(transaction_id=transaction_id)
            return transaction
        except Transaction.DoesNotExist:
            return None  # Or handle the case where the transaction doesn't exist
