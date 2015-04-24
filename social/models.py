from django.db import models

# Create your models here.
class user(models.Model):
 name_m=models.CharField(max_length=100)
 age=models.IntegerField()
 password=models.CharField(max_length=100)
 class Admin:
  list_display = ('name_m', 'age', 'password')
  list_filter = ('name_m', 'age')
  ordering = ('name_m',)
  search_fields = ('name_m',)

 def __str__(self):
  return self.name_m
 



