import base64
from datetime import datetime, date

from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

# Create your views here.
from myapp.models import *


def login(request):
    return render(request,'loginindex.html')





def login_post(request):
    a=request.POST['textfield']
    b=request.POST['textfield2']
    result=Login.objects.filter(username=a,password=b)
    if result.exists():
        result2=Login.objects.get(username=a,password=b)
        request.session['lid']=result2.id
        if result2.type=='admin':
            return HttpResponse('''<script>alert('Admin login success fully');window.location='/myapp/admin_home/'</script>''')


        elif result2.type=='company':
            return HttpResponse('''<script>alert('Company login success fully');window.location='/myapp/company_home/'</script>''')


        else:
            return HttpResponse(
                '''<script>alert('invalid');window.location='/myapp/login/'</script>''')
    else:
        return HttpResponse(
            '''<script>alert('invalid');window.location='/myapp/login/'</script>''')



def logout(request):
    request.session['lid']=''
    return HttpResponse('''<script>alert('Logout');window.location='/myapp/login/'</script>''')

def home(request):
    if request.session['lid'] == "":
        return HttpResponse('''<script>alert(' Logout SuccessFully');window.location='/myapp/login'</script>''')
    return render(request,'admin/adminindex.html')

def admin_change_password(request):
    if request.session['lid']=="":
        return HttpResponse('''<script>alert(' Logout SuccessFully');window.location='/myapp/login'</script>''')

    return render(request,'admin/Admin_change_password.html')


def admin_change_password_post(request):
    if request.session['lid'] == "":
        return HttpResponse('''<script>alert(' Logout SuccessFully');window.location='/myapp/login'</script>''')

    old = request.POST['old_password']
    new = request.POST['new_password']
    confirm = request.POST['con_password']
    result=Login.objects.filter(id=request.session['lid'],password=old)
    if result.exists():
        if new==confirm:
            Login.objects.filter(id=request.session['lid']).update(password=confirm)
            return HttpResponse('''<script>alert('Successfully changed');window.location='/myapp/login/'</script>''')
        else:
            return HttpResponse('''<script>alert('Invalid');window.location='/myapp/admin_home/'</script>''')
    else:
        return HttpResponse('''<script>alert('Invalid');window.location='/myapp/admin_home/'</script>''')




def category(request):
    if request.session['lid'] == "":
        return HttpResponse('''<script>alert(' Logout SuccessFully');window.location='/myapp/login'</script>''')
    return render(request,'admin/add_category.html')

def category_post(request):
    if request.session['lid'] == "":
        return HttpResponse('''<script>alert(' Logout SuccessFully');window.location='/myapp/login'</script>''')

    category = request.POST['category']
    if Category.objects.filter(category_name=category ).exists():
        return HttpResponse('''<script>alert('Category already exists');window.location='/myapp/category/'</script>''')



    var=Category()
    var.category_name=category
    var.save()
    return HttpResponse('''<script>alert('Success');window.location='/myapp/category/'</script>''')




def view_category(request):
    if request.session['lid'] == "":
        return HttpResponse('''<script>alert(' Logout SuccessFully');window.location='/myapp/login'</script>''')

    var=Category.objects.all()
    return render(request,'admin/view_category.html',{'data':var})


def view_category_post(request):
    if request.session['lid'] == "":
        return HttpResponse('''<script>alert(' Logout SuccessFully');window.location='/myapp/login'</script>''')
    search=request.POST['category']
    var=Category.objects.filter(category_name__icontains=search)
    return render(request,'admin/view_category.html',{'data':var})


def edit_category(request,id):
    var=Category.objects.get(id=id)
    return render(request,'admin/edit_category.html',{'data':var})



def edit_category_post(request):
    id=request.POST['id']
    category=request.POST['category']
    var=Category.objects.get(id=id)
    var.category_name=category
    var.save()
    return HttpResponse('''<script>alert('Success');window.location='/myapp/view_category/'</script>''')



def delete_category(request,id):
    var=Category.objects.get(id=id)
    var.delete()

    return HttpResponse('''<script>alert('Success');window.location='/myapp/view_category/'</script>''')



def add_skill(request):
    if request.session['lid'] == "":
        return HttpResponse('''<script>alert(' Logout SuccessFully');window.location='/myapp/login'</script>''')
    return render(request,'admin/add_skill.html')
def add_skill_post(request):
    if request.session['lid'] == "":
        return HttpResponse('''<script>alert(' Logout SuccessFully');window.location='/myapp/login'</script>''')
    skil=request.POST['skil']
    var=Skill()
    var.skil=skil
    var.save()
    return HttpResponse('''<script>alert('Success');window.location='/myapp/add_skill/'</script>''')


