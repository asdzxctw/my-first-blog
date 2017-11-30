from django.http import HttpResponse
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
    #   writer.writerow([answers.name, answers.sn, answers.mobile, \
    #       answers.email, answers.phone, answers.password])

    # return response

    return render_to_csv_response(answers)

def allcalcsv(request):
    answers = cal4_ans.objects.all().order_by('id')
    return render_to_csv_response(answers)

def calculate(request):
    if request.method == 'POST':
        cal4_ans_Form = cal4_ansForm(request.POST)
        if cal4_ans_Form.is_valid():
            print(cal4_ans_Form.cleaned_data)
            cal4_ans_Form.save()
    return HttpResponse(0)


    

def estate_cal4(request):

    estate = ""
    successName = ""
    successName2 = ""
    spendEnd = ""
    spendEnd2 = ""

    if request.method == 'POST':
        cal4_ans_Form = cal4_ansForm(request.POST)
        if cal4_ans_Form.is_valid():
            print(cal4_ans_Form.cleaned_data)
            cal4_ans_Form.save()
            total = cal4_ans_Form.cleaned_data['total']
            beforeMarry = cal4_ans_Form.cleaned_data['beforeMarry']
            partnerDA = cal4_ans_Form.cleaned_data['partnerDA']
            partnerName = cal4_ans_Form.cleaned_data['partnerName']
            childName = cal4_ans_Form.cleaned_data['childName']
            parentName = cal4_ans_Form.cleaned_data['parentName']
            broName = cal4_ans_Form.cleaned_data['broName']
            gPaName = cal4_ans_Form.cleaned_data['gPaName']
            # estate = cal4_ans_Form.cleaned_data['estate']
            # successName = cal4_ans_Form.cleaned_data['successName']
            # spendEnd = cal4_ans_Form.cleaned_data['spendEnd']
            # successName2 = cal4_ans_Form.cleaned_data['successName2']
            # spendEnd2 = cal4_ans_Form.cleaned_data['spendEnd2']
            childNum = cal4_ans_Form.cleaned_data['childNum']
            parentNum = cal4_ans_Form.cleaned_data['parentNum']
            broNum = cal4_ans_Form.cleaned_data['broNum']
            gPaNum = cal4_ans_Form.cleaned_data['gPaNum']

            total = int(total)
            beforeMarry = int(beforeMarry)
            childNum = int(childNum)
            parentNum = int(parentNum)
            broNum = int(broNum)
            gPaNum = int(gPaNum)
            if(partnerName == None):
                partnerName = ''

            if(parentName == None):
                parentName = ''

            if(broName == None):
                broName = ''
            
            if(childName == None):
                childName = ''
            
            if(gPaName == None):
                gPaName = ''
            

            estateTemp = total - beforeMarry

            if(estateTemp < 0):
                estate = "建議拋棄繼承"
                spendEnd = "建議拋棄繼承"
            else:
                estate = estateTemp
                spendTemp = estateTemp
                if(partnerDA=='0'):
                    successName = "配偶已不在"
                    spendEnd = "無繼承額度"
                    if(childNum==0):
                        if(parentNum==0):
                            if(broNum==0):
                                if(gPaNum==0):
                                    spendEnd2 = "沒有繼承人，歸國庫。"   
                                else:
                                    spendEnd2 = (spendTemp/gPaNum)
                                    successName2 = "祖父母" + gPaName
                            else:
                                spendEnd2 = (spendTemp/broNum)
                                successName2 = "兄弟姐妹" + broName
                        else:
                            spendEnd2 = (spendTemp/parentNum)
                            successName2 = "父母" + parentName                              
                    else:
                        spendEnd2 = (spendTemp / childNum)
                        successName2 = "子女" + childName
                else:
                    successName = "配偶" + partnerName
                    spendTemp = estateTemp
                    spendTemp2 = estateTemp
                    if(childNum==0):
                        if(parentNum==0):
                            if(broNum==0):
                                if(gPaNum==0):
                                    spendEnd = spendTemp
                                else:
                                    spendEnd = spendTemp*2/3
                                    spendEnd2 = spendTemp2/3/gPaNum
                                    successName2 = "祖父母" + gPaName
                            else:
                                spendEnd = spendTemp/2
                                spendEnd2 = spendTemp2/2/broNum
                                successName2 = "兄弟姐妹" + broName
                        else:
                            spendEnd = spendTemp/2
                            spendEnd2 = spendTemp2/2/parentNum
                            successName2 = "父母" + parentName
                    else:
                        spendEnd = spendTemp/(childNum+1)
                        spendEnd2 = spendTemp2/(childNum+1)
                        successName2 = "子女" + childName

            print({'estate':estate,'spendEnd':spendEnd,\
            'successName':successName,'spendEnd2':spendEnd2,'successName2':successName2})

            message = '提交成功！'
        else:
            message = '未通過驗證'
    else:
        message = '請填入資料'
    return render(request,"blog/estate_cal4.html",{'estate':estate,'spendEnd':spendEnd,\
        'successName':successName,'spendEnd2':spendEnd2,'successName2':successName2})

