from django.shortcuts import render,redirect
from django.utils import timezone
from .models import Post,Answer
from .form import PostForm
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