def view_skill(request):
    if request.session['lid'] == "":
        return HttpResponse('''<script>alert(' Logout SuccessFully');window.location='/myapp/login'</script>''')

    var=Skill.objects.all()
    return render(request,'admin/view_skill.html',{'data':var})


def view_skill_post(request):
    if request.session['lid'] == "":
        return HttpResponse('''<script>alert(' Logout SuccessFully');window.location='/myapp/login'</script>''')

    search=request.POST['skill']
    var=Skill.objects.filter(skil__icontains=search)
    return render(request,'admin/view_skill.html',{'data':var})



def edit_skill(request,id):
    var=Skill.objects.get(id=id)
    return render(request,'admin/edit_skill.html',{'data':var})



def edit_skill_post(request):
    id=request.POST['id']
    skill=request.POST['skill']
    var=Skill.objects.get(id=id)
    var.skil=skill
    var.save()
    return HttpResponse('''<script>alert('Success');window.location='/myapp/view_skill/'</script>''')



def delete_skill(request,id):
    var=Skill.objects.get(id=id)
    var.delete()

    return HttpResponse('''<script>alert('Success');window.location='/myapp/view_skill/'</script>''')




def view_Company(request):
    if request.session['lid'] == "":
        return HttpResponse('''<script>alert(' Logout SuccessFully');window.location='/myapp/login'</script>''')

    var=Company.objects.filter(status='pending')
    return render(request,'admin/admin_view_Company.html',{'data':var})

def view_Company_post(request):
    if request.session['lid'] == "":
        return HttpResponse('''<script>alert(' Logout SuccessFully');window.location='/myapp/login'</script>''')

    search = request.POST['searching']
    var = Company.objects.filter(name__icontains=search)
    return render(request,'admin/admin_view_Company.html',{'data':var})




def view_aproved_Comapany(request):
    if request.session['lid'] == "":
        return HttpResponse('''<script>alert(' Logout SuccessFully');window.location='/myapp/login'</script>''')

    var=Company.objects.filter(status='approved')
    return render(request,'admin/admin_view_aproved_Company.html',{'data':var})


def view_aproved_Comapany_post(request):
    search=request.POST['searching']
    var=Company.objects.filter(name__icontains=search,status='approved')
    return render(request,'admin/admin_view_aproved_Company.html',{'data':var})



def view_rejected_Comapany(request):
    if request.session['lid'] == "":
        return HttpResponse('''<script>alert(' Logout SuccessFully');window.location='/myapp/login'</script>''')

    var=Company.objects.filter(status='rejected')
    return render(request,'admin/admin_view_rejected_Company.html',{'data':var})



def view_rejected_Comapany_post(request):
    search=request.POST['searching']
    var=Company.objects.filter(name__icontains=search,status='rejected')
    return render(request,'admin/admin_view_aproved_Company.html',{'data':var})




def aproving_company(request,id):
    if request.session['lid'] == "":
        return HttpResponse('''<script>alert(' Logout SuccessFully');window.location='/myapp/login'</script>''')

    Company.objects.filter(LOGIN_id=id).update(status='approved')
    Login.objects.filter(id=id).update(type='company')


    return HttpResponse('''<script>alert('Company Approved');window.location='/myapp/view_aproved_Comapany/'</script>''')


def reject_company(request,id):
    if request.session['lid'] == "":
        return HttpResponse('''<script>alert(' Logout SuccessFully');window.location='/myapp/login'</script>''')

    Company.objects.filter(LOGIN_id=id).update(status='rejected')
    Login.objects.filter(id=id).update(type='pending')


    return HttpResponse('''<script>alert('Company Rejected');window.location='/myapp/view_rejected_Comapany/'</script>''')


def view_complaint(request):
    if request.session['lid'] == "":
        return HttpResponse('''<script>alert(' Logout SuccessFully');window.location='/myapp/login'</script>''')

    var=Complaint.objects.all()
    return render(request, 'admin/View_complaint.html',{'var':var})



def view_complaint_post(request, ):
    if request.session['lid'] == "":
        return HttpResponse('''<script>alert(' Logout SuccessFully');window.location='/myapp/login'</script>''')

    fromD=request.POST['f']
    to=request.POST['t']
    var=Complaint.objects.filter(date__range=[fromD,to])

    return render(request, 'admin/View_complaint.html', {'var': var})




def send_reply(request,id):
    if request.session['lid'] == "":
        return HttpResponse('''<script>alert(' Logout SuccessFully');window.location='/myapp/login'</script>''')
    var=Complaint.objects.get(id=id)
    return render(request,'admin/send_reply.html',{'data':var})



