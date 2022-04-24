from django.contrib import admin
from .models import User, UserPaymentManager, Sponsor, Profile

admin.site.register(User)
admin.site.register(UserPaymentManager)
admin.site.register(Profile)
admin.site.register(Sponsor)

