from django.shortcuts import render_to_response
from django.template import RequestContext
from django.core.context_processors import csrf
from project1.forms import login_the_user,login_the_user2,take_message
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponseRedirect,HttpResponse,JsonResponse
from project1.models import *
from django import forms
from django.core.urlresolvers import reverse
from django.db.models import Q
import datetime


def check_msg(request):
    real_id = Login.objects.get(user=request.user).id
    d = user_message.objects.filter(reciever_id=real_id, msg_read=False)
    s = set()
    m = ''
    for i in d:
        s.add(Login.objects.get(id=i.sender_id))
    for i in s:
        m += "You have unread messages from : "+str(i)+"<br/>"
    y = {"y1": m}
    return JsonResponse(y)


def ang_msg(request):
    s = set()
    offline = []
    unread_msg = []
    online = []
    d = []
    online_and_msg = user_message.objects.filter(reciever_id = Login.objects.get(user=request.user).id, msg_read=False)
    for i in online_and_msg:
        s.add(Login.objects.get(id=i.sender_id))
    for i in s:
        x = {"name": str(i), "my_id": i.id}
        unread_msg.append(x)
    t = Login.objects.filter(online=False).exclude(name__in=s)
    for i in t:
        offline.append({"name": str(i), "my_id": i.id, "my_time": str(datetime.datetime.now()-i.last_log_in)[:-10]})
    u = Login.objects.filter(online=True).exclude(Q(user=request.user) | Q(name__in=s))
    for i in u:
        online.append({"name":str(i),"my_id":i.id})
    d.append(unread_msg)
    d.append(online)
    d.append(offline)
    return JsonResponse(d,safe=False)

# Create your views here.
def check_register(request):
    f=login_the_user()
    f2=login_the_user2() 
    c=RequestContext(request)
    if request.user.is_authenticated():
        print("inside authenticated")
        return render_to_response('proj_logged.html',{"user":request.user},RequestContext(request ))
    if request.method=='POST':
        print("inside post")
        if request.POST.get("reg",False):         
            f=login_the_user(request.POST)
            if f.is_valid():
                try:
                    user=User.objects.create_user(f.cleaned_data["name"],'',f.cleaned_data["password"])
                except Exception:
                    er="This Username is already taken.Please try another"
                    return render_to_response('proj1.html',{"form":f,"login_form":f2,"er":er},c)
                l=Login(user=user,name=f.cleaned_data["name"])
                l.save()
                return render_to_response('proj1.html',{"form":f,"login_form":f2,"success_submit":True},c)
        else:
            print("trying to login again")
            f2=login_the_user2(request.POST)
            err="Username/Password did not match.Please try again"
            if f2.is_valid():
                user=authenticate(username=f2.cleaned_data["name2"],password=f2.cleaned_data["password3"])
                if user:
                    try:
                        x=Login.objects.get(user=user)
                        x.online=True
                        x.save()
                       # logged_in_users(user=user).save()
                        login(request,user)
                        print(x)
                        return HttpResponseRedirect(reverse('testpge'))
                    except Exception :
                        return render_to_response('proj1.html',{"form":f,"login_form":f2,"err":"Id already in use"},c) 
                    #return render_to_response('proj_logged.html',{"user":user,"user_list":Login.objects.all(),"online_list":logged_in_users.objects.all()})
                else:
                    return render_to_response('proj1.html',{"form":f,"login_form":f2,"err":err},c)
            else:return render_to_response('proj1.html',{"form":f,"login_form":f2,"err":"Please give valid input"},c)
      
    return render_to_response('proj1.html',{"form":f,"login_form":f2},c)
def log_user_out(request):
    #print("inside")
    x=Login.objects.get(user=request.user)
    x.online=False
    #x.last_log_in = datetime.datetime.now()
    #print(datetime.datetime.now())
    x.save()
  #  logged_in_users.objects.get(user=request.user).delete()
    logout(request)    
    return HttpResponseRedirect("../")
def message_user(request,user_id):
    real_id=Login.objects.get(user=request.user).id
    m=take_message(request.POST)
    got_message=request.POST.get('sended_msg',False)
    if m.is_valid():
        user_message(sender_id=real_id,reciever_id=user_id,message=m.cleaned_data['sended_msg'],msg_read=False).save()
        return HttpResponseRedirect("/project1/"+user_id)
    sender_message_list=list(user_message.objects.filter(Q(sender_id=real_id,reciever_id=user_id) | Q(sender_id=user_id,reciever_id=real_id)).order_by("created"))[-10:]
   # print(real_id)
    return render_to_response('proj_logged.html',{"chat_name":Login.objects.get(id=user_id),"message_list":sender_message_list,"input_form":take_message(),"user":request.user},RequestContext(request ))

def aj_req(request,user_id=1):
    print("inside ajax req")
    map_mon = ['Jan','Feb','March','April','May','June','July','Aug','Sep','Oct','Nov','Dec']
    data1 = str()
    x = str()
    x1=str()
    x2=str()
    if  user_id:
        real_id = Login.objects.get(user = request.user).id
        m = user_message.objects.filter(sender_id = user_id,reciever_id = real_id,msg_read = False)
        for i in m:
            i.msg_read=True
            i.save()
        """   d = user_message.objects.filter(reciever_id = real_id,msg_read = False)
        s = set()
        
        for i in d :
            s.add(Login.objects.get(id=i.sender_id))
            for j in s:
                 x += str(j)+"<br/>"
        y = Login.objects.filter(online=False).exclude(name__in=s) 
        for i in y:
            x1 += str(i)+"<br/>"
        z = Login.objects.filter(online=True).exclude(Q(user=request.user) | Q(name__in=s))
        for i in z:
            x2 += str(i)+"<br/>"     
        #print("sender id = %s and reciever_id =%s" % (real_id,user_id)) """
        sender_message_list=list(user_message.objects.filter(Q(sender_id=real_id,reciever_id=user_id) | Q(sender_id=user_id,reciever_id=real_id)).order_by("created")) [-10:]
       # print(len(sender_message_list)) 
        data3 = []
        for i in sender_message_list:
            #data1+=str(i)+"`"
            x,y = map(str,str(i.created).split())
            x1,y1 = map(str,str(i).split("*e&^1"))
            data2 = {'key1':x1,'key1_msg':y1,'time':y[:8],'date':x[-2:]+','+map_mon[int(x[5:7])-1]}
            data3.append(data2)
#           print(data2["key1"])
        #data={"data1":data1}#,"online_and_msg":x,"user_list":x1,"online_list":x2}"""
    return JsonResponse(data3,safe=False)