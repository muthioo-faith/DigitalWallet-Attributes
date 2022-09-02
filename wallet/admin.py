from django.contrib import admin
from .models import Customer,Wallet,Account,Transaction,Card,ThirdParty,Notification,Loan,Receipt,Reward

# Register your models here.
class CustomerAdmin(admin.ModelAdmin):
    list_display=("first_name","last_name","address","email","phonenumber","age")
    search_fields=("first_name","last_name","address","email","phonenumber","age")   
admin.site.register(Customer,CustomerAdmin)

class WalletAdmin(admin.ModelAdmin):
    list_display=("customer","currency","pin","date_created","isActive","balance")
    search_fields=("currency","customer","pin","date_created","isActive","balance")
admin.site.register(Wallet,WalletAdmin)

class AccountAdmin(admin.ModelAdmin):
 list_display=("account_name","account_number","wallet","balance")
search_fields=("account_name","account_number","wallet","balance"),
admin.site.register(Account, AccountAdmin)

class TransctionAdmin(admin.ModelAdmin):
 list_display=("transaction_code","transaction_type","wallet","amount")
search_fields=("transaction_code")
admin.site.register(Transaction,TransctionAdmin)

class CardAdmin(admin.ModelAdmin):
 list_display=("card_name","card_number")
search_fields=("card_name","card_number")
admin.site.register(Card,CardAdmin)

class ThirdPartyAdmin(admin.ModelAdmin):
    list_display=("third_party_name","transaction_cost")
    search_fields=("third_party_name","transaction_cost")
admin.site.register(ThirdParty,ThirdPartyAdmin)

class NotificationAdmin(admin.ModelAdmin):
    list_display=("message","title")
    search_fields=("message","title")
admin.site.register(Notification,NotificationAdmin)

class ReceiptAdmin(admin.ModelAdmin):
    list_display=("amount","dateTime","transaction")
    search_fields=("amount","dateTime","transaction")
admin.site.register(Receipt,ReceiptAdmin)

class LoanAdmin(admin.ModelAdmin):
    list_display=("Wallet","Loan_balance","LoanTerm","purpose","amount","interest_rate")
    search_fields=("Wallet","Loan_balance","LoanTerm","purpose","amount","interest_rate")
admin.site.register(Loan,LoanAdmin)

class RewardAdmin(admin.ModelAdmin):
    list_display=("name","customer_id","points")
    search_fields=("name","customer_id","points")
admin.site.register(Reward,RewardAdmin)