def send_reply_post(request):
    reply=request.POST['reply']
    id=request.POST['id']
    date=datetime.now().date().today()

    var=Complaint.objects.get(id=id)
    var.date=date
    var.status='Replied'
    var.reply=reply
    var.save()

    return HttpResponse('''<script>alert(' Reply SuccessFully Sent');window.location='/myapp/view_complaint/'</script>''')




def view_review(request):
    if request.session['lid'] == "":
        return HttpResponse('''<script>alert(' Logout SuccessFully');window.location='/myapp/login'</script>''')

    var=Review.objects.all()
    return render(request, 'admin/View_review.html',{'var':var})

def view_review_post(request):
    if request.session['lid'] == "":
        return HttpResponse('''<script>alert(' Logout SuccessFully');window.location='/myapp/login'</script>''')

    fromD = request.POST['f']
    to = request.POST['t']
    var = Review.objects.filter(date__range=[fromD, to])

    return render(request, 'admin/View_review.html',{'var':var})



def view_user(request):
    var=User.objects.all()
    return render(request,'admin/view__user.html',{'data':var})


def view_user_post(request):
    if request.session['lid'] == "":
        return HttpResponse('''<script>alert(' Logout SuccessFully');window.location='/myapp/login'</script>''')

    search = request.POST['search']
    var = User.objects.filter(name__icontains=search)
    return render(request,'admin/view__user.html',{'data':var})




# company

def company(request):
    return render(request,'Company/companyreg.html')


def company_post(request):


    name=request.POST['name']
    email=request.POST['email']
    phone=request.POST['phone']
    place=request.POST['place']
    pin=request.POST['pin']
    post=request.POST['post']
    password=request.POST['password']
    confirm=request.POST['confirm']

    var=Login.objects.filter(username=email)
    if var.exists():
        return HttpResponse('''<script>alert(' Email Already Taken');window.location='/myapp/login'</script>''')



    if password==confirm:
        log = Login()
        log.username = email
        log.password = confirm
        log.type = 'pending'
        log.save()

        image = request.FILES['image']
        date = datetime.now().strftime('%Y%m%d-%H%M%S') + '.jpg'

        fs = FileSystemStorage()
        fs.save(date, image)
        path = fs.url(date)

        var = Company()
        var.LOGIN = log
        var.name = name
        var.email = email
        var.phone = phone
        var.pin = pin
        var.post = post
        var.place = place
        var.logo = path
        var.status='pending'
        var.save()
        return HttpResponse('''<script>alert(' Register Successfull');window.location='/myapp/login'</script>''')


    else:

        return HttpResponse('''<script>alert(' innvalid ');window.location='/myapp/login'</script>''')



def company_home(request):
    if request.session['lid'] == "":
        return HttpResponse('''<script>alert(' Logout SuccessFully');window.location='/myapp/login'</script>''')
    return render(request,'Company/companyindex.html')



def company_change_password(request):
    if request.session['lid']=="":
        return HttpResponse('''<script>alert(' Logout SuccessFully');window.location='/myapp/login'</script>''')

    return render(request,'Company/company_change_password.html')


def company_change_password_post(request):
    if request.session['lid'] == "":
        return HttpResponse('''<script>alert(' Logout SuccessFully');window.location='/myapp/login'</script>''')

    old = request.POST['old_password']
    new = request.POST['new_password']
    confirm = request.POST['con_password']
    result=Login.objects.filter(id=request.session['lid'],password=old)
    if result.exists():
        if new==confirm:
            Login.objects.filter(id=request.session['lid']).update(password=confirm)
            return HttpResponse('''<script>alert('Successfully changed');window.location='/myapp/login/'</script>''')
        else:
            return HttpResponse('''<script>alert('Invalid');window.location='/myapp/company_change_password/'</script>''')
    else:
        return HttpResponse('''<script>alert('Invalid');window.location='/myapp/company_change_password/'</script>''')




def company_profile(request):
    if request.session['lid'] == "":
        return HttpResponse('''<script>alert(' Logout SuccessFully');window.location='/myapp/login'</script>''')

    var=Company.objects.get(LOGIN_id=request.session['lid'])

    return render(request, 'Company/company_profile.html',{'data':var})

def edit_company(request,id):

    var=Company.objects.get(id=id)
    return render(request,'Company/edit_company.html',{'data':var})

def edit_company_post(request):
    id=request.POST['id']
    name=request.POST['name']
    phone=request.POST['phone']
    place=request.POST['place']
    pin=request.POST['pin']
    post=request.POST['post']






    var=Company.objects.get(id=id)
    var.name=name
    var.phone=phone
    var.pin=pin
    var.post=post
    var.place=place

    if 'image' in request.FILES:
        image = request.FILES['image']
        date = datetime.now().strftime('%Y%m%d-%H%M%S') + '.jpg'

        fs = FileSystemStorage()
        fs.save(date, image)
        path = fs.url(date)
        var.logo=path
    var.save()


    return HttpResponse('''<script>alert('  Successfull');window.location='/myapp/company_profile/'</script>''')

