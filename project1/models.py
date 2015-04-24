from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Login(models.Model):
    user=models.OneToOneField(User)
    name=models.CharField(max_length=100)
    online=models.BooleanField(default=False)
    last_log_in = models.DateTimeField(auto_now=True)
 #   bday=models.DateField()
    def __str__(self):
        return self.name

class user_message(models.Model):
    sender_id=models.IntegerField(max_length=100,unique=False,default=1)
    reciever_id=models.IntegerField(max_length=100,default=1,unique=False)
    message=models.CharField(max_length=300,unique=False)
    created = models.DateTimeField(auto_now_add=True)
    msg_read = models.BooleanField(default = True)

    def __str__(self):
        #return "from %s to %s" %(User.objects.get(id=self.sender_id).username,Login.objects.get(id=self.reciever_id).name)
        return "%s*e&^1  %s" %(Login.objects.get(id=self.sender_id).name,self.message)
   #     return str(self.sender_id)
    