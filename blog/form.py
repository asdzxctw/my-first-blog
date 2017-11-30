from django import forms
from .models import cal4_ans

class PostForm(forms.Form):
	name = forms.CharField(max_length=20)
	sn = forms.CharField(max_length=20)
	mobile = forms.CharField(max_length=20)
	email = forms.EmailField(max_length=100)
	phone = forms.CharField(max_length=20)
	password = forms.CharField(max_length=20)

class cal4_ansForm(forms.ModelForm):

    class Meta:
        model = cal4_ans
        fields = ['total',
		'beforeMarry',
		'partnerDA',
		'partnerName',
		'childName',
		'parentName',
		'broName',
		'gPaName',
		'estate',
		'successName',
		'spendEnd',
		'successName2',
		'spendEnd2',
		'childNum',
		'parentNum',
		'broNum',
		'gPaNum']