def add_jobs(request):
    if request.session['lid'] == "":
        return HttpResponse('''<script>alert(' Logout SuccessFully');window.location='/myapp/login'</script>''')
    var=Category.objects.all()
    dt=date.today()

    return render(request,'Company/add_jobs.html',{'data':var,'dt':str(dt)})

def add_jobs_post(request):
    jobname =request.POST['name']
    qualification = request.POST['qualification']
    salary = request.POST['salary']
    experience = request.POST['experience']
    Interview = request.POST['Interview']
    CATEGORY = request.POST['cat']
    var=Jobs()
    var.jobname=jobname
    var.qualification=qualification
    var.salary=salary
    var.interview_date=Interview
    var.experience=experience
    var.CATEGORY=Category.objects.get(id=CATEGORY)
    var.COMPANY=Company.objects.get(LOGIN_id=request.session['lid'])

    var.save()
    return HttpResponse('''<script>alert('  Successfull');window.location='/myapp/add_jobs/'</script>''')


def view_jobs(request):
    if request.session['lid'] == "":
        return HttpResponse('''<script>alert(' Logout SuccessFully');window.location='/myapp/login'</script>''')
    var=Jobs.objects.filter(COMPANY__LOGIN_id=request.session['lid'])
    return render(request,'Company/view_jobs.html',{'data':var})


def view_jobs_post(request):
    search=request.POST['search']
    var=Jobs.objects.filter(jobname__icontains=search)
    return render(request,'Company/view_jobs.html',{'data':var})
def delete_job(request,id):
    var=Jobs.objects.get(id=id)
    var.delete()
    return HttpResponse('''<script>alert('  Deleted');window.location='/myapp/view_jobs/'</script>''')

def edit_jobs(request,id):
    var=Jobs.objects.get(id=id)
    var2=Category.objects.all()
    dt=date.today()
    return render(request,'Company/edit_jobs.html',{'data':var,'data1':var2,'dt':str(dt)})

def edit_jobs_post(request):
    id =request.POST['id']
    jobname =request.POST['name']
    qualification = request.POST['qualification']
    salary = request.POST['salary']
    experience = request.POST['experience']
    Interview = request.POST['Interview']
    CATEGORY = request.POST['cat']

    var=Jobs.objects.get(id=id)
    var.jobname=jobname
    var.qualification=qualification
    var.salary=salary
    var.interview_date=Interview
    var.experience=experience
    var.CATEGORY=Category.objects.get(id=CATEGORY)
    var.COMPANY=Company.objects.get(LOGIN_id=request.session['lid'])
    var.save()
    return HttpResponse('''<script>alert('  Successfull');window.location='/myapp/view_jobs/'</script>''')


def add_job_skill(request):
    if request.session['lid'] == "":
        return HttpResponse('''<script>alert(' Logout SuccessFully');window.location='/myapp/login'</script>''')


    var=Skill.objects.all()
    var2=Jobs.objects.filter(COMPANY__LOGIN_id=request.session['lid'])
    return render(request,'Company/add_jobs_skill.html',{'data':var,'data2':var2})


def add_job_skill_post(request):
    JOB=request.POST['job']
    SKILL=request.POST['skill']
    var=Jobs_Skill()
    var.JOB=Jobs.objects.get(id=JOB)
    var.SKILL=Skill.objects.get(id=SKILL)
    var.save()
    return HttpResponse('''<script>alert('  Successfull');window.location='/myapp/add_job_skill/'</script>''')


def view_jobs_skill(request):
    if request.session['lid'] == "":
        return HttpResponse('''<script>alert(' Logout SuccessFully');window.location='/myapp/login'</script>''')
    var=Jobs_Skill.objects.filter(JOB__COMPANY__LOGIN_id=request.session['lid'])
    return render(request,'Company/view_jobs_skill.html',{'data':var})


def view_jobs_skill_post(request):
    search=request.POST['search']
    var=Jobs_Skill.objects.filter(JOB__jobname__icontains=search)
    return render(request,'Company/view_jobs_skill.html',{'data':var})



def delete_jobskill(request,id):
    var=Jobs_Skill.objects.get(id=id)
    var.delete()
    return HttpResponse('''<script>alert('  Deleted');window.location='/myapp/view_jobs/#about'</script>''')


