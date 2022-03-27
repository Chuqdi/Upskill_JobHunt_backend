from django.db import models
from django.utils import timezone
from users.models import User

class Company(models.Model):
    company_name = models.TextField(null=False, blank=False)
    company_mobile_contact = models.CharField(max_length=40, null=False, blank=False)
    company_address = models.TextField(null=False, blank=False)
    company_area_of_interest = models.TextField(null=False, blank=False)
    company_current_plan = models.CharField(max_length =30, null=True, blank=True)
    company_slug = models.TextField(unique=True, blank=False,null=False)
    company_is_active = models.BooleanField(default=False)
    registered_by = models.OneToOneField(User,on_delete=models.CASCADE, related_name="company")
    registerd_on = models.DateTimeField(default=timezone.now)


    def __str__(self) -> str:
        return self.user