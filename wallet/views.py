from django.shortcuts import render
from .forms import AccountRegistrationForm, CardRegistrationForm, CustomerRegistrationForm, LoanRegistrationForm, NotificationsRegistrationForm, ReceiptRegistrationForm, RewardRegistrationForm, ThirdPartyRegistrationForm, TransactionRegistrationForm, WalletRegistrationForm

# Create your views here.
def register_customer(request):
    form= CustomerRegistrationForm()
    return render(request,"register_customer.html",{"form":form})


def register_wallet(request):
    form= WalletRegistrationForm()
    return render(request,"wallet.html",{"form":form})


def register_account(request):
    form=AccountRegistrationForm()
    return render(request,"account.html",{"form":form})

def register_transaction(request):
    form=TransactionRegistrationForm
    return render(request,"transaction.html",{"form":form})

def register_card(request):
    form=CardRegistrationForm
    return render(request,"card.html",{"form":form})

def register_thirdparty(request):
    form=ThirdPartyRegistrationForm
    return render(request,"thirdparty.html",{"form":form})

def register_notifications(request):
    form=NotificationsRegistrationForm
    return render(request,"notifications.html",{"form":form})


def register_receipt(request):
    form=ReceiptRegistrationForm
    return render(request,"receipt.html",{"form":form})

def register_loan(request):
    form=LoanRegistrationForm
    return render(request,"receipt.html",{"form":form})


def register_reward(request):
    form=RewardRegistrationForm
    return render(request,"receipt.html",{"form":form})
