from django.shortcuts import render
from .forms import AccountRegistrationForm, CardRegistrationForm, CustomerRegistrationForm, LoanRegistrationForm, NotificationsRegistrationForm, ReceiptRegistrationForm, RewardRegistrationForm, ThirdPartyRegistrationForm, TransactionRegistrationForm, WalletRegistrationForm
from .models import Account, Card, Customer, Loan, Notification, Receipt, Reward, ThirdParty, Wallet

# Create your views here.
def register_customer(request):

    if request.method=="POST":
        form=CustomerRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
    else:
         form= CustomerRegistrationForm()
    return render(request,"register_customer.html",{"form":form})

def list_customer(request):
    customer=Customer.objects.all()
    return render(request,"wallet/customers_list.html",{"customers":customer})


def register_wallet(request):
    if request.method=="POST":
        form=WalletRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
    else:
       form= WalletRegistrationForm()
    return render(request,"wallet.html",{"form":form})

def list_wallets(request):
    wallets=Wallet.objects.all()
    return render(request,"wallets_list.html",{"wallets":wallets})



def register_account(request):
    if request.method=="POST":
        form=AccountRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form=AccountRegistrationForm()
    return render(request,"account.html",{"form":form})
def list_accounts(request):
    accounts=Account.objects.all()
    return render(request,"accounts_list.html",{"accounts":accounts})




def register_transaction(request):
    if request.method=="POST":
        form=TransactionRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form=TransactionRegistrationForm
    return render(request,"transaction.html",{"form":form})
def list_accounts(request):
    accounts=Account.objects.all()
    return render(request,"accounts_list.html",{"accounts":accounts})


def register_card(request):
    if request.method=="POST":
        form=CardRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form=CardRegistrationForm
    return render(request,"card.html",{"form":form})
def list_cards(request):
    cards=Card.objects.all()
    return render(request,"cards_list.html",{"cards":cards})
    


def register_thirdparty(request):
    if request.method=="POST":
        form=ThirdPartyRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form=ThirdPartyRegistrationForm
    return render(request,"thirdparty.html",{"form":form})
def list_thirdparty(request):
    thirdparty=ThirdParty.objects.all()
    return render(request,"thirdparty_list.html",{"thirdparty":thirdparty})
    

def register_notifications(request):
    if request.method=="POST":
        form=NotificationsRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
    else:
       form=NotificationsRegistrationForm
    return render(request,"notifications.html",{"form":form})
def list_notifications(request):
    Notification=Notification.objects.all()
    return render(request,"notifications_list.html",{"notification":Notification})
    

def register_receipt(request):
    if request.method=="POST":
        form=ReceiptRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
    else:
       form=ReceiptRegistrationForm
    return render(request,"receipt.html",{"form":form})
def list_receipt(request):
    receipt=Receipt.objects.all()
    return render(request,"receipts_list.html",{"receipt":receipt})
    




def register_loan(request):
    if request.method=="POST":
        form=LoanRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form=LoanRegistrationForm
    return render(request,"loan.html",{"form":form})

def list_loan(request):
    loan=Loan.objects.all()
    return render(request,"loans_list.html",{"loan":loan})

def register_reward(request):
    if request.method=="POST":
        form=RewardRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
    else:
       form=RewardRegistrationForm
    return render(request,"reward.html",{"form":form})

def list_reward(request):
    reward=Reward.objects.all()
    return render(request,"reward_list.html",{"reward":reward})