def edit_jobskill(request,id):
    var=Jobs_Skill.objects.get(id=id)
    var3=Jobs.objects.all()
    var4=Skill.objects.all()
    return render(request,'Company/edit_jobs_skill.html',{'data':var,'data3':var3,'data4':var4})

def edit_jobskill_post(request):
    ID = request.POST['id']
    JOB = request.POST['job']
    SKILL = request.POST['skill']
    var = Jobs_Skill.objects.get(id=ID)
    var.JOB = Jobs.objects.get(id=JOB)
    var.SKILL = Skill.objects.get(id=SKILL)
    var.save()

    return HttpResponse('''<script>alert('  Updated');window.location='/myapp/view_jobs_skill/'</script>''')


def view_job_review(request):
    if request.session['lid'] == "":
        return HttpResponse('''<script>alert(' Logout SuccessFully');window.location='/myapp/login'</script>''')
    var=Jobs_rating.objects.filter(JOB__COMPANY__LOGIN_id=request.session['lid'])
    return render(request,'Company/View_job_review.html',{'data':var})



def view_job_review_post(request):
    from1=request.POST['f']
    to=request.POST['t']
    var=Jobs_rating.objects.filter(date__range=[from1,to])
    return render(request,'Company/View_job_review.html',{'data':var})




def view_job_application(request):
    if request.session['lid'] == "":
        return HttpResponse('''<script>alert(' Logout SuccessFully');window.location='/myapp/login'</script>''')
    var=Application.objects.filter(JOB__COMPANY__LOGIN_id=request.session['lid'],status='pending')
    return render(request,'Company/view_jobs_application.html',{'data':var})

def view_job_application_post(request):
    from1 = request.POST['f']
    to = request.POST['t']
    var = Application.objects.filter(date__range=[from1, to],status='pending')
    return render(request,'Company/view_jobs_application.html',{'data':var})



def confirm_application(request,id):
    var=Application.objects.filter(id=id).update(status='confirmed')
    return HttpResponse('''<script>alert('  Confirmed');window.location='/myapp/view_job_application/'</script>''')
def reject_application(request,id):
    var=Application.objects.filter(id=id).update(status='rejected')
    return HttpResponse('''<script>alert('  Rejected');window.location='/myapp/view_job_application/'</script>''')

def view_confirmed_job_application(request):
    if request.session['lid'] == "":
        return HttpResponse('''<script>alert(' Logout SuccessFully');window.location='/myapp/login'</script>''')
    var=Application.objects.filter(JOB__COMPANY__LOGIN_id=request.session['lid'],status='confirmed')
    return render(request,'Company/view_confirmed_jobs_application.html',{'data':var})


def view_confirmed_job_application_post(request):
    from1 = request.POST['f']
    to = request.POST['t']
    var = Application.objects.filter(date__range=[from1, to],status='confirmed')
    return render(request,'Company/view_confirmed_jobs_application.html',{'data':var})

def view_rejected_job_application_post(request):
    from1 = request.POST['f']
    to = request.POST['t']
    var = Application.objects.filter(date__range=[from1, to],status='rejected')
    return render(request,'Company/view_rejected_job_application.html',{'data':var})


def view_rejected_job_application(request):
    var=Application.objects.filter(JOB__COMPANY__LOGIN_id=request.session['lid'],status='rejected')
    return render(request,'Company/view_rejected_job_application.html',{'data':var})




# users

def login2(request):
    a = request.POST['uname']
    b = request.POST['psw']
    result = Login.objects.filter(username=a, password=b)
    if result.exists():
        result2 = Login.objects.get(username=a, password=b)
        if result2.type == 'user':
            lid=result2.id
            usr=User.objects.get(LOGIN_id=lid)
            # return JsonResponse({'status':"ok",'lid':str(lid)})
            return JsonResponse({'status':"ok",'lid':str(lid),'type':'user','photo':usr.image,'name':usr.name})

        else:
            return JsonResponse({'status': 'not Ok'})
    else:
        return JsonResponse({'status': 'not Ok'})








def user_post_new(request):

    name=request.POST['name']
    phone=request.POST['phone']
    email=request.POST['email']
    gender=request.POST['gender']
    place=request.POST['place']
    pin=request.POST['pin']
    post=request.POST['post']
    dob=request.POST['dob']
    password=request.POST['password']
    conf=request.POST['confirm']

    if password==conf:
        image = request.POST['image']
        fs1 = base64.b64decode(image)
        date1 = datetime.now().strftime("%Y%m%d-%H%M%S") + ".jpg"

        open(r'C:\Users\GAYATHRI\PycharmProjects\Careerrecomendation\media\user\\' + date1, 'wb').write(fs1)

        path1 = "/media/user/" + date1

        var = Login()
        var.username = email
        var.password = password


        var.type = 'user'
        var.save()

        result = User()
        result.LOGIN = var
        result.name = name
        result.email = email
        result.gender = gender
        result.phone = phone
        result.dob=dob
        result.pin=pin
        result.post=post
        result.place=place

        result.image=path1
        result.save()
        return JsonResponse({'status': "ok"})
    else:
        return JsonResponse({'status': "Not Ok"})


