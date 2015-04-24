from django.shortcuts import render_to_response
from django.db.models import Q
from bookmarks.models import *
from django.http import HttpResponse,JsonResponse
from bookmarks.forms import reg_form
from django.template import RequestContext
from django import forms
# Create your views here.
def main_page(request):
  return render_to_response("ang.html",{"working":"working" })
  x=request.GET.get('x',False)
  f=reg_form(request.POST)
  if not x and request.method !="POST":
    return render_to_response("search_page.html",{"my_form":reg_form()},RequestContext(request))  
  elif f.is_valid():
    print("valid")
    
    data={"title":"All Fields are correct","sign":True}
    Link(name=f.cleaned_data["name"],password=f.cleaned_data["password"]).save()
    return JsonResponse(data)
    #login the user,save in database
  else:  
    print("inside else")
    try:  
      users=Link.objects.get(name=x)
      print("after try")
      if users:
        print("taken")
        data={"title":"Username is taken,please choose another","s":2}
        return JsonResponse(data)
    except Exception:
      print("accepted")
      data={"title":"Username is available","s":1}
      return JsonResponse(data)
        
