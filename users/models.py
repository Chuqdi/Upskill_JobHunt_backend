
from pyexpat import model
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.contrib.auth.hashers import make_password
from django.dispatch import receiver
from django.utils import timezone
from django.db.models.signals import post_save
from cloudinary.models import CloudinaryField



from utils.RandomStrings import GenerateRandomString


class UserManager(BaseUserManager):
    def create_user(self,email, password):
        if not email:
            raise ValueError("Please enter an email")

        if not password:
            raise ValueError("Please enter a password")

        
        email = self.normalize_email(email)
        slug = GenerateRandomString.randomStringGenerator(90)
        user = self.model(email=email,password=make_password(password), slug=slug)
        user.save(using=self._db)
        return user

    def create_superuser(self,email,password):
        user = self.create_user(email, password)
        user.is_active=True
        user.is_super=True
        user.is_admin=True
        user.is_staff=True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    email = models.EmailField(unique=True, blank=False)
    phoneNumber = models.TextField(unique=False, null=True, blank=True)
    username = models.TextField(unique=True)
    slug = models.TextField(null=False, blank=False, unique=True)
    is_super = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    is_admin= models.BooleanField(default=False)
    is_staff= models.BooleanField(default=False)

    EMAIL_FIELD = 'email'
    USERNAME_FIELD="email"
    PASSWORD_FIELD="password"
    REQUIRED_FIELDS = ['password']


    def has_perm(self, obj):
        return True

    def has_module_perms(self, obj):
        return True

    def equals(self,  object):
        return self.id == object.id
    
    object = UserManager()


class Profile(models.Model):
    first_name = models.TextField(null=True, blank=True)
    last_name= models.TextField(null=True, blank=True)
    twitterHandle = models.URLField(null=True, blank=True)
    facebookHandle = models.URLField(null=True, blank=True)
    linkedInHandle = models.URLField(null=True, blank=True)
    jobRole = models.TextField(null=True, blank=True)


    profile_image = CloudinaryField("user/profile",null=True, blank=True)
    resume = CloudinaryField("user/resume",null=True, blank=True)
    skills = models.TextField(null=True, blank=True)
    user = models.OneToOneField(User,related_name="profile", on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.user.email

class UserPaymentManager(models.Model):
    is_paid = models.BooleanField(default=False)
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="payment")
    date_paid = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.user.email


@receiver(post_save, sender=User) 
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance,profile_image ="image/upload/v1650829247/noProfileImage_bbsutn.png")
        UserPaymentManager.objects.create(user= instance)


@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()






class Sponsor(models.Model):
    email = models.EmailField(null=False, blank=False)
    website = models.TextField(null=False, blank=False)
    joined_on = models.DateTimeField(default=timezone.now)


    def __str__(self):
        return self.email