def user_profile_new(request):


    lid=request.POST['lid']
    var=User.objects.get(LOGIN_id=lid)
    return JsonResponse({'status': "ok",'name':var.name,'email':var.email,'phone':var.phone,'gender':var.gender,'image':var.image,'dob':var.dob,'place':var.place,'post':var.post,'pin':var.pin})

def edit_userprofile(request):

    lid = request.POST['loginid']
    name = request.POST['name']
    phone = request.POST['phone']
    email = request.POST['email']
    gender = request.POST['gender']
    image = request.POST['image']
    place = request.POST['place']
    pin = request.POST['pin']
    post = request.POST['post']
    dob = request.POST['dob']

    result = User.objects.get(LOGIN_id=lid)
    result.name = name
    result.email = email
    result.phone=phone
    result.place=place
    result.pin=pin
    result.post=post
    result.dob=dob

    result.gender = gender

    if len(image) > 1:
        fs1 = base64.b64decode(image)
        date1 = datetime.now().strftime("%Y%m%d-%H%M%S") + ".jpg"
        open(r'C:\Users\GAYATHRI\PycharmProjects\Careerrecomendation\media\user\\' + date1, 'wb').write(fs1)
        path1 = "/media/user/" + date1
        result.image = path1

    result.save()
    return JsonResponse({'status': "ok"})



def user_view_complaints(request):
    var=request.POST['lid']
    var2=User.objects.get(LOGIN=var)
    result=Complaint.objects.filter(USER=var2)
    l =[]
    for i in result:
        l.append({'id':i.id, 'complaint':i.complaint,'date':i.date,'reply':i.reply,'status':i.status})
    return JsonResponse({'status': "ok", 'data':l})


def user_complaint_post(request):
    var=request.POST['comp']
    lid=request.POST['lid']
    date=datetime.now().date().today()

    c_obj=Complaint()
    c_obj.complaint=var
    c_obj.date=date
    uid=User.objects.get(LOGIN_id=lid)
    c_obj.USER=uid
    c_obj.save()

    return JsonResponse({'status': "ok"})


def user_changepassword(request):
    lid = request.POST['lid']
    old = request.POST['old']
    newpass = request.POST['new']
    confirm = request.POST['confirm']

    var = Login.objects.filter(id=lid, password=old)
    if var.exists():
        if newpass == confirm:
            var2 = Login.objects.filter(id=lid).update(password=confirm)
            return JsonResponse({'status': 'ok'})
        else:
            return JsonResponse({'status': 'Not ok'})
    else:
        return JsonResponse({'status': 'NoT Ok'})


def user_review_post(request):
    var=request.POST['review']
    var2=request.POST['rate']
    lid=request.POST['lid']
    date=datetime.now().date().today()

    c_obj=Review()
    c_obj.review=var
    c_obj.rating=var2
    c_obj.date=date
    uid=User.objects.get(LOGIN_id=lid)
    c_obj.USER=uid
    c_obj.save()

    return JsonResponse({'status': "ok"})


def user_experience_post(request):


    company=request.POST['company']
    experience=request.POST['experience']
    joined_date=request.POST['joined_date']
    lid=request.POST['lid']

    c_obj=Experinece()
    c_obj.company=company
    c_obj.experience=experience
    c_obj.joined_date=joined_date
    uid=User.objects.get(LOGIN_id=lid)
    c_obj.USER=uid
    c_obj.save()

    return JsonResponse({'status': "ok"})



def view_experience(request):
    var=request.POST['lid']
    var2=User.objects.get(LOGIN=var)



    result=Experinece.objects.filter(USER=var2)
    l =[]
    for i in result:
        l.append({'id':i.id, 'company':i.company,'experience':i.experience,'joined_date':i.joined_date})
    return JsonResponse({'status': "ok", 'data':l})




def user_view_application(request):
    var=request.POST['lid']
    var2=User.objects.get(LOGIN=var)



    result=Application.objects.filter(USER=var2)
    l =[]
    for i in result:
        l.append({'id':i.id, 'JOB':i.JOB.jobname,'date':i.date,'status':i.status})
    return JsonResponse({'status': "ok", 'data':l})




