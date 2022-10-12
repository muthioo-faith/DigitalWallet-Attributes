from django.shortcuts import render,redirect
from .forms import AccountRegistrationForm, CardRegistrationForm, CustomerRegistrationForm, LoanRegistrationForm, NotificationsRegistrationForm, ReceiptRegistrationForm, RewardRegistrationForm, ThirdPartyRegistrationForm, TransactionRegistrationForm, WalletRegistrationForm
from .models import Account, Card, Customer, Loan, Notification, Receipt, Reward, ThirdParty, Transaction, Wallet

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

def customer_profile(request,id):
    customer=Customer.objects.get(id=id)
    return render(request,"customer_profile.html",
    {"customer":customer})

def edit_profile(request,id):
    customer=Customer.objects.get(id=id)
    if request.method=="POST":
        form=CustomerRegistrationForm(request.POST,instance=customer)
        if form.is_valid():
            form.save()
            return redirect("wallet/customer_profile",id=customer)
    else:
        form=CardRegistrationForm(instance=customer)
        return render(request,"edit_profile.html",{"form":form})



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

def wallet_profile(request,id):
    wallet=Wallet.objects.get(id=id)
    return render(request,"wallets_profile.html",
    {"wallets":wallet})

def edit_wallet(request,id):
    Wallet=Wallet.objects.get(id=id)
    if request.method=="POST":
        form=WalletRegistrationForm(request.POST,instance=Wallet)
        if form.is_valid():
            form.save()
            return redirect("wallet/wallet_profile",id=Wallet)
    else:
        form=WalletRegistrationForm(instance=Wallet)
        return render(request,"edit_wallet.html",{"form":form})





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


def account_profile(request,id):
    account=Account.objects.get(id=id)
    return render(request,"accounts_profile.html",
    {"accounts":account})

def edit_account(request,id):
    Account=Account.objects.get(id=id)
    if request.method=="POST":
        form=AccountRegistrationForm(request.POST,instance=Account)
        if form.is_valid():
            form.save()
            return redirect("account/account_profile",id=Account)
    else:
        form=AccountRegistrationForm(instance=Account)
        return render(request,"edit_account.html",{"form":form})


    
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


def transaction_profile(request,id):
    transaction=Transaction.objects.get(id=id)
    return render(request,"transactions_profile.html",
    {"transaction":transaction})

def edit_transaction(request,id):
    Transaction=Transaction.objects.get(id=id)
    if request.method=="POST":
        form=TransactionRegistrationForm(request.POST,instance=Transaction)
        if form.is_valid():
            form.save()
            return redirect("transaction/transaction_profile",id=Transaction)
    else:
        form=TransactionRegistrationForm(instance=Transaction)
        return render(request,"edit_transaction.html",{"form":form})





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


def card_profile(request,id):
    card=Card.objects.get(id=id)
    return render(request,"cards_profile.html",
    {"cards":card})

def edit_card(request,id):
    Card=Card.objects.get(id=id)
    if request.method=="POST":
        form=CardRegistrationForm(request.POST,instance=Card)
        if form.is_valid():
            form.save()
            return redirect("card/card_profile",id=Card)
    else:
        form=CardRegistrationForm(instance=Card)
        return render(request,"edit_card.html",{"form":form})

    


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


def thirdparty_profile(request,id):
    thirdparty=ThirdParty.objects.get(id=id)
    return render(request,"thirdparty_profile.html",
    {"thirdparty":thirdparty})

def edit_thirdparty(request,id):
    ThirdParty=ThirdParty.objects.get(id=id)
    if request.method=="POST":
        form=ThirdPartyRegistrationForm(request.POST,instance=ThirdParty)
        if form.is_valid():
            form.save()
            return redirect("thirdparty/thirdparty_profile",id=ThirdParty)
    else:
        form=ThirdPartyRegistrationForm(instance=ThirdParty)
        return render(request,"edit_thirdparty.html",{"form":form})


    

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



def notifications_profile(request,id):
    notification=Notification.objects.get(id=id)
    return render(request,"notifications_profile.html",
    {"notifications":notification})

def edit_notifications(request,id):
    Notification=Notification.objects.get(id=id)
    if request.method=="POST":
        form=NotificationsRegistrationForm(request.POST,instance=Notification)
        if form.is_valid():
            form.save()
            return redirect("notification/notification_profile",id=Notification)
    else:
        form=NotificationsRegistrationForm(instance=Notification)
        return render(request,"edit_notifications.html",{"form":form})    
    

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
    

def receipt_profile(request,id):
    receipt=Receipt.objects.get(id=id)
    return render(request,"receipts_profile.html",
    {"receipt":receipt})

def edit_receipt(request,id):
    Receipt=Receipt.objects.get(id=id)
    if request.method=="POST":
        form=ReceiptRegistrationForm(request.POST,instance=Receipt)
        if form.is_valid():
            form.save()
            return redirect("receipt/receipt_profile",id=Receipt)
    else:
        form=ReceiptRegistrationForm(instance=Receipt)
        return render(request,"edit_receipt.html",{"form":form})






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

def loan_profile(request,id):
    Loan=Loan.objects.get(id=id)
    return render(request,"loan_profile.html",
    {"loan":Loan})

def edit_loan(request,id):
    Loan=Loan.objects.get(id=id)
    if request.method=="POST":
        form=LoanRegistrationForm(request.POST,instance=Loan)
        if form.is_valid():
            form.save()
            return redirect("loan/loan_profile",id=Loan)
    else:
        form=LoanRegistrationForm(instance=Loan)
        return render(request,"edit_loan.html",{"form":form})



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

def reward_profile(request,id):
    Reward=Reward.objects.get(id=id)
    return render(request,"reward_profile.html",
    {"reward":Reward})

def edit_reward(request,id):
    Reward=Reward.objects.get(id=id)
    if request.method=="POST":
        form=RewardRegistrationForm(request.POST,instance=Reward)
        if form.is_valid():
            form.save()
            return redirect("reward/reward_profile",id=Reward)
    else:
        form=RewardRegistrationForm(instance=Loan)
        return render(request,"edit_reward.html",{"form":form})