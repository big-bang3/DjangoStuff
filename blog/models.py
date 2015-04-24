from django.db import models

# Create your models here.
class blog_data(models.Model):
 name=models.CharField(max_length=100)
 passw=models.CharField(max_length=100)
 title=models.CharField(max_length=100,null=True,blank=True)
 def __str__(self):
  return self.name
class blog_info(models.Model):
 author=models.CharField(max_length=100)
 title=models.CharField(max_length=100)
 data=models.CharField(max_length=1000)
 def __str__(self):
  return '%s posted by - %s' % (self.title, self.author)

    #code
