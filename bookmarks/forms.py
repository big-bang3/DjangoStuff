from django import forms

class reg_form(forms.Form):
	name=forms.CharField(max_length=100,widget=forms.TextInput(attrs={"placeholder":"Enter your name","id":"name",}))
	password=forms.CharField(max_length=100,widget=forms.PasswordInput(render_value=False,attrs={"id":"pass1","placeholder":"Enter password",}))
	password_verify=forms.CharField(max_length=100,widget=forms.PasswordInput(render_value=False,attrs={"id":"pass2","placeholder":"Enter password Again",}))

