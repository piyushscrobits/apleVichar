from django.db import models
from users.models import CustomUser
import uuid
from django.db.models.signals import post_delete, post_save
from django.db.models.deletion import CASCADE
from django.dispatch import receiver
# Create your models here.
class vichars(models.Model):
    vicharId = models.UUIDField(primary_key = True,default = uuid.uuid4,editable = False)
    user = models.ForeignKey(CustomUser,related_name='userVichar',on_delete=CASCADE)
    createdAt = models.DateTimeField(auto_now_add=True,editable=False)
    likes = models.IntegerField(default=0)
    vichar = models.CharField(max_length=2048)

class comment(models.Model):
    commentId = models.UUIDField(primary_key = True,default = uuid.uuid4,editable = False)
    vicharId = models.ForeignKey(vichars,on_delete=CASCADE,related_name='postComment')
    comment = models.TextField()
    user = models.ForeignKey(CustomUser,related_name='userComment',on_delete=CASCADE)

@receiver(post_save,sender=vichars)
def updateCount(sender,instance,**kwargs):
    instance.user.totalVichars += 1
    instance.user.save() 

@receiver(post_delete,sender=vichars)
def decrementCount(sender,instance,**kwargs):
    instance.user.totalVichars -= 1
    instance.user.save()