def user_view_jobs(request):
    var=request.POST['lid']
    var2=User.objects.get(LOGIN=var)



    # result=Jobs_Skill.objects.filter(USER=var2)
    result=Jobs.objects.all()
    l =[]
    for i in result:
        l.append({'id':i.id, 'JOB':i.jobname,'qualification':i.qualification,'experience':i.experience,'company':i.COMPANY.name,'totalvacancy':i.totalvacancy,'interview_date':i.interview_date})
    return JsonResponse({'status': "ok", 'data':l})



def user_view_company(request):
    var=request.POST['lid']
    var2=User.objects.get(LOGIN=var)



    # result=Jobs_Skill.objects.filter(USER=var2)
    result=Company.objects.all()
    l =[]
    for i in result:
        l.append({'id':i.id, 'name':i.name,'email':i.email,'phone':i.phone,'logo':i.logo,'place':i.place,'pin':i.pin,'post':i.post})
    return JsonResponse({'status': "ok", 'data':l})


def user_qualification_post(request):
    print(request.POST)
    type=request.POST['type']
    course=request.POST['course']
    university=request.POST['university']
    yearofpass=request.POST['yearofpass']
    grade=request.POST['grade']
    lid=request.POST['lid']


    c_obj=Qualification()
    c_obj.type=type
    c_obj.course=course
    c_obj.university=university
    c_obj.yearofpass=yearofpass
    c_obj.grade=grade
    uid=User.objects.get(LOGIN_id=lid)
    c_obj.USER=uid
    c_obj.save()

    return JsonResponse({'status': "ok"})


def user_view_qualification(request):
    var=request.POST['lid']
    var2=User.objects.get(LOGIN=var)



    result=Qualification.objects.filter(USER=var2)
    l =[]
    for i in result:
        l.append({'id':i.id, 'type':i.type,'course':i.course,'university':i.university,'yearofpass':i.yearofpass,'grade':i.grade})
    return JsonResponse({'status': "ok", 'data':l})



def user_addskills(request):
    skill=request.POST['skills']
    sk=skill.split(',')
    lid=request.POST['lid']
    print(skill)
    for i in sk:
        if MySkill.objects.filter(SKILL_id=i,USER__LOGIN_id=lid).exists():
            continue
        ms=MySkill()
        ms.SKILL_id=i
        ms.USER=User.objects.get(LOGIN=lid)
        ms.save()
    return JsonResponse({'status': "ok"})
        # else:
        #     return JsonResponse({'status': "no"})


def user_ViewSkills(request):
    pobj = Skill.objects.all()
    l = []
    for vac in pobj:
        l.append({"id":vac.id,"skill": vac.skill})
    print(l)
    return JsonResponse({'status': "ok", "data": l})


def user_ViewMySkills(request):
    lid=request.POST['lid']
    pobj = MySkill.objects.filter(USER=User.objects.get(LOGIN=lid))
    l = []
    for vac in pobj:
        l.append({"id":vac.id,"skill": vac.SKILL.skill})
    print(l)
    return JsonResponse({'status': "ok", "data": l})


def user_deleteskills(request):
    sid=request.POST['sid']
    pobj = MySkill.objects.get(id=sid).delete()
    return JsonResponse({'status': "ok"})



def user_view_own_qualification(request):
    id=request.POST['qid']
    i=Qualification.objects.get(id=id)
    l ={'id':i.id, 'type':i.type,'course':i.course,'university':i.university,'yearofpass':i.yearofpass,'grade':i.grade}
    return JsonResponse({'status':'ok','data':l})


def user_qualification_edit_post(request):
    print(request.POST)
    qid=request.POST['qid']
    type=request.POST['type']
    course=request.POST['course']
    university=request.POST['university']
    yearofpass=request.POST['yearofpass']
    grade=request.POST['grade']


    c_obj=Qualification.objects.get(id=qid)
    c_obj.type=type
    c_obj.course=course
    c_obj.university=university
    c_obj.yearofpass=yearofpass
    c_obj.grade=grade
    c_obj.save()

    return JsonResponse({'status': "ok"})


def view_user_edit_experience(request):
    eid=request.POST['cid']
    i=Experinece.objects.get(id=eid)
    l ={'id':i.id, 'company':i.company,'experience':i.experience,'joined_date':i.joined_date}
    return JsonResponse({'status': "ok", 'data':l})

def user_edit_experience_post(request):
    print(request.POST)


    cid=request.POST['cid']
    company=request.POST['company']
    experience=request.POST['experience']
    joined_date=request.POST['joined_date']

    c_obj=Experinece.objects.get(id=cid)
    c_obj.company=company
    c_obj.experience=experience
    c_obj.joined_date=joined_date
    c_obj.save()

    return JsonResponse({'status': "ok"})






