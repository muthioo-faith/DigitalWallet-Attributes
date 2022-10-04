from django.db import models
from datetime import datetime
from email import message


# Create your models here.
class Customer(models.Model):
    first_name=models.CharField(max_length=15)
    last_name=models.CharField(max_length=10)
    address=models.TextField()
    email=models.EmailField()
    phonenumber=models.CharField(max_length=10)
    age=models.PositiveSmallIntegerField()
    # nationality =models.CharField(max_length=30)
    # occupation=models.CharField(max_length=30)
    # profile_picture=models.ImageField(upload_to='profile_pictures/',null=True)
    # # date_created = models.DateTimeField(default=tim.now)
    # dob =models.DateField()
    # GENDER_CHOICES =(
    #     ('M', 'Male'),
    #     ('F', 'Female'),
    # )
    # gender = models.CharField(max_length=2, choices=GENDER_CHOICES, null=True)

class Wallet(models.Model):
    customer = models.ForeignKey(default=1,on_delete=models.CASCADE, to = Customer)
    currency = models.CharField(max_length=50)
    pin = models.PositiveSmallIntegerField()
    date_created = models.DateTimeField(default=datetime.now)
    isActive = models.BooleanField()
    balance = models.BigIntegerField()
class Account(models.Model):
    account_number = models.IntegerField()
    account_name = models.CharField(max_length=100)
    wallet = models.ForeignKey(default=1,on_delete=models.CASCADE, to=Wallet)
    balance = models.PositiveIntegerField()
    account_type = models.CharField(max_length=100)

class Transaction(models.Model):
    transaction_code = models.CharField(max_length=100)
    transaction_type = models.CharField(max_length=100)
    transaction_charge = models.IntegerField()
    transaction_number = models.IntegerField()
    wallet = models.ForeignKey(default=1,on_delete=models.CASCADE, to=Wallet)
    amount = models.BigIntegerField()
    # receipt = models.OneToOneField(on_delete=models.CASCADE,to=Receipt)

class Card(models.Model):
    card_name  = models.CharField(max_length=100)
    card_number = models.CharField(max_length=100)
    expiry_date = models.DateTimeField(default=datetime.now)
    issuer = models.CharField(max_length=100)
    account = models.ForeignKey(default=1,on_delete=models.CASCADE, to=Account)
    date_issued = models.DateTimeField(default=datetime.now)

class ThirdParty(models.Model):
    third_party_name = models.CharField(max_length=100)
    transaction_cost = models.IntegerField()
    currency = models.CharField(max_length=100)
    account = models.ForeignKey(default=1,on_delete=models.CASCADE, to=Account)

class Notification(models.Model):
    message = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    # recipient = models.ForeignKey()

class Receipt(models.Model):
    amount = models.IntegerField()
    dateTime = models.DateTimeField(default=datetime.now)
    transaction  = models.PositiveIntegerField()
    receipt_type = models.CharField(max_length=100)

class Loan(models.Model):
    Wallet = models.ForeignKey(default=1,on_delete=models.CASCADE, to=Wallet)
    interest_rate = models.IntegerField()
    Loan_balance = models.IntegerField()
    # guarantor = models.ForeignKey()
    LoanTerm = models.IntegerField()
    payment_due_date = models.DateTimeField(default=datetime.now)
    purpose = models.CharField(max_length=100)
    amount = models.IntegerField()

class Reward(models.Model):
    name = models.CharField(max_length=100)
    points = models.IntegerField()
    customer_id = models.IntegerField()