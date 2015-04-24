from django.shortcuts import render_to_response
from django.core.context_processors import csrf
from django.template import RequestContext
from django.http import HttpResponse
from social.models import *
# Create your views here.
def input_req(request):
 c=RequestContext(request)
 name_word=request.POST.get('name','')
 pass_word=request.POST.get("pass_word",'')
 name_x=request.session.get('name','')
 if request.POST.get('log out',False):
  print("inside 1")
  del request.session["name"]
  person=[]
 elif name_x:
  print("inside 3")  
  response = HttpResponse("Your favorite color is now %s" %name_x)
  response.set_cookie("nmeee",name_x)
  person=request.session["name"]
  return response
 elif user.objects.filter(name_m=name_word,password=pass_word):
  person=user.objects.filter(name_m=name_word)
  request.session["name"]=name_word
  person=name_word
  xxx=render_to_response('social.html',{"person":person},c)
  xxx.set_cookie('nameeeee',name_word)
  print("inside 2")
  return xxx
  #else :wrong usrname/pass
 else:
  person=[]
  print("inside 4")
 return render_to_response('social.html',{"person":person},c) 
