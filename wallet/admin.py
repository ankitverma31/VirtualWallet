from django.contrib import admin
from .models import  Owner, Debit,Recharge,Transfer,ReceivedAmount,CodeSent,CodeReceived
admin.site.register(Owner)
admin.site.register(Debit)
admin.site.register(Recharge)
admin.site.register(Transfer)
admin.site.register(ReceivedAmount)
admin.site.site_title = 'Virtual Wallet'
admin.site.site_header = 'Virtual Wallet'









