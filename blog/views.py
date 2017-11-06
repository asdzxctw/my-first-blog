from django.shortcuts import render,redirect
from django.utils import timezone
from .models import Post,Answer,cal4_ans
from .form import PostForm,cal4_ansForm
from djqscsv import render_to_csv_response

def index(request):
	return render(request, 'blog/index.html')

def post_list(request):
	posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
	return render(request, 'blog/post_list.html', {'posts': posts})

def listall(request):
	answers = Answer.objects.all().order_by('id')
	return render(request, 'blog/listall.html', {'answers': answers})

def post_answer(request):
	if request.method == 'POST':
		postform = PostForm(request.POST)
		if postform.is_valid():
			name = postform.cleaned_data['name']
			sn = postform.cleaned_data['sn']
			mobile = postform.cleaned_data['mobile']
			email = postform.cleaned_data['email']
			phone = postform.cleaned_data['phone']
			password = postform.cleaned_data['password']

			unit = Answer.objects.create(name=name,sn=sn,mobile=mobile,\
				email=email,phone=phone,password=password)
			unit.save()
			message = '提交成功！'
			return redirect('/listall/')
		else:
			message = '未通過驗證'
	else:
		message = '請填入資料'
		postform = PostForm()
	return render(request, 'blog/post_answer.html',{'message':message,'postform':postform})

def allcsv(request):
	answers = Answer.objects.all().order_by('id')
	# response = HttpResponse(content_type='text/csv')
	# response['Content-Disposition'] = 'attachment; filename="somefilename.csv"'

	# writer = csv.writer(response)
	# writer.writerow(['name', 'sn', 'mobile', 'email', 'phone', 'password'])
	# for answer in answers:
	# 	writer.writerow([answers.name, answers.sn, answers.mobile, \
	# 		answers.email, answers.phone, answers.password])

	# return response

	return render_to_csv_response(answers)

def estate_cal4(request):
	print(request.POST)
	if request.method == 'POST':
		cal4_ans_Form = cal4_ansForm(request.POST)
		if cal4_ans_Form.is_valid():
			print(cal4_ans_Form.cleaned_data)
			total = cal4_ans_Form.cleaned_data['total']
			beforeMarry = cal4_ans_Form.cleaned_data['beforeMarry']
			partnerDA = cal4_ans_Form.cleaned_data['partnerDA']
			partnerName = cal4_ans_Form.cleaned_data['partnerName']
			childName = cal4_ans_Form.cleaned_data['childName']
			parentName = cal4_ans_Form.cleaned_data['parentName']
			broName = cal4_ans_Form.cleaned_data['broName']
			gPaName = cal4_ans_Form.cleaned_data['gPaName']
			estate = cal4_ans_Form.cleaned_data['estate']
			successName = cal4_ans_Form.cleaned_data['successName']
			spendEnd = cal4_ans_Form.cleaned_data['spendEnd']
			successName2 = cal4_ans_Form.cleaned_data['successName2']
			spendEnd2 = cal4_ans_Form.cleaned_data['spendEnd2']
			childNum = cal4_ans_Form.cleaned_data['childNum']
			parentNum = cal4_ans_Form.cleaned_data['parentNum']
			broNum = cal4_ans_Form.cleaned_data['broNum']
			gPaNum = cal4_ans_Form.cleaned_data['gPaNum']

			unit = cal4_ans.objects.create(total = total, beforeMarry = beforeMarry, \
				partnerDA = partnerDA, partnerName = partnerName, childName = childName, \
				parentName = parentName, broName = broName, gPaName = gPaName, \
				estate = estate, successName = successName, spendEnd = spendEnd, \
				successName2 = successName2, spendEnd2 = spendEnd2, childNum = childNum ,\
				parentNum =parentNum ,broNum=broNum,gPaNum=gPaNum)


			unit.save()
			message = '提交成功！'
			return redirect('/estate_cal4/')
		else:
			message = '未通過驗證'
	else:
		message = '請填入資料'
		postform = PostForm()
	return render(request,"blog/estate_cal4.html",{'message':message})

