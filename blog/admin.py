from django.contrib import admin
from blog.models import *
# Register your models here.
class abc(admin.ModelAdmin):
 fields=['name','passw','title']
admin.site.register(blog_data,abc)
class efg(admin.ModelAdmin):
 field=['author','title','data']
admin.site.register(blog_info,efg)
