from django.shortcuts import render_to_response
from django.core.context_processors import csrf
from django.template import RequestContext
from blog.models import *
from django.http import HttpResponseRedirect
# Create your views here.
def blog_req(request):
 name=request.POST.get('name','')
 passw = request.POST.get('pass','')
 c=RequestContext(request)
 data=blog_info.objects.all()
 blog_id=blog_info.objects.values('id')
 val=[]
 for i in blog_id:
  val.append(i.get('id'))
 #blog_id=blog_id.values()
 data=zip(data,val)
 if blog_data.objects.filter(name=name,passw=passw):
  logged_in=True
  request.session["name"]=name
 elif request.POST.get("log_out",False):
  logged_in=False
  request.session["name"]=False
 elif request.session.get("name",False):logged_in=True
 else:
  logged_in=False
 return render_to_response('blog.html',{"msg":data,"logged_in":logged_in,"session_name":request.session.get("name",'')},c)
def blog_input(request):
 c=RequestContext(request)
 allowed=request.session.get('name',False)
 title=request.POST.get('name',False)
 msg=request.POST.get('msg',False)
 if msg and title:
  data=blog_info(author=request.session.get('name',''),title=title,data=msg)
  data.save()
  return HttpResponseRedirect('../')
 return render_to_response('blog_input.html',{"allowed":allowed},c)
def blog_showdata(request):
 try:
  offset=request.GET.get('id','')
  row=blog_info.objects.filter(id=offset)
  val=row.values()
  data=val[0].get('data')
 except Exception: 
  return render_to_response('blog_error.html')
 return render_to_response('blog_display.html',{"data":data})
 