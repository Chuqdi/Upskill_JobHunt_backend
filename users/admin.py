from django.contrib import admin
from .models import User, UserPaymentManager, Sponsor

admin.site.register(User)
admin.site.register(UserPaymentManager)
admin.site.register(Sponsor)

