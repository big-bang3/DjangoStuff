from django import forms
from project1.models import Login
class login_the_user(forms.Form):
    name=forms.CharField(label='Your name',max_length=100,widget=forms.TextInput(attrs={"class":"form-control","placeholder":"Your Name",}))
    password=forms.CharField(label='Enter your password',widget=forms.PasswordInput(render_value=False,attrs={"class":"form-control","placeholder":"Enter Password",}))
    password2=forms.CharField(label='Enter password again',widget=forms.PasswordInput(render_value=False,attrs={"class":"form-control","placeholder":"Enter Password Again",}))
    
class login_the_user2(forms.Form):
    name2=forms.CharField(label='',max_length=100,widget=forms.TextInput(attrs={"class":"form-control","placeholder":"Username",}))
    password3=forms.CharField(label='',widget=forms.PasswordInput(render_value=False,attrs={"class":"form-control","placeholder":"Password",}))

class take_message(forms.Form):
	#<textarea type="textarea" row=10 col=10 placeholder="Enter your message here !!!" name="sended_msg" class="form-control">
	sended_msg=forms.CharField(label="Send message",widget=forms.Textarea(attrs={"id":"send_msg","class":"form-control","placeholder":"enter your message here !!","rows":4,"cols":10,}))