def add_refference(request):
    print(request.POST)
    narration = request.POST['narration']
    name = request.POST['name']
    phone = request.POST['phone']
    email = request.POST['email']
    lid = request.POST['lid']

    c_obj = Refference()
    c_obj.narration = narration
    c_obj.name = name
    c_obj.phone = phone
    c_obj.email = email
    uid = User.objects.get(LOGIN_id=lid)
    c_obj.USER = uid
    c_obj.save()

    return JsonResponse({'status': "ok"})



def user_view_own_refference(request):
    id=request.POST['lid']
    result=Refference.objects.filter(USER__LOGIN_id=id)

    l=[]
    for i in result:
        l.append({'id':i.id, 'narration':i.narration,'name':i.name,'phone':i.phone,'email':i.email})
    return JsonResponse({'status':'ok','data':l})




def user_edit_reffernce(request):
    eid=request.POST['cid']
    i=Refference.objects.get(id=eid)
    l ={'id':i.id, 'narration':i.narration,'name':i.name,'phone':i.phone,'email':i.email}
    return JsonResponse({'status': "ok", 'data':l})

def user_edit_refference_post(request):
    print(request.POST)


    cid=request.POST['cid']
    narration=request.POST['narration']
    name=request.POST['name']
    phone=request.POST['phone']
    email=request.POST['email']

    c_obj=Refference.objects.get(id=cid)
    c_obj.narration=narration
    c_obj.name=name
    c_obj.phone=phone
    c_obj.email=email
    c_obj.save()

    return JsonResponse({'status': "ok"})


def delete_refference(request):
    sid=request.POST['did']
    pobj = Refference.objects.filter(id=sid).delete()
    return JsonResponse({'status': "ok"})


def delete_qualification(request):
    sid=request.POST['did']
    pobj = Qualification.objects.filter(id=sid).delete()
    return JsonResponse({'status': "ok"})

def delete_experience(request):
    sid=request.POST['did']
    pobj = Experinece.objects.filter(id=sid).delete()
    return JsonResponse({'status': "ok"})





def sent_job_review1(request):
    lid=request.POST['lid']
    review=request.POST['review']
    rating=request.POST['rate']
    job=request.POST['job_id']

    date=datetime.now().date().today()
    var=Jobs_rating()
    var.USER=User.objects.get(LOGIN_id=lid)
    var.Review=review
    var.Rating=rating
    var.date=date
    var.JOB_id=job
    var.save()

    return JsonResponse({'status': "ok"})






def user_view_select_jobs(request):
    id=request.POST['lid']
    j=Jobs.objects.filter(interview_date__gt=datetime.now())
    sk=Skill.objects.all()
    L=[]
    label=[]
    for i in j:
        a=[]
        for k in sk:
            if Jobs_Skill.objects.filter(SKILL=k,JOB=i).exists():
                a.append(1)
            else:
                a.append(0)
        L.append(a)
        label.append(i.id)
    test_feature=[]
    for i in sk:
        if MySkill.objects.filter(USER__LOGIN_id=id).exists():
            test_feature.append(1)
        else:
            test_feature.append(0)

    from sklearn.ensemble import RandomForestClassifier
    a=RandomForestClassifier()
    a.fit(L,label)
    s=a.predict_proba([test_feature])
    print(s)

    print(label,"hurraaiaaiai")

    result = Jobs.objects.all()
    l = []
    s=s[0]
    for ii in  range(len(label)):
        if s[ii] > .5:
            i=Jobs.objects.get(id=label[ii])
            l.append({'id': i.id, 'JOB': i.jobname, 'qualification': i.qualification, 'experience': i.experience,
                  'company': i.COMPANY.name, 'totalvacancy': i.totalvacancy, 'interview_date': i.interview_date})
    return JsonResponse({'status': "ok", 'data': l})



def user_apply_post(request):

    jobid= request.POST["jid"]
    lid= request.POST["lid"]

    if Application.objects.filter(JOB_id= jobid, USER__LOGIN_id=lid).exists():
        return JsonResponse({'status':'nop'})
    else:

        aa=Application()
        aa.JOB_id= jobid
        aa.USER= User.objects.get(LOGIN_id= lid)
        aa.date= datetime.now()
        aa.status="Pending"
        aa.save()

        return JsonResponse({'status': "ok" })



def admin_view_jobs(request,id):

    var = Jobs_Skill.objects.filter(JOB__jobname__icontains=search)


    var = Jobs.objects.filter(COMPANY_id=id)
    return render(request, 'admin/view_jobs.html', {'data': var})


def company_view_jobs_skill(request,id):

    var = Jobs_Skill.objects.filter(JOB__COMPANY_id=id)


    return render(request, 'Company/view_jobs_skill.html', {'data': var})

