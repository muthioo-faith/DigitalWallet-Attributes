from django.urls import path
from .views import register_loan, register_notifications, register_receipt, register_reward, register_thirdparty, register_account, register_card, register_customer, register_transaction, register_wallet

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









]