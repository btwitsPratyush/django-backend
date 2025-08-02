from django.db import models

# Create your models here.
class Payout(models.Model):
    recipient_name = models.CharField(max_length=100)
    recipient_account = models.CharField(max_length=50)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=20, choices=[('pending', 'Pending'), ('completed', 'Completed')])
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.recipient_name} - ₹{self.amount}"