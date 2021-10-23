from django.db import models
from django.db.models.fields.related import ForeignKey
from django.utils.translation import ugettext_lazy as _
from django.db import models
from django.contrib.auth.models import AbstractUser,UserManager
from django.conf import settings
from django.db.models.signals import post_delete, post_save
from django.dispatch import receiver
from django.db.models.deletion import CASCADE
from rest_framework.authtoken.models import Token
import uuid
# Create your models here.

class CustomUser(AbstractUser):
    email = None
    userId = models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False,unique=True)
    gender = models.CharField(max_length=1)
    totalVichars = models.IntegerField(default=0)
    points = models.IntegerField(default=0)
    REQUIRED_FIELDS = []
    objects = UserManager()

@receiver(post_save,sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender,instance = None,created=False,**kwargs):
    if created:
        token = Token.objects.create(user=instance)