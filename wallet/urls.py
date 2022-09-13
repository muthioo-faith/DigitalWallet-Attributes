from django.urls import path
from .views import list_accounts, list_cards, list_customer, list_loan, list_notifications, list_receipt, list_reward, list_thirdparty, list_wallets, register_loan, register_notifications, register_receipt, register_reward, register_thirdparty, register_account, register_card, register_customer, register_transaction, register_wallet

urlpatterns =[
    path("register/",register_customer,name="registration"),
    path("wallet/",register_wallet,name="wallet"),
    path("account/",register_account,name="account"),
    path("transaction/",register_transaction,name="transaction"),
    path("card/",register_card,name="card"),
    path("thirdparty/",register_thirdparty,name="thirdparty"),
    path("notifications/",register_notifications,name="notifications"),
    path("receipt/",register_receipt,name="receipt"),
    path("loan/",register_loan,name="loan"),
    path("reward/",register_reward,name="reward"),

    path("customers/",list_customer,name="list_customers"),
    path("wallets/",list_wallets,name="list_wallets"),
    path("accounts/",list_accounts,name="list_accounts"),
    path("cards/",list_cards,name="list_cards"),
    path("thirdparty/",list_thirdparty,name="list_thirdparty"),
    path("notifications/",list_notifications,name="list_notifications"),
    path("receipts/",list_receipt,name="list_receipts"),
    path("loans/",list_loan,name="list_loans"),
    path("rewards/",list_reward,name="list_rewards"),

















]