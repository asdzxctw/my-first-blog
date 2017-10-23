from django import forms

class PostForm(forms.Form):
	name = forms.CharField(max_length=20)
	sn = forms.CharField(max_length=20)
	mobile = forms.CharField(max_length=20)
	email = forms.EmailField(max_length=100)
	phone = forms.CharField(max_length=20)
	password = forms.CharField(max_length=20)