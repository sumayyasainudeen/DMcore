from django.shortcuts import render
from venv import create
import qrcode
import random
import os, json, math
# import psycopg2
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from urllib.parse import urlencode
from django.views.decorators.csrf import csrf_exempt
from django. contrib import messages
from unicodedata import name
# pip install openpyxl
from openpyxl import Workbook

from django.shortcuts import render, redirect
from .models import *
from datetime import datetime,date, timedelta
from django.http import HttpResponse, HttpResponseRedirect
from django.db.models import Q
from io import BytesIO
from django.core.files import File
from django.conf import settings
from django.db.models import Q
from num2words import num2words
from django.http import JsonResponse
from django.core.mail import send_mail

from django.core.files.storage import FileSystemStorage

from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa


from django.views.decorators.http import require_GET

import requests

from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseRedirect
# Create your views here.

from datetime import datetime, time, timedelta
from django.db.models.functions import TruncHour
from datetime import time

from datetime import datetime, timedelta, time
#----------------------------------------------------------Login, Sign Up, Reset, Internshipform 
def login(request):
    return render(request, 'home/login.html')

def signin(request):
    
    if request.method == 'POST':
        email  = request.POST['email']
        password = request.POST['password']
        user = authenticate(username=email, password=password)
        if user is not None:
            return redirect('login')
        
        if user_registration.objects.filter(email=request.POST['email'], password=request.POST['password'],department="Admin",status="active").exists():

            member = user_registration.objects.get(email=request.POST['email'],password=request.POST['password'])
            
            request.session['userid'] = member.id
            
            return redirect('ad_profile')


        elif user_registration.objects.filter(email=request.POST['email'], password=request.POST['password'],department="Digital Marketing Head",status="active").exists():
            member = user_registration.objects.get(email=request.POST['email'],password=request.POST['password'])
            request.session['userid'] = member.id
            return redirect('he_profile')

        elif user_registration.objects.filter(email=request.POST['email'], password=request.POST['password'],department="Digital Marketing Executive",status="active").exists():
            member = user_registration.objects.get(email=request.POST['email'],password=request.POST['password'])
            request.session['userid'] = member.id

            return redirect('ex_profile')
        else:
           
            return redirect('login')


           

def signup(request):
    return render(request, 'home/signup.html')

def registration_form(request):

 
    a = user_registration()
    b = qualification()
    c = extracurricular()

    if request.method == 'POST':
        if  user_registration.objects.filter(email=request.POST['email']).exists():
            
            msg_error = "Mail id already exist"
            return render(request, 'home/signup.html',{'msg_error': msg_error})
        else:
            
            a.fullname = request.POST['fname']
            a.fathername = request.POST['fathername']
            a.mothername = request.POST['mothername']
            a.dateofbirth = request.POST['dob']
            a.gender = request.POST['gender']
            a.presentaddress1 = request.POST['address1']
            a.presentaddress2  =  request.POST['address2']
            a.presentaddress3 =  request.POST['address3']
            a.pincode = request.POST['pincode']
            a.district  =  request.POST['district']
            a.state  =  request.POST['state']
            a.country  =  request.POST['country']
            a.permanentaddress1 = request.POST['paddress1']
            a.permanentaddress2  =  request.POST['paddress2']
            a.permanentaddress3  =  request.POST['paddress3']
            a.permanentpincode = request.POST['ppincode']
            a.permanentdistrict  =  request.POST['pdistrict']
            a.permanentstate  =  request.POST['pstate']
            a.permanentcountry =  request.POST['pcountry']
            a.mobile = request.POST['mobile']
            a.alternativeno = request.POST['alternative']
            a.department = request.POST['department']
            a.email = request.POST['email']
            a.status = "active"
            a.designation = request.POST['designation']
            a.password= random.SystemRandom().randint(100000, 999999)
            
            #a.branch_id = request.POST['branch']
            a.photo = request.FILES['photo']
            a.idproof = request.FILES['idproof']
            a.save()
            
            x = user_registration.objects.get(id=a.id)
            today = date.today()
            tim = today.strftime("%m%y")
            x.employee_id = "INF"+str(tim)+''+"B"+str(x.id)
            passw=x.password
            email_id=x.email
            x.save()
            y1 = user_registration.objects.get(id=a.id)
            qr = qrcode.make("http://altoscore.in/offerletter/" + str(y1.id))
            qr.save(settings.MEDIA_ROOT + "/images"+"//" +"offer"+str(y1.id) + ".png")
            with open(settings.MEDIA_ROOT + "/images"+"//"+"offer"+ str(y1.id) +".png","rb") as reopen:
                    djangofile = File(reopen)
                    y1.offerqr = djangofile
                    y1.save()
    
            y2 = user_registration.objects.get(id=a.id)
            qr1 = qrcode.make("http://altoscore.in/relieveletter/" + str(y2.id))
            qr1.save(settings.MEDIA_ROOT + "/images"+"//"+"re" +str(y2.id) + ".png")
            with open(settings.MEDIA_ROOT + "/images"+"//"+"re" + str(y2.id) + ".png", "rb") as reopen:
                    djangofile = File(reopen)
                    y2.relieveqr = djangofile
                    y2.save()
            y3 = user_registration.objects.get(id=a.id)
            qr2 = qrcode.make("http://altoscore.in/experienceletter/" + str(y3.id))
            qr2.save(settings.MEDIA_ROOT + "/images"+"//"+"exp" +str(y3.id) + ".png")
            with open(settings.MEDIA_ROOT + "/images"+"//"+"exp" + str(y3.id) + ".png", "rb") as reopen:
                    djangofile = File(reopen)
                    y3.expqr = djangofile
                    y3.save()
           
    
            b.user_id = a.id
            b.plustwo = request.POST.get('plustwo')
            b.school = request.POST['school']
            b.schoolaggregate = request.POST['aggregate']
            if request.FILES.get('cupload') is not None:
                b.schoolcertificate = request.FILES['cupload']
            b.ugdegree = request.POST['degree']
            b.ugstream = request.POST['stream']
            b.ugpassoutyr = request.POST['passoutyear']
            b.ugaggregrate = request.POST['aggregate1']
            b.backlogs = request.POST['supply']
            if request.FILES.get('cupload1') is not None:
                b.ugcertificate = request.FILES['cupload1']
            b.pg = request.POST['pg']
            b.save()
    
            c.user_id = a.id
            c.internshipdetails = request.POST['details']
            c.internshipduration = request.POST['duration']
            c.internshipcertificate = request.POST['certificate']
            c.onlinetrainingdetails = request.POST['details1']
            c.onlinetrainingduration = request.POST['duration1']
            c.onlinetrainingcertificate= request.POST['certificate1']
            c.projecttitle = request.POST['title']
            c.projectduration = request.POST['duration2']
            c.projectdescription = request.POST['description']
            c.projecturl = request.POST['url']
            c.skill1 = request.POST['skill1']
            c.skill2 = request.POST['skill2']
            c.skill3 = request.POST['skill3']
            c.save()
            
            subject = 'Greetings from ALTOS TECHNOLOGIES'
            message = 'Congratulations,\nYou have successfully registered ALTOS TECHNOLOGIES.\nYour login credentials \n\nEmail :'+str(email_id)+'\nPassword :'+str(passw)+'\n\nNote: This is a system generated email, do not reply to this email id.'
            email_from = settings.EMAIL_HOST_USER
            
            recipient_list = [email_id, ]
            send_mail(subject,message , email_from, recipient_list, fail_silently=True)
            msg_success = "Registration successfully Check Your Registered Mail"
            return redirect('login')
        
    return redirect('login')



def reset_password(request):
    if request.method == "POST":
        email_id = request.POST.get('email')
        access_user_data = user_registration.objects.filter(email=email_id).exists()
        if access_user_data:
            _user = user_registration.objects.get(email=email_id)
            password = random.SystemRandom().randint(100000, 999999)

            _user.password = password
            subject = 'iNFOX Technologies your authentication data updated'
            message = 'Password Reset Successfully\n\nYour login details are below\n\nUsername : ' + str(email_id) + '\n\nPassword : ' + str(password) + \
                '\n\nYou can login this details\n\nNote: This is a system generated email, do not reply to this email id'
            email_from = settings.EMAIL_HOST_USER
            recipient_list = [email_id, ]
            send_mail(subject, message, email_from,
                      recipient_list, fail_silently=True)

            _user.save()
            msg_success = "Password Reset successfully check your mail new password"
            return render(request, 'home/Reset_password.html', {'msg_success': msg_success})
        else:
            msg_error = "This email does not exist iNFOX Technologies "
            return render(request, 'home/Reset_password.html', {'msg_error': msg_error})

    return render(request,'home/Reset_password.html')

def internshipform(request):
    # branch = branch_registration.objects.all()
    return render(request, 'home/internship.html')

def internship_save(request):

    a = internship()
    if request.method == 'POST':
        try:
            a.fullname = request.POST['name']
            a.collegename = request.POST['college_name']
            a.reg_date = datetime.now()
            a.reg_no = request.POST['reg_no']
            a.course = request.POST['course']
            a.stream = request.POST['stream']
            a.platform = request.POST['platform']

            a.start_date =  request.POST['start_date']
            a.end_date  =  request.POST['end_date']
            a.mobile  =  request.POST['mobile']

            a.alternative_no  =  request.POST['alternative_no']

            a.email = request.POST['email']
            a.profile_pic  =  request.FILES['profile_pic']
            if (a.end_date<a.start_date):
                return render(request,'home/internship.html',{'a':a})
            else:
                a.save()
                qr = qrcode.make("https://altoscore.in/admin_code?id=" + str(a.id))
                qr.save(settings.MEDIA_ROOT + "\\" +str(a.id) + ".png")
                with open(settings.MEDIA_ROOT + "\\" + str(a.id) + ".png", "rb") as reopen:
                        djangofile = File(reopen)
                        a.qr = djangofile

                        a.save()
           
            msg_success="Your application has been sent successfully"
            Flag='True'
            return render(request, 'home/internship.html',{'msg_success':msg_success})
        except:
            message = "Enter all details !!!"
            return render(request, 'home/internship.html',{'message':message})
    else:
        
        return render(request, 'home/internship.html')



# -----------------------------------------------------------------------------Admin Section

def ad_base(request):
    ids=request.session['userid']
    usr = user_registration.objects.get(id=ids)
    context={
        "usr":usr,
    }
    return render(request, 'admin/ad_base.html',context)

def ad_profile(request):
    ids=request.session['userid']
    usr = user_registration.objects.get(id=ids)
    context={
        "usr":usr,
    }
    return render(request, 'admin/ad_profile.html',context )

def ad_dashboard(request):
    ids=request.session['userid']
    usr = user_registration.objects.get(id=ids)
    context={
        "usr":usr,
    }
    return render(request, 'admin/ad_dashboard.html',context)

def ad_create_work(request):
    ids=request.session['userid']
    usr = user_registration.objects.get(id=ids)
    context={
        "usr":usr,
    }
    return render(request, 'admin/ad_create_work.html',context)

def save_create_work(request):
    client = client_information()
    ids=request.session['userid']
    usr = user_registration.objects.get(id=ids)
    
    if request.session.has_key('userid'):
        userid = request.session['userid']
    else:
       return redirect('/')
    if request.method == 'POST':
        client.client_name = request.POST.get('client_name')
        
        client.client_address = request.POST.get('client_address')
        client.client_mail = request.POST.get('client_mail')
        client.bs_name = request.POST.get('bs_name')
        client.bs_website = request.POST.get('bs_website',None)
       
        client.bs_location = request.POST.get('bs_location')
        client.client_files = request.FILES.get('client_files',None)
        client.seo = request.POST.get('seo',None)
        client.seo_txt = request.POST.get('seo_txt',None)
        client.seo_file = request.FILES.get('seo_file',None)
        client.seo_target = request.POST.get('seo_target',None)

        client.on_pg = request.POST.get('onpage',None)
        client.on_pg_txt = request.POST.get('on_txt',None)
        client.on_pg_file = request.FILES.get('on_file',None)
        client.on_pg_target = request.POST.get('on_target',None)

        client.off_pg = request.POST.get('offpage',None)
        client.off_pg_txt = request.POST.get('off_txt',None)
        client.off_pg_file = request.FILES.get('off_file',None)
        client.off_pg_target = request.POST.get('off_target',None)

        client.smm = request.POST.get('smm',None)
        client.smm_txt = request.POST.get('smm_txt',None)
        client.smm_file = request.FILES.get('smm_file',None)
        client.smm_target = request.POST.get('smm_target',None)
        client.smo = request.POST.get('smo',None)
        client.smo_txt = request.POST.get('smo_txt',None)
        client.smo_file = request.FILES.get('smo_file',None)
        client.smo_target = request.POST.get('smo_target',None)

        client.sem = request.POST.get('sem',None)
        client.sem_txt = request.POST.get('sem_txt',None)
        client.sem_file = request.FILES.get('sem_file',None)
        client.sem_target = request.POST.get('sem_target',None)
        client.em = request.POST.get('em',None)
        client.em_txt = request.POST.get('em_txt',None)
        client.em_file = request.FILES.get('em_file',None)
        client.em_target = request.POST.get('em_target',None)
        client.cm = request.POST.get('cm',None)
        client.cm_txt = request.POST.get('cm_txt',None)
        client.cm_file = request.FILES.get('cm_file',None)
        client.cm_target = request.POST.get('cm_target',None)
        client.am = request.POST.get('am',None)
        client.am_txt = request.POST.get('am_txt',None)
        client.am_file = request.FILES.get('am_file',None)
        client.am_target = request.POST.get('am_target',None)
        client.mm = request.POST.get('mm',None)
        client.mm_txt = request.POST.get('mm_txt',None)
        client.mm_file = request.FILES.get('mm_file',None)
        client.mm_target = request.POST.get('mm_target',None)
        client.vm = request.POST.get('vm',None)
        client.vm_txt = request.POST.get('vm_txt',None)
        client.vm_file = request.FILES.get('vm_file',None)
        client.vm_target = request.POST.get('vm_target',None)

        client.lc = request.POST.get('lc',None)
        client.lc_txt = request.POST.get('lc_txt',None)
        client.lc_file = request.FILES.get('lc_file',None)
        client.lc_target = request.POST.get('lc_target',None)

        client.user=usr
        client.save()
        
        client = client_information.objects.get(id=client.id)
        
        labels = request.POST.getlist('label[]')
        text =request.POST.getlist('dis[]')
        
        if len(labels)==len(text):
            mapped = zip(labels,text)
            mapped=list(mapped)
            for ele in mapped:
            
                created = addi_client_info.objects.get_or_create(labels=ele[0],discription=ele[1],user=usr,client=client,section='client_information')
        else:
            pass

        labels2 = request.POST.getlist('label2[]')
        text2 =request.POST.getlist('dis2[]')
        
        if len(labels2)==len(text2):
            mappeds = zip(labels2,text2)
            mappeds=list(mappeds)
            for ele in mappeds:
            
                created = addi_client_info.objects.get_or_create(labels=ele[0],discription=ele[1],user=usr,client=client,section='business_details')
        else: 
            pass
          
        
        files_req =request.FILES.getlist('file_add[]') 
        label_req =request.POST.getlist('label_req[]')
        dis_req =request.POST.getlist('dis_req[]') 
        target =request.POST.getlist('target[]')

        
        if len(files_req)==len(label_req)==len(dis_req)==len(target):
            mapped2 = zip(label_req,dis_req,files_req,target)
            mapped2=list(mapped2)
         
            for ele in mapped2:
                created = addi_client_info.objects.get_or_create(labels=ele[0],discription=ele[1],file=ele[2],target=ele[3],user=usr,client=client,section='requirments')

        msg_success = "Save Successfully"
        context={
            "usr":usr,
            "msg_success":msg_success,
        }
        return redirect("ad_dashboard") 
        
    return redirect("ad_create_work")


def ad_view_work(request):
    ids=request.session['userid']
    usr = user_registration.objects.get(id=ids)

    client=client_information.objects.filter(user=ids)

    context={
        "usr":usr,
        "client":client,
    }
    return render(request, 'admin/ad_view_work.html',context)

def ad_view_clint(request,id):
    client=client_information.objects.get(id=id)
    addicl=addi_client_info.objects.filter(client=client.id,section='client_information')
    addibs=addi_client_info.objects.filter(client=client.id,section='business_details')
    addirq=addi_client_info.objects.filter(client=client.id,section='requirments')
    
    ids=request.session['userid']
    usr = user_registration.objects.get(id=ids)
    context={
        "usr":usr,
        "client":client,
        "addicl":addicl,
        "addibs":addibs,
        "addirq":addirq,
    }
    return render(request, 'admin/ad_view_clint.html',context)



def update_client(request,id):
    client = client_information.objects.get(id=id)
    ids=request.session['userid']
    usr = user_registration.objects.get(id=ids)
    
    if request.session.has_key('userid'):
        userid = request.session['userid']
    else:
       return redirect('/')
    if request.method == 'POST':
        client.client_name = request.POST.get('client_name')
        
        client.client_address = request.POST.get('client_address')
        client.client_mail = request.POST.get('client_mail')
        client.bs_name = request.POST.get('bs_name')
        client.bs_website = request.POST.get('bs_website',None)
       
        client.bs_location = request.POST.get('bs_location')
        if request.FILES.get('client_files',None) == None:
            client.client_files=client.client_files
        else:
            client.client_files = request.FILES.get('client_files',None)
      
        client.seo = request.POST.get('seo',None)
        client.seo_txt = request.POST.get('seo_txt',None)
        if request.FILES.get('seo_file',None) == None:
            client.seo_file=client.seo_file
        else:
            client.seo_file = request.FILES.get('seo_file',None)

        client.on_pg = request.POST.get('onpage',None)
        client.on_pg_txt = request.POST.get('on_txt',None)
        client.on_pg_target = request.POST.get('on_target',None)
        if request.FILES.get('on_file',None) == None:
            client.on_pg_file=client.on_pg_file
        else:
            client.on_pg_file = request.FILES.get('on_file',None)


        client.off_pg = request.POST.get('offpage',None)
        client.off_pg_txt = request.POST.get('off_txt',None)
        client.off_pg_target = request.POST.get('off_target',None)
        if request.FILES.get('off_file',None) == None:
            client.off_pg_file=client.off_pg_file
        else:
            client.off_pg_file = request.FILES.get('off_file',None)

   


        client.smm = request.POST.get('smm',None)
        client.smm_txt = request.POST.get('smm_txt',None)
        client.smm_target = request.POST.get('smm_target',None)
     
        if request.FILES.get('smm_file',None) == None:
            client.smm_file=client.smm_file
        else:
            client.smm_file = request.FILES.get('smm_file',None)

        client.smo = request.POST.get('smo',None)
        client.smo_txt = request.POST.get('smo_txt',None)
        client.smo_target = request.POST.get('smo_target',None)
     
        if request.FILES.get('smo_file',None) == None:
            client.smo_file=client.smo_file
        else:
            client.smo_file = request.FILES.get('smo_file',None)

        client.sem = request.POST.get('sem',None)
        client.sem_txt = request.POST.get('sem_txt',None)
        client.sem_target = request.POST.get('sem_target',None)
    

        if request.FILES.get('sem_file',None) == None:
            client.sem_file=client.sem_file
        else:
            client.sem_file = request.FILES.get('sem_file',None)


        client.em = request.POST.get('em',None)
        client.em_txt = request.POST.get('em_txt',None)
        client.em_target = request.POST.get('em_target',None)
        if request.FILES.get('em_file',None) == None:
            client.em_file=client.em_file
        else:
            client.em_file = request.FILES.get('em_file',None)


        client.cm = request.POST.get('cm',None)
        client.cm_txt = request.POST.get('cm_txt',None)
        client.cm_target = request.POST.get('cm_target',None)

        if request.FILES.get('cm_file',None) == None:
            client.cm_file=client.cm_file
        else:
            client.cm_file = request.FILES.get('cm_file',None)


        client.am = request.POST.get('am',None)
        client.am_txt = request.POST.get('am_txt',None)
        client.am_target = request.POST.get('am_target',None)
        if request.FILES.get('am_file',None) == None:
            client.am_file=client.am_file
        else:
            client.am_file = request.FILES.get('am_file',None)


        client.mm = request.POST.get('mm',None)
        client.mm_txt = request.POST.get('mm_txt',None)
        client.mm_target = request.POST.get('mm_target',None)
        if request.FILES.get('mm_file',None) == None:
            client.mm_file=client.mm_file
        else:
            client.mm_file = request.FILES.get('mm_file',None)


        client.vm = request.POST.get('vm',None)
        client.vm_txt = request.POST.get('vm_txt',None)
        client.vm_target = request.POST.get('vm_target',None)
        if request.FILES.get('vm_file',None) == None:
            client.vm_file=client.vm_file
        else:
            client.vm_file = request.FILES.get('vm_file',None)

        client.lc = request.POST.get('lc',None)
        
        client.lc_txt = request.POST.get('lc_txt',None)
     
        client.lc_target = request.POST.get('lc_target',None)
        if request.FILES.get('lc_file',None) == None:
            client.lc_file=client.lc_file
        else:
            client.lc_file = request.FILES.get('lc_file',None)


        client.user=usr
        client.save()
        client = client_information.objects.get(id=id)
       

        
        client = client_information.objects.get(id=client.id)
        
        labels = request.POST.getlist('label[]')
        text =request.POST.getlist('dis[]')
        
        if len(labels)==len(text):
            mapped = zip(labels,text)
            mapped=list(mapped)
            count = addi_client_info.objects.filter(client=id,section='client_information').count()
            lb_count=len(labels)
            print(lb_count)
            for ele in mapped:
                
                    try:
                        adiclient = addi_client_info.objects.get(Q(client=client),Q(labels=ele[0])|Q(discription=ele[1]))
                        
                    
                        if ((adiclient.labels==ele[0]) or (adiclient.discription==ele[1])):
                            created = addi_client_info.objects.filter(Q(client=client),Q(labels=ele[0])|Q(discription=ele[1])).update(labels=ele[0],discription=ele[1])
                        
                        
                        elif ((adiclient.labels!=ele[0]) or (adiclient.discription!=ele[1])):
                            created = addi_client_info.objects.get_or_create(labels=ele[0],discription=ele[1],user=usr,client=client,section='client_information')
                    
                        else:
                            pass
                            
                    except:
                        created = addi_client_info.objects.get_or_create(labels=ele[0],discription=ele[1],user=usr,client=client,section='client_information')
                




        else:
            
            pass

        labels2 = request.POST.getlist('label2[]')
        text2 =request.POST.getlist('dis2[]')
        
        if len(labels2)==len(text2):
            mappeds = zip(labels2,text2)
            mappeds=list(mappeds)

      
            for ele in mappeds:
                try:
                    adiclient=addi_client_info.objects.get(Q(client=client),Q(labels=ele[0])|Q(discription=ele[1]))
                    if ((adiclient.labels==ele[0]) or (adiclient.discription==ele[1])):
                        created = addi_client_info.objects.filter(Q(client=client),Q(labels=ele[0])|Q(discription=ele[1])).update(labels=ele[0],discription=ele[1])
                    elif ((adiclient.labels!=ele[0]) or (adiclient.discription!=ele[1])):
                        created = addi_client_info.objects.get_or_create(labels=ele[0],discription=ele[1],client=client,user=usr,section='business_details')
                    else:
                        pass
                except:
                    created = addi_client_info.objects.get_or_create(labels=ele[0],discription=ele[1],client=client,user=usr,section='business_details')

        else: 
            pass
        
      
          

        
        label_req =request.POST.getlist('label_req[]')
        dis_req =request.POST.getlist('dis_req[]')
        target =request.POST.getlist('target[]')
       
        if request.FILES.getlist('file_add[]') == []:
            img=addi_client_info.objects.filter(client=id,section='Requirments')
            files_req=[]
            for i in img:
                files_req.append(i.file)
       
           
        elif len(request.FILES.getlist('file_add[]')) != len(label_req):
          
            img=addi_client_info.objects.filter(client=id,section='Requirments')
            fr=[]
            for i in img:
                fr.append(i.file)
            fr2 =request.FILES.getlist('file_add[]') 
            files_req=fr+fr2
           
        else:
           
            files_req=request.FILES.getlist('file_add[]')

        
        
        if len(label_req)==len(dis_req)==len(target)==len(files_req):
            
            mapped2 = zip(label_req,dis_req,files_req,target)
            mapped2=list(mapped2)
           
            
            abs=addi_client_info.objects.filter(client=id,section='Requirments').delete()
            for ele in mapped2:
                    

                    created = addi_client_info.objects.get_or_create(labels=ele[0],discription=ele[1],file=ele[2],target=ele[3],user=usr,client=client,section='Requirments')
                
        else:
       
            pass

        msg_success = "Save Successfully"
        return redirect('ad_view_clint',id)
    return redirect('ad_view_clint',id)




def ad_daily_work_det(request):
    ids=request.session['userid']
    usr = user_registration.objects.get(id=ids)
    dl_work=daily_work.objects.filter(date=date.today())

    dl_sub=daily_work_sub.objects.all() 
    dl_off=daily_off_sub.objects.all()
    dl_leeds=daily_leeds.objects.all()
    print(dl_sub)
    context={
        "usr":usr,
        "dl_work":dl_work,
        "dl_leeds":dl_leeds,
        "dl_off":dl_off,
        "dl_sub":dl_sub

    }
    return render(request, 'admin/ad_daily_work_det.html',context)


def ad_work_analiz_det(request):
    ids=request.session['userid']
    usr = user_registration.objects.get(id=ids)
    dl_sub=daily_work_sub.objects.all() 
    dl_off=daily_off_sub.objects.all()
    dl_leeds=daily_leeds.objects.all()

    dl_work=daily_work.objects.all()
    context={
        "usr":usr,
        "dl_work":dl_work,
        "dl_sub":dl_sub,
        "dl_off":dl_off,
        "dl_leeds":dl_leeds

    }
    return render(request, 'admin/ad_work_analiz_det.html',context)

def flt_dt_analiz(request):
    ids=request.session['userid']
    usr = user_registration.objects.get(id=ids)
    st_dt=request.POST.get('str_dt')
    en_dt=request.POST.get('end_dt')
    dl_sub=daily_work_sub.objects.all() 
    dl_off=daily_off_sub.objects.all()
    dl_leeds=daily_leeds.objects.all()

    dl_work=daily_work.objects.filter(date__gte=st_dt,date__lte=en_dt)
    context={
        "usr":usr,
        "dl_work":dl_work,
        "dl_sub":dl_sub,
        "dl_off":dl_off,
        "dl_leeds":dl_leeds

    }
    return render(request, 'admin/ad_work_analiz_det.html',context)


def ad_work_progress(request):
    ids=request.session['userid']
    usr = user_registration.objects.get(id=ids)
    pr_work=progress_report.objects.all()
    context={
        "usr":usr,
        "pr_work":pr_work

    }
    return render(request, 'admin/ad_work_progress.html',context)

def flt_progress(request):
    ids=request.session['userid']
    usr = user_registration.objects.get(id=ids)
    st_dt=request.POST.get('str_dt')
    en_dt=request.POST.get('end_dt')
    
    pr_work=progress_report.objects.filter(start_date__gte=st_dt,start_date__lte=en_dt)
    context={
        "usr":usr,
        "pr_work":pr_work

    }
    return render(request, 'admin/ad_work_progress.html',context)


def ad_work_progress_det(request,id):
    ids=request.session['userid']
    usr = user_registration.objects.get(id=ids)
    
 
    pr_work=progress_report.objects.get(id=id)
    try:
        prv_work=progress_report.objects.filter(work_id=pr_work.work_id).order_by('-end_date')[1]
    except:
        prv_work=None
    context={
        "usr":usr,
        "pr_work":pr_work,
        "prv_work":prv_work

    }
    return render(request, 'admin/ad_work_progress_det.html',context) 

# 

def ad_warning_ex(request):
    ids=request.session['userid']
    usr = user_registration.objects.get(id=ids)
    exe=user_registration.objects.filter(department="Digital Marketing Executive")
   
    context={
        "usr":usr,
        "exe":exe

    }
    return render(request, 'admin/ad_warning_ex.html',context)

def ad_warning_sugg_dash(request,id):
    ids=request.session['userid']
    usr = user_registration.objects.get(id=ids)
    ids=id
    context={
        "usr":usr,
        "ids":ids
        

    }
    return render(request, 'admin/ad_warning_sugg_dash.html',context)

def ad_warning_det(request,id):
    ids=request.session['userid']
    usr = user_registration.objects.get(id=ids)
    warn = Warning.objects.filter(executive=id,type="Warning")
    context={
        "usr":usr,
        "warn":warn

    }
    return render(request, 'admin/ad_warning_det.html',context) 

def ad_suggestions_det(request,id):
    ids=request.session['userid']
    usr = user_registration.objects.get(id=ids)
    warn = Warning.objects.filter(executive=id,type="Suggestion")
    context={
        "usr":usr,
        "warn":warn

    }
    return render(request, 'admin/ad_suggestions_det.html',context)


def change_pass(request):
    ids=request.session['userid']
    usr = user_registration.objects.get(id=ids)
    if request.session.has_key('userid'):
        devid = request.session['userid']
    else:
        return redirect('/')
    dev = user_registration.objects.filter(id=devid)

    if request.method == 'POST':
        abc = user_registration.objects.get(id=devid)
        cur = abc.password
        oldps = request.POST["currentPassword"]
        newps = request.POST["newPassword"]
        cmps = request.POST["confirmPassword"]
        if oldps == cur:
            if oldps != newps:
                if newps == cmps:
                    abc.password = request.POST.get('confirmPassword')
                    abc.save()
                    return render(request, 'admin/ch_pass.html', {'dev': dev,"usr":usr})
            elif oldps == newps:
                messages.add_message(request, messages.INFO, 'Current and New password same')
            else:
                messages.info(request, 'Incorrect password same')

            return render(request, 'admin/ch_pass.html', {'dev': dev,"usr":usr})
        else:
            messages.add_message(request, messages.INFO, 'old password wrong')
            return render(request, 'admin/ch_pass.html', {'dev': dev,"usr":usr})
    return render(request, 'admin/ch_pass.html', {'dev': dev,"usr":usr})

def ad_accountset(request):
    ids=request.session['userid']
    usr = user_registration.objects.get(id=ids)
    if request.session.has_key('userid'):
        devid = request.session['userid']
    else:
        return redirect('/')
    dev = user_registration.objects.filter(id=devid)
    return render(request, 'admin/ad_accountset.html', {'dev': dev,"usr":usr})

def ad_imagechange(request, id):
    ids=request.session['userid']
    usr = user_registration.objects.get(id=ids)
    if request.session.has_key('userid'):
        devid = request.session['userid']
    else:
        return redirect('/')
    dev = user_registration.objects.filter(id=devid)
    if request.method == 'POST':
        abc = user_registration.objects.get(id=id)
        abc.photo = request.FILES['filename']
        
        abc.save()
        return redirect('ad_accountset')
    return render(request, 'admin/ad_accountset.html',{'dev': dev,"usr":usr})


def get_dis(request):
    ele = request.GET.get('ele')
    warn = daily_work.objects.get(id=ele)
    
    rep =warn.workdone
 
    return JsonResponse({"status":" not","rep":rep})

def get_sub(request):
    ele = request.GET.get('ele')
    ids = request.GET.get('idss')
    try:
        warn = daily_work.objects.get(id=ids)
    except:
        pass
    if ele=="Facebook":
        hd=ele
        des=warn.fb_txt
        fl=warn.fb_file

    elif ele=="Twitter":
        hd=ele
        des=warn.tw_txt
        fl=warn.tw_file

    elif ele=="Pinterest":
        hd=ele
        des=warn.pin_txt
        fl=warn.pin_file

    elif ele=="Linkedin":
        hd=ele
        des=warn.link_txt
        fl=warn.link_file

    elif ele=="Instagram":
        hd=ele
        des=warn.insta_txt
        fl=warn.insta_file

    elif ele=="Tumblr":
        hd=ele
        des=warn.tumb_txt
        fl=warn.tumb_file

    elif ele=="Directories":
        hd=ele
        des=warn.diry_txt
        fl=warn.diry_file

    elif ele=="You Tube":
        hd=ele
        des=warn.yt_txt
        fl=warn.yt_file

    elif ele=="Quora":
        hd=ele
        des=warn.qra_txt
        fl=warn.qra_file

    elif ele=="PR Submission":
        hd=ele
        des=warn.pr_txt
        fl=warn.pr_file 

    elif ele=="Article Submission":
        hd=ele
        des=warn.art_txt
        fl=warn.art_file 

    elif ele=="Blog Posting":
        hd=ele
        des=warn.blg_txt
        fl=warn.blg_file 

    elif ele=="Classified Submission":
        hd=ele
        des=warn.clss_txt
        fl=warn.clss_file

    elif ele=="Guest Blogging":
        hd=ele
        des=warn.gst_txt
        fl=warn.gst_file

    elif ele=="Bokkmarking":
        hd=ele
        des=warn.bk_txt
        fl=warn.bk_file

    elif daily_off_sub.objects.filter(id=ids,sub=ele).exists():
       
        off = daily_off_sub.objects.get(id=ids,sub=ele)
        hd=off.sub
        des=off.sub_txt
        fl=off.sub_file

    elif daily_leeds.objects.filter(id=ids,sub=ele).exists():
       
        lc = daily_leeds.objects.get(id=ids,sub=ele)
        hd=lc.sub
        des=lc.sub_txt
        fl=lc.sub_file


    else:
        
        sm = daily_work_sub.objects.get(id=ids,sub=ele)
        hd=sm.sub
        des=sm.sub_txt
        fl=sm.sub_file
        

    return JsonResponse({"status":" not","hd":hd,"des":des,"fl":str(fl),})



def work_shedule_exe(request):
    ids=request.session['userid']
    usr = user_registration.objects.get(id=ids)
    exe=user_registration.objects.filter(department="Digital Marketing Executive")
   
    context={
        "usr":usr,
        "exe":exe

    }
    return render(request, 'admin/ad_exe_shedule.html',context)

def work_shedule(request,id):
    ids=request.session['userid']
    now = datetime.now()
    usr = user_registration.objects.get(id=ids)
    events = Events.objects.filter(executive=id, start__date=now.date())
    dl_sub=addi_events.objects.filter(executive=id)

    

    # # Define a start and end time range
    # start_time = time(0, 0, 0)
    # end_time = time(23, 59, 59)

    # # Define the date for which you want to find missing times
    # search_date = datetime(2023, 5, 4).date()

    # # Create a list of all times that should be in the database for the given date
    # expected_times = [datetime.combine(search_date, start_time) + timedelta(seconds=x) for x in range((datetime.combine(search_date, end_time) - datetime.combine(search_date, start_time)).seconds + 1)]

    # # Retrieve all date and time values from the database for the given date
    # actual_datetimes = Events.objects.filter(start__date=search_date).values_list('start', flat=True)

    # # Extract the time portion of the actual date and time values
    # actual_times = [dt.time() for dt in actual_datetimes]

    # # Find missing times
    # missing_times = set(expected_times) - set(actual_times)

    # # Print out the missing times
    # print(missing_times)

    # from datetime import datetime, timedelta, time
    # from django.db.models.functions import TruncHour
  
    # start_time = time(0, 0, 0)
    # end_time = time(9, 59, 59)

    # search_date = datetime(2023, 5, 4).date()


    # expected_hours = [datetime.combine(search_date, start_time) + timedelta(hours=x) for x in range((datetime.combine(search_date, end_time) - datetime.combine(search_date, start_time)).seconds // 3600 + 1)]

  
    # actual_hours = Events.objects.filter(start__date=search_date).annotate(hour=TruncHour('start')).values_list('start', flat=True)

    # # Find missing hours
    # missing_hours = set(expected_hours) - set(actual_hours)

    # # Print out the missing hours
    # print(missing_hours)


    # from datetime import datetime, timedelta, time
    # from django.db.models.functions import TruncHour


    # # Define a start and end date and time range
    # start_datetime = datetime(2023, 4, 5, 9, 0, 0)
    # end_datetime = datetime(2023, 4, 5, 18, 0, 0)

    # # Create a list of all hours that should be in the table for the given date range
    # expected_hours = []
    # current_datetime = start_datetime
    # while current_datetime <= end_datetime:
    #     expected_hours += [current_datetime]
    #     current_datetime += timedelta(hours=1)

    # # Retrieve all records from the database for the given date range and group them by hour
    # actual_hours = Events.objects.filter(start__gte=start_datetime, end__lte=end_datetime, id=1).annotate(hour=TruncHour('start')).values_list('hour', flat=True)
   
    # # Find missing hours
    # missing_hours = set(expected_hours) - set(actual_hours)

    # # Print out the missing hours
    # print(missing_hours)

    
    


    

    start_time = datetime.combine(now.date(), time.min)
    end_time = datetime.combine(now.date(), time.max)
    records = Events.objects.filter(start__date=now.date(), end__date=now.date(), start__lte=end_time, end__gte=start_time,executive=id)
    # records = Events.objects.filter(start__lte=start_time, end__gte=end_time)

    all_hours = [start_time + timedelta(hours=x) for x in range(9,18)]
    
    occupied_hours = set()
    for record in records:
        
        hours = [record.start+ timedelta(hours=x) for x in range((record.end - record.start).seconds // 3600 + 1)]
        occupied_hours.update(hours)
   
 

    free_hours = set(all_hours) - occupied_hours
    

    lst = []
    
    
    # for all_hr in sorted(all_hours):
    #   for oc_hr in sorted(occupied_hours):
    #         print( str(all_hr.time()) +"="+ str(oc_hr.time()))
    #         if all_hr.time() == oc_hr.time():
    #             pass
    #         else:
                
    #             print(all_hr.time())
    
    
 
    list1=[]
    for ls1 in sorted(occupied_hours):
        list1.append(ls1.time())

    list2=[]
    for ls2 in all_hours:
        list2.append(ls2.time())

    result_set = set(list1) - set(list2)

    result_list = list(result_set)
    
    def remove_dupilicate(List1,List2):
        return [item for item in List1 if item not in List2]

    new_a = remove_dupilicate(list1, list2)
    new_b = remove_dupilicate(list2, list1)

    k=list(sorted(new_b))
    
    context={
        "usr":usr,
        'events': events,
        "hr":k,
        "noti":len(k),
        "idr":id,
        "dl_sub":dl_sub
        

    }
    return render(request, 'admin/ad_work_shedule.html',context)

def filter_shedule(request,id):

    if request.method == 'POST':
        dates = request.POST['flt_date']
        
        ids=request.session['userid']
        usr = user_registration.objects.get(id=ids)
        events = Events.objects.filter(executive=id, start__date=dates)
        dl_sub=addi_events.objects.filter(executive=id)
     
        now = datetime.now()

        start_time = datetime.combine(now.date(), time.min)
        end_time = datetime.combine(now.date(), time.max)
        
        records = Events.objects.filter(start__date=dates, end__date=dates,executive=id)
     

        all_hours = [start_time + timedelta(hours=x) for x in range(9,18)]
        
        occupied_hours = set()
        for record in records:
            
            hours = [record.start+ timedelta(hours=x) for x in range((record.end - record.start).seconds // 3600 + 1)]
            occupied_hours.update(hours)
    
    

        free_hours = set(all_hours) - occupied_hours
        

        lst = []
        
    
        list1=[]
        for ls1 in sorted(occupied_hours):
            list1.append(ls1.time())

        list2=[]
        for ls2 in all_hours:
            list2.append(ls2.time())

        result_set = set(list1) - set(list2)

        result_list = list(result_set)
        
        def remove_dupilicate(List1,List2):
            return [item for item in List1 if item not in List2]

        new_a = remove_dupilicate(list1, list2)
        new_b = remove_dupilicate(list2, list1)

        k=list(sorted(new_b))
        
        context={
            "usr":usr,
            'events': events,
            "hr":k,
            "noti":len(k),
            "idr":id,
            "dl_sub":dl_sub

        }
        return render(request, 'admin/ad_work_shedule.html',context)
    return redirect("work_shedule",id)

# views.py


def events(request):
    events = Events.objects.all()
    data = []
    for event in events:
        data.append({
            'title': event.title,
            'start': event.start_time.isoformat(),
            'end': event.end_time.isoformat(),
        })
    return JsonResponse(data, safe=False)

def ad_exe_smopost(request):
    ids=request.session['userid']
    usr = user_registration.objects.get(id=ids)
    exe=user_registration.objects.filter(department="Digital Marketing Executive")
   
    context={
        "usr":usr,
        "exe":exe

    }
    return render(request, 'admin/ad_exe_smopost.html',context) 
    # 

def ad_sv_smopost(request,id):
    ids=request.session['userid']
    usr = user_registration.objects.get(id=ids)
    post = smo_post.objects.filter(executive=id)
    addi_post=addi_smo_post.objects.all()
    print(addi_post)
    context={
            "usr":usr,
            "post":post,
            "addi_post":addi_post,
        }
    return render(request, 'admin/ad_sv_smopost.html',context)

def ad_get_smo_pst(request):
    ele = request.GET.get('ele')
    ids = request.GET.get('idss')
    print("fdgfdgfdgdgfdgfdg")
    print(ids)
    try:
        warn = smo_post.objects.get(id=ids)
    except:
        pass
    if ele=="Facebook":
        print("haii")
        hd=ele
        des=warn.fb_dt
        print(des)
        fl=warn.fb_file

    elif ele=="Twitter":
        hd=ele
        des=warn.tw_dt
        fl=warn.tw_file

    elif ele=="Pinterest":
        hd=ele
        des=warn.pin_dt
        fl=warn.pin_file

    elif ele=="Linkedin":
        hd=ele
        des=warn.link_dt
        fl=warn.link_file

    elif ele=="Instagram":
        hd=ele
        des=warn.insta_dt
        fl=warn.insta_file

    elif ele=="Tumblr":
        hd=ele
        des=warn.tumb_dt
        fl=warn.tumb_file

    elif ele=="Directories":
        hd=ele
        des=warn.diry_dt
        fl=warn.diry_file

    elif ele=="You Tube":
        hd=ele
        des=warn.yt_dt
        fl=warn.yt_file

    elif ele=="Quora":
        hd=ele
        des=warn.qra_dt
        fl=warn.qra_file

    elif ele=="PR Submission":
        hd=ele
        des=warn.pr_dt
        fl=warn.pr_file 

    elif ele=="Article Submission":
        hd=ele
        des=warn.art_dt
        fl=warn.art_file 

    elif ele=="Blog Posting":
        hd=ele
        des=warn.blg_dt
        fl=warn.blg_file 

    elif ele=="Classified Submission":
        hd=ele
        des=warn.clss_dt
        fl=warn.clss_file

    elif ele=="Guest Blogging":
        hd=ele
        des=warn.gst_dt
        fl=warn.gst_file

    elif ele=="Bokkmarking":
        hd=ele
        des=warn.bk_dt
        fl=warn.bk_file

    elif daily_off_sub.objects.filter(id=ids,sub=ele).exists():
       
        off = daily_off_sub.objects.get(id=ids,sub=ele)
        hd=off.sub
        des=off.sub_dt
        fl=off.sub_file

    elif addi_smo_post.objects.filter(id=ids,label=ele).exists():
      
        add_smo = addi_smo_post.objects.get(id=ids,label=ele)
        hd=add_smo.label
        des=add_smo.date
        fl=add_smo.file
    else:
        
        sm = daily_work_sub.objects.get(id=ids,sub=ele)
        hd=sm.sub
        des=sm.sub_dt
        fl=sm.sub_file
        

    return JsonResponse({"status":" not","hd":hd,"des":des,"fl":str(fl),})

def get_event_det(request):
    ele = request.GET.get('ele')
    ids = request.GET.get('idss')
 
    try:
        warn = Events.objects.get(id=ids)
    except:
        warn = addi_events.objects.get(id=ids)
    if ele=="Facebook":
        print("haii")
        hd=ele
        des=warn.fb_dt
        print(des)
        fl=warn.fb_file

    elif ele=="Twitter":
        hd=ele
        des=warn.tw_dt
        fl=warn.tw_file

    elif ele=="Pinterest":
        hd=ele
        des=warn.pin_dt
        fl=warn.pin_file

    elif ele=="Linkedin":
        hd=ele
        des=warn.link_dt
        fl=warn.link_file

    elif ele=="Instagram":
        hd=ele
        des=warn.insta_dt
        fl=warn.insta_file

    elif ele=="Tumblr":
        hd=ele
        des=warn.tumb_dt
        fl=warn.tumb_file

    elif ele=="Directories":
        hd=ele
        des=warn.diry_dt
        fl=warn.diry_file

    elif ele=="You Tube":
        hd=ele
        des=warn.yt_dt
        fl=warn.yt_file

    elif ele=="Quora":
        hd=ele
        des=warn.qra_dt
        fl=warn.qra_file

    elif ele=="PR Submission":
        hd=ele
        des=warn.pr_dt
        fl=warn.pr_file 

    elif ele=="Article Submission":
        hd=ele
        des=warn.art_dt
        fl=warn.art_file 

    elif ele=="Blog Posting":
        hd=ele
        des=warn.blg_dt
        fl=warn.blg_file 

    elif ele=="Classified Submission":
        hd=ele
        des=warn.clss_dt
        fl=warn.clss_file

    elif ele=="Guest Blogging":
        hd=ele
        des=warn.gst_dt
        fl=warn.gst_file

    elif ele=="Bokkmarking":
        hd=ele
        des=warn.bk_dt
        fl=warn.bk_file

    elif addi_events.objects.filter(id=ids,label=ele).exists():
       
        off = addi_events.objects.get(id=ids,label=ele)
        hd=off.label
        des=off.date
        fl=off.file
    else:
        
        sm = daily_work_sub.objects.get(id=ids,sub=ele)
        hd=sm.sub
        des=sm.sub_dt
        fl=sm.sub_file
        

    return JsonResponse({"status":" not","hd":hd,"des":des,"fl":str(fl),})


def ad_export_excel(request,id):

    filtered_data = daily_leeds.objects.filter(daily=id)

    # Create an Excel workbook and get the active sheet
    workbook = Workbook()
    sheet = workbook.active

    # Add column headers to the Excel sheet
    headers = ['No.', 'Date', 'Label', 'Text']  # Replace with your actual column names
    sheet.append(headers)

    # Add data rows to the Excel sheet
    count = 1
    for item in filtered_data:
       
        row = [count,item.daily.date,item.sub, item.sub_txt]  # Replace with your actual column names
        sheet.append(row)
        count+=1

    # Set the response headers for the Excel file
    response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    response['Content-Disposition'] = 'attachment; filename=filtered_data.xlsx'

    # Save the Excel workbook to the response
    workbook.save(response)

    return response

# -----------------------------------------------------------------------------Executive Section

def ex_base(request):
    ids=request.session['userid']
    usr = user_registration.objects.get(id=ids)
    context={
        "usr":usr,
    }
    return render(request, 'executive/ex_base.html',context)

def ex_profile(request):
    ids=request.session['userid']
    usr = user_registration.objects.get(id=ids)
    context={
        "usr":usr,
    }
    return render(request, 'executive/ex_profile.html',context)

def ex_dashboard(request):
    ids=request.session['userid']
    usr = user_registration.objects.get(id=ids)
    cor=correction.objects.filter(executive=ids).order_by('id').last()
    
    dt=date.today()
    context={
        "usr":usr,
        "cor":cor,
        "dt":dt
    }
    return render(request, 'executive/ex_dashboard.html',context)

def ex_daily_work_clint(request):
    ids=request.session['userid']
    usr = user_registration.objects.get(id=ids)
    work_as=work_asign.objects.filter(exe_name=ids).values('client_name_id').distinct()
    last=work_asign.objects.filter(exe_name=ids).last()
    work=Work.objects.all()
    cl=client_information.objects.all()

   
    context={
        "usr":usr,
        "work_as":work_as,
        "work":work,
        "cl":cl,
        "last":last
    }
    return render(request, 'executive/ex_daily_work_clint.html',context)

def ex_daily_work_det(request,id):
    ids=request.session['userid']
    usr = user_registration.objects.get(id=ids)
    work_as=work_asign.objects.filter(exe_name=ids)
    works=Work.objects.filter(client_name_id=id).order_by("-id")
    daily=daily_work.objects.filter(user=ids)
    dl_sub=daily_work_sub.objects.all() 
    dl_off=daily_off_sub.objects.all()

    dl_leeds=daily_leeds.objects.all()
    cr_date=date.today()
    
    context={
        "usr":usr,
        "cr_date":cr_date,
        "daily":daily,
        "work_as":work_as,
        "works":works,
        "dl_sub":dl_sub,
        "dl_off":dl_off,
        "dl_leeds":dl_leeds
        
    }
    return render(request, 'executive/ex_daily_work_det.html',context)

def daily_work_done(request,id):
    ids=request.session['userid']
    usr = user_registration.objects.get(id=ids)

    work=Work.objects.get(id=id)
    if request.method == 'POST':
        daily = daily_work()
        daily.task=work.task
        daily.date=date.today()
        daily.workdone =request.POST.get('workdone',None)

        daily.fb = request.POST.get('fb',None)
        daily.fb_txt = request.POST.get('fb_txt',None)
        daily.fb_file = request.FILES.get('fb_file',None)
        daily.tw = request.POST.get('tw',None)
        daily.tw_txt = request.POST.get('tw_txt',None)
        daily.tw_file = request.FILES.get('tw_file',None)
        daily.pin = request.POST.get('pin',None)
        daily.pin_txt = request.POST.get('pin_txt',None)
        daily.pin_file = request.FILES.get('pin_file',None)
        daily.link = request.POST.get('link',None)
        daily.link_txt = request.POST.get('link_txt',None)
        daily.link_file = request.FILES.get('link_file',None)
        daily.insta = request.POST.get('insta',None)
        daily.insta_txt = request.POST.get('insta_txt',None)
        daily.insta_file = request.FILES.get('insta_file',None)
        daily.tumb = request.POST.get('tumb',None)
        daily.tumb_txt = request.POST.get('tumb_txt',None)
        daily.tumb_file = request.FILES.get('tumb_file',None)
        daily.diry = request.POST.get('diry',None)
        daily.diry_txt = request.POST.get('diry_txt',None)
        daily.diry_file = request.FILES.get('diry_file',None)
        daily.yt = request.POST.get('yt',None)
        daily.yt_txt = request.POST.get('yt_txt',None)
        daily.yt_file = request.FILES.get('yt_file',None)
        daily.qra = request.POST.get('qra',None)
        daily.qra_txt = request.POST.get('qra_txt',None)
        daily.qra_file = request.FILES.get('qra_file',None)
        daily.sbms = request.POST.get('sbms',None)
        daily.sbms_txt = request.POST.get('sbms_txt',None)
        daily.sbms_file = request.FILES.get('sbms_file',None)

        daily.pr = request.POST.get('pr',None)
        daily.pr_txt = request.POST.get('pr_txt',None)
        daily.pr_file = request.FILES.get('pr_file',None)
        daily.art = request.POST.get('art',None)
        daily.art_txt = request.POST.get('art_txt',None)
        daily.art_file = request.FILES.get('art_file',None)
        daily.blg = request.POST.get('blg',None)
        daily.blg_txt = request.POST.get('blg_txt',None)
        daily.blg_file = request.FILES.get('blg_file',None)
        daily.clss = request.POST.get('cls',None)
        daily.clss_txt = request.POST.get('cls_txt',None)
        daily.clss_file = request.FILES.get('cls_file',None)
        daily.gst = request.POST.get('gst',None)
        daily.gst_txt = request.POST.get('gst_txt',None)
        daily.gst_file = request.FILES.get('gst_file',None)
        daily.bk = request.POST.get('bk',None)
        daily.bk_txt = request.POST.get('bk_txt',None)
        daily.bk_file = request.FILES.get('bk_file',None)
        
        dct_file = dict(request.FILES)
        lst_screenshot = dct_file['filed']
        lst_file = []
        for ins_screenshot in lst_screenshot:
            str_img_path = ""
            if ins_screenshot:
                img_emp = ins_screenshot
                fs = FileSystemStorage(location=settings.MEDIA_ROOT,base_url=settings.MEDIA_URL)
                str_img = fs.save(''.join(filter(str.isalnum, str(img_emp))), img_emp)
                str_img_path = fs.url(''.join(filter(str.isalnum, str_img)))
                lst_file.append('/media/'+''.join(filter(str.isalnum, str(img_emp))))
                daily.json_testerscreenshot = lst_file
        daily.work=work
        daily.user=usr
        daily.cl_name=work.cl_name
        daily.save() 
        dl = daily_work.objects.get(id=daily.id)
        
        sub_lb =request.POST.getlist('sub_lb[]') 
        sub_txt =request.POST.getlist('sub_txt[]')
        sub_file =request.FILES.getlist('sub_file[]')
        
        if len(sub_lb)==len(sub_txt)==len(sub_file):
            mapped2 = zip(sub_lb,sub_txt,sub_file)
            mapped2=list(mapped2)
            for ele in mapped2:
               
                created = daily_work_sub.objects.get_or_create(sub=ele[0],sub_txt=ele[1],sub_file=ele[2],daily=dl)
                    
        off_sub_lb =request.POST.getlist('off_sub_lb[]') 
        off_sub_txt =request.POST.getlist('off_sub_txt[]')
        off_sub_file =request.FILES.getlist('off_sub_file[]')
        
        if len(off_sub_lb)==len(off_sub_txt)==len(off_sub_file):
            mapped2 = zip(off_sub_lb,off_sub_txt,off_sub_file)
            mapped2=list(mapped2)
            for ele in mapped2:
               
                created = daily_off_sub.objects.get_or_create(sub=ele[0],sub_txt=ele[1],sub_file=ele[2],daily=dl)

        lc_lb =request.POST.getlist('lc_lb[]') 
        lc_txt =request.POST.getlist('lc_txt[]')
        lc_file =request.FILES.getlist('lc_file[]')
        
        if len(lc_lb)==len(lc_txt)==len(lc_file):
            mapped2 = zip(lc_lb,lc_txt,lc_file)
            mapped2=list(mapped2)
            for ele in mapped2:
               
                created = daily_leeds.objects.get_or_create(sub=ele[0],sub_txt=ele[1],sub_file=ele[2],daily=dl)

        return redirect("ex_daily_work_det",work.client_name_id)
    return redirect("ex_daily_work_det",work.client_name_id)

def ex_weekly_rep_clint(request):
    ids=request.session['userid']
    usr = user_registration.objects.get(id=ids)
    work_as=work_asign.objects.filter(exe_name=ids).values('client_name_id').distinct()
    work=Work.objects.filter()
    last=work_asign.objects.filter(exe_name=ids).last()
    cl=client_information.objects.all()
    context={
        "usr":usr,
        "work_as":work_as,
        "work":work,
        "cl":cl,
        "last":last
    }
    return render(request, 'executive/ex_weekly_rep_clint.html',context)

def ex_weekly_rep_clint_det(request,id):
    ids=request.session['userid']
    usr = user_registration.objects.get(id=ids)
    work_as=work_asign.objects.filter(exe_name=ids)
   
    work_tb=Work.objects.filter(client_name_id=id).order_by("-id")
    rep=progress_report.objects.filter(user=usr)
    context={
        "usr":usr,
        "work_as":work_as,
      
        "rep":rep,
        "work_tb":work_tb
    }
    return render(request, 'executive/ex_weekly_rep_det.html',context)

def sv_wk_rp(request,id):
    ids=request.session['userid']
    usr = user_registration.objects.get(id=ids)
    
    work=Work.objects.get(id=id)
    if request.method == 'POST':
        pro = progress_report()
        pro.task=work.task
        pro.audit_rprt=request.FILES.get('repr_fl',None)
        pro.graph=request.FILES.get('gr_fl',None)
        pro.start_date=request.POST.get('st_dt',None)
        pro.end_date=request.POST.get('ed_dt',None)
        pro.work=work
        pro.user=usr
        pro.cl_name=work.cl_name
        pro.save()
        return redirect("ex_weekly_rep_clint_det",work.client_name_id)
    return redirect("ex_weekly_rep_clint_det",work.client_name_id)

def ex_view_work_clint(request):
    ids=request.session['userid']
    usr = user_registration.objects.get(id=ids)
    
    work_as=work_asign.objects.filter(exe_name=ids)
    work=Work.objects.all()
    cl=client_information.objects.all()
    last=work_asign.objects.filter(exe_name=ids).last()

    context={
        "usr":usr,
        "work":work,
        "work_as":work_as,
        "cl":cl,
        "last":last,
    }
    return render(request, 'executive/ex_view_work_clint.html',context)

def ex_view_clint_det(request,id):
    ids=request.session['userid']
    usr = user_registration.objects.get(id=ids)
    
    work=Work.objects.get(id=id)
    context={
        "usr":usr, 
        "client":work
    }
    return render(request, 'executive/ex_view_clint_det.html',context)

def ex_warnings_dash(request):
    ids=request.session['userid']
    usr = user_registration.objects.get(id=ids)
    context={
        "usr":usr
    }
    return render(request, 'executive/ex_warnings_dash.html',context) 


def ex_warning(request):
    ids=request.session['userid']
    usr = user_registration.objects.get(id=ids)

    warn=Warning.objects.filter(executive=ids,type="Warning")
    context={
        "usr":usr,
        "warn":warn
    }
    return render(request, 'executive/ex_warning.html',context)

def add_warning(request, id):
   

    if request.method == 'POST':
        warn = Warning.objects.get(id=id)
        warn.reply=request.POST.get('workdone',None)
        warn.save()
        return redirect("ex_warning")
    return redirect("ex_warning")
    
def ex_suggestions(request):
    ids=request.session['userid']
    usr = user_registration.objects.get(id=ids)
    warn=Warning.objects.filter(executive=ids,type="Suggestion")
    context={
        "usr":usr,
        "warn":warn
    }
    return render(request, 'executive/ex_suggestions.html',context)

def add_suggestion(request, id):
   

    if request.method == 'POST':
        warn = Warning.objects.get(id=id)
        warn.reply=request.POST.get('workdone',None)
        warn.save()
        return redirect("ex_warning")
    return redirect("ex_warning")


def corrections(request):
    ids=request.session['userid']
    usr = user_registration.objects.get(id=ids)
    cor=correction.objects.filter(executive=ids)
    dl_work=daily_work.objects.filter(user=ids)
    dl_sub=daily_work_sub.objects.all() 
    dl_off=daily_off_sub.objects.all()
    dl_leeds=daily_leeds.objects.all()
    print(dl_leeds)
    context={
        "usr":usr,
        "warn":cor,
        "dl_work":dl_work,
        "dl_sub":dl_sub,
        "dl_off":dl_off,
        "dl_leeds":dl_leeds,

    }
    return render(request, 'executive/correction.html',context)

def add_corrections(request, id):
   

    if request.method == 'POST':
        warn = correction.objects.get(id=id)
        warn.reply=request.POST.get('workdone',None)
        warn.save()
        return redirect("corrections")
    return redirect("corrections")

def get_corrections(request):
    ele = request.GET.get('ele')
    warn = correction.objects.get(id=ele)
    warns =warn.description
    rep =warn.reply
 
    return JsonResponse({"status":" not","warns":warns,"rep":rep})

    
def get_warns(request):
    ele = request.GET.get('ele')
    warn = Warning.objects.get(id=ele)
    warns =warn.description
    rep =warn.reply
 
    return JsonResponse({"status":" not","warns":warns,"rep":rep})

    
def get_requ(request):
    ele = request.GET.get('ele')
    warn = addi_client_info.objects.get(id=ele)
    warns =warn.discription
    rep =warn.file
    nm =warn.labels
    target =warn.target
   
    vk=str(rep)
    
    return JsonResponse({"status":" not","warns":warns,"rep":vk,"nm":nm,"target":target})


def logout(request):
    if 'userid' in request.session:  
        request.session.flush()
        return redirect('/')
    else:
        return redirect('/') 


def ex_change_pass(request):
    ids=request.session['userid']
    usr = user_registration.objects.get(id=ids)
    if request.session.has_key('userid'):
        devid = request.session['userid']
    else:
        return redirect('/')

    dev = user_registration.objects.filter(id=devid)

    if request.method == 'POST':
        abc = user_registration.objects.get(id=devid)
        cur = abc.password
        oldps = request.POST["currentPassword"]
        newps = request.POST["newPassword"]
        cmps = request.POST["confirmPassword"]
        if oldps == cur:
            if oldps != newps:
                if newps == cmps:
                    abc.password = request.POST.get('confirmPassword')
                    abc.save()
                    return render(request, 'executive/ex_ch_pass.html', {'dev': dev,"usr":usr})
            elif oldps == newps:
                messages.add_message(request, messages.INFO, 'Current and New password same')
            else:
                messages.info(request, 'Incorrect password same')

            return render(request, 'executive/ex_ch_pass.html', {'dev': dev,"usr":usr})
        else:
            messages.add_message(request, messages.INFO, 'old password wrong')
            return render(request, 'executive/ex_ch_pass.html', {'dev': dev,"usr":usr})
    return render(request, 'executive/ex_ch_pass.html', {'dev': dev,"usr":usr})

def ex_accountset(request):
    ids=request.session['userid']
    usr = user_registration.objects.get(id=ids)
    if request.session.has_key('userid'):
        devid = request.session['userid']
    else:
        return redirect('/')
    dev = user_registration.objects.filter(id=devid)
    return render(request, 'executive/ex_accountset.html', {'dev': dev,"usr":usr})

def ex_imagechange(request, id):
    ids=request.session['userid']
    usr = user_registration.objects.get(id=ids)
    if request.session.has_key('userid'):
        devid = request.session['userid']
    else:
        return redirect('/')
    dev = user_registration.objects.filter(id=devid)
    if request.method == 'POST':
        abc = user_registration.objects.get(id=id)
        abc.photo = request.FILES['filename']
        
        abc.save()
        return redirect('ex_accountset')
    return render(request, 'executive/ex_accountset.html',{'dev': dev,"usr":usr})


def ex_schedule_dash(request):
    ids=request.session['userid']
    usr = user_registration.objects.get(id=ids)
    context={
        "usr":usr,
    
    }
    return render(request, 'executive/ex_schedule_dash.html',context)

def ex_calander(request):
    ids=request.session['userid']
    usr = user_registration.objects.get(id=ids)
    context={
        "usr":usr,
    
    }
    return render(request, 'executive/ex_calander.html',context)


def ex_all_events(request):
    all_events = Events.objects.all()
    out=[]
    for event in all_events:
        out.append({
            "title":event.name,
            "id":event.id,
            "start":event.start.strftime("%m/%d/%Y, %H:%M:%S"), 
        })
    return JsonResponse(out, safe=False)
 
 
def ex_add_event(request):
    ids=request.session['userid']
    usr = user_registration.objects.get(id=ids)
    if request.method == 'POST':
        start = request.POST.get('start', None)
        end = request.POST.get("end", None)
        title = request.POST.get('title', None)
        img = request.FILES.get('file', None)

        b = Events()
        b.name=title
        b.start=start 
        b.end=end 
        b.img=img
        b.executive=usr
        b.status="pending"
        b.save()
        data = {}
        return JsonResponse(data)
 
def ex_update(request):
    start = request.GET.get("start", None)
    end = request.GET.get("end", None)
    title = request.GET.get("title", None)
    id = request.GET.get("id", None)
    event = Events.objects.get(id=id)
    event.start = start
    event.end = end
    event.name = title
    event.save()
    data = {}
    return JsonResponse(data)
 
def ex_remove(request):
    id = request.GET.get("id", None)
    event = Events.objects.get(id=id)
    event.delete()
    data = {}
    return JsonResponse(data)

def ex_shedule_work(request):
    ids=request.session['userid']
    usr = user_registration.objects.get(id=ids)
    events = Events.objects.filter(executive=usr)
    dl_sub = addi_events.objects.filter(executive=usr)

    
    context={
        "usr":usr,
        'events': events,
        "dl_sub":dl_sub

    }
    return render(request, 'executive/ex_schedule_work.html',context)


def ex_edit_post_status(request,id):
    if request.method == 'POST':
        ids=request.session['userid']
        usr = user_registration.objects.get(id=ids)
        b=Events.objects.get(id=id)
        b.status=request.POST['status']
        b.st_file=request.FILES.get('cmpl_file',None)
        b.fb = request.POST.get('fb',None)
        b.fb_dt = request.POST.get('fb_txt',None)
        b.fb_file = request.FILES.get('fb_file',None)
        b.tw = request.POST.get('tw',None)
        b.tw_dt = request.POST.get('tw_txt',None)
        b.tw_file = request.FILES.get('tw_file',None)
        b.pin = request.POST.get('pin',None)
        b.pin_dt = request.POST.get('pin_txt',None)
        b.pin_file = request.FILES.get('pin_file',None)
        b.link = request.POST.get('link',None)
        b.link_dt = request.POST.get('link_txt',None)
        b.link_file = request.FILES.get('link_file',None)
        b.insta = request.POST.get('insta',None)
        b.insta_dt = request.POST.get('insta_txt',None)
        b.insta_file = request.FILES.get('insta_file',None)
        b.tumb = request.POST.get('tumb',None)
        b.tumb_dt = request.POST.get('tumb_txt',None)
        b.tumb_file = request.FILES.get('tumb_file',None)
        b.diry = request.POST.get('diry',None)
        b.diry_dt = request.POST.get('diry_txt',None)
        b.diry_file = request.FILES.get('diry_file',None)
        b.yt = request.POST.get('yt',None)
        b.yt_dt = request.POST.get('yt_txt',None)
        b.yt_file = request.FILES.get('yt_file',None)
        b.qra = request.POST.get('qra',None)
        b.qra_dt = request.POST.get('qra_txt',None)
        b.qra_file = request.FILES.get('qra_file',None)
        b.sbms = request.POST.get('sbms',None)
        b.sbms_dt = request.POST.get('sbms_txt',None)
        b.sbms_file = request.FILES.get('sbms_file',None)
        
        b.save()

        
        label_req =request.POST.getlist('sub_lb[]')
        dt =request.POST.getlist('dates[]') 
        files_req =request.FILES.getlist('sub_file[]') 
      

        
        if len(files_req)==len(label_req)==len(dt):
            mapped2 = zip(label_req,dt,files_req)
            mapped2=list(mapped2)
         
            for ele in mapped2:
                created = addi_events.objects.get_or_create(label=ele[0],date=ele[1],file=ele[2],executive=usr,events=b)
                
      
        b.save()
        return redirect('ex_shedule_work')

    return redirect('ex_shedule_work')
    
def ex_save_shedule(request):
    idr=request.session['userid']
    usr_lg = user_registration.objects.get(id=idr)

    if request.method == 'POST':

        ids=request.session['smo_userid']
        usr = smo_registration.objects.get(id=ids)
        b=smo_post()
        b.description = request.POST['description']
        b.status="pending"
        dct_file = dict(request.FILES)
        lst_screenshot = dct_file['filed']
        lst_file = []
        for ins_screenshot in lst_screenshot:
            str_img_path = ""
            if ins_screenshot:
                img_emp = ins_screenshot
                fs = FileSystemStorage(location=settings.MEDIA_ROOT,base_url=settings.MEDIA_URL)
                str_img = fs.save(''.join(filter(str.isalnum, str(img_emp))), img_emp)
                str_img_path = fs.url(''.join(filter(str.isalnum, str_img)))
                lst_file.append('/media/'+''.join(filter(str.isalnum, str(img_emp))))
                b.json_testerscreenshot = lst_file

        
        b.json_testerscreenshot=b.json_testerscreenshot
        b.smo=usr
        b.executive=usr_lg

 
        b.fb = request.POST.get('fb',None)
        b.fb_dt = request.POST.get('fb_txt',None)
        b.fb_file = request.FILES.get('fb_file',None)
        b.tw = request.POST.get('tw',None)
        b.tw_dt = request.POST.get('tw_txt',None)
        b.tw_file = request.FILES.get('tw_file',None)
        b.pin = request.POST.get('pin',None)
        b.pin_dt = request.POST.get('pin_txt',None)
        b.pin_file = request.FILES.get('pin_file',None)
        b.link = request.POST.get('link',None)
        b.link_dt = request.POST.get('link_txt',None)
        b.link_file = request.FILES.get('link_file',None)
        b.insta = request.POST.get('insta',None)
        b.insta_dt = request.POST.get('insta_txt',None)
        b.insta_file = request.FILES.get('insta_file',None)
        b.tumb = request.POST.get('tumb',None)
        b.tumb_dt = request.POST.get('tumb_txt',None)
        b.tumb_file = request.FILES.get('tumb_file',None)
        b.diry = request.POST.get('diry',None)
        b.diry_dt = request.POST.get('diry_txt',None)
        b.diry_file = request.FILES.get('diry_file',None)
        b.yt = request.POST.get('yt',None)
        b.yt_dt = request.POST.get('yt_txt',None)
        b.yt_file = request.FILES.get('yt_file',None)
        b.qra = request.POST.get('qra',None)
        b.qra_dt = request.POST.get('qra_txt',None)
        b.qra_file = request.FILES.get('qra_file',None)
        b.sbms = request.POST.get('sbms',None)
        b.sbms_dt = request.POST.get('sbms_txt',None)
        b.sbms_file = request.FILES.get('sbms_file',None)
        
        b.save()

        
        label_req =request.POST.getlist('sub_lb[]')
        dt =request.POST.getlist('dates[]') 
        files_req =request.FILES.getlist('sub_file[]') 
      

        
        if len(files_req)==len(label_req)==len(dt):
            mapped2 = zip(label_req,dt,files_req)
            mapped2=list(mapped2)
         
            for ele in mapped2:
                created = addi_smo_post.objects.get_or_create(label=ele[0],date=ele[1],file=ele[2],executive=usr_lg,smo=usr,post=b)
        return redirect('ex_calander')
    return redirect('ex_calander')
#---------------------------------marketing section

    

def he_profile(request):
    ids=request.session['userid']
    usr = user_registration.objects.get(id=ids)
    return render(request, 'head/he_profile.html',{"usr":usr})

def he_project(request):
    ids=request.session['userid']
    usr = user_registration.objects.get(id=ids)
    return render(request,'head/he_project.html',{"usr":usr})

def he_view_works(request):
    ids=request.session['userid']
    usr = user_registration.objects.get(id=ids)
    client=client_information.objects.all()
    return render(request,'head/he_view_works.html',{'client':client,"usr":usr,})

def he_work_asign(request,pk):
    ids=request.session['userid']
    usr = user_registration.objects.get(id=ids)
    client=client_information.objects.get(id=pk)
    exe=user_registration.objects.filter(department='Digital Marketing Executive')
    return render(request,'head/he_work_asign.html',{'client':client,'exe':exe,"usr":usr,})

def he_view_work_asign_client(request):
    ids=request.session['userid']
    usr = user_registration.objects.get(id=ids)
    client=client_information.objects.all()
    return render(request,'head/he_view_work_asign_client.html',{'client':client,"usr":usr,})

def he_view_work_asign_exe(request,id):
    ids=request.session['userid']
    usr = user_registration.objects.get(id=ids)
    client=client_information.objects.get(id=id)
    work=work_asign.objects.filter(client_name=client.id)
    return render(request,'head/he_view_work_asign_exe.html',{"usr":usr,"w":work})


def he_daily_task(request):
    ids=request.session['userid']
    usr = user_registration.objects.get(id=ids)
    today=date.today()
    work=daily_work.objects.filter(date=today)
    sub_work=daily_work_sub.objects.all()
    dl_sub=daily_work_sub.objects.all() 
    dl_off=daily_off_sub.objects.all()

    dl_leeds=daily_leeds.objects.all()
    return render(request,'head/he_daily_task.html',{'work':work,"usr":usr,"sub":sub_work,"dl_sub":dl_sub,"dl_off":dl_off,"dl_leeds":dl_leeds})


def he_workprogress_executive(request):
    ids=request.session['userid']
    usr = user_registration.objects.get(id=ids)
    prgs=progress_report.objects.all()
    return render(request,'head/he_workprogress_executive.html',{'prgs':prgs,"usr":usr,})

def he_progress_report(request,pk):
    ids=request.session['userid']
    usr = user_registration.objects.get(id=ids)
    work=progress_report.objects.get(id=pk)
    try:
        prv_work=progress_report.objects.filter(work_id=work.id).order_by('-end_date')[0]
    except:
        prv_work=None
    return render(request,'head/he_progress_report.html',{'work':work,"usr":usr,"prv_work":prv_work})


def he_feedback(request):
    ids=request.session['userid']
    usr = user_registration.objects.get(id=ids)
    exe=user_registration.objects.filter(department="Digital Marketing Executive")
    return render(request,'head/he_feedback.html',{'exe':exe,"usr":usr,})


def he_feedbacke1(request,pk):
    ids=request.session['userid']
    usr = user_registration.objects.get(id=ids)
    exe=user_registration.objects.get(id=pk)
    wrng=Warning.objects.filter(executive_id=exe.id)
    return render(request,'head/he_feedback1.html',{'exe':exe,'wrng':wrng,"usr":usr,})

    
def he_feedback_submit(request,pk):
    ids=request.session['userid']
    usr = user_registration.objects.get(id=ids)
    if request.method=='POST':
        des=request.POST['des']
        typ=request.POST['option']
        warning=Warning(executive_id=pk,description=des,type=typ,)
        warning.save()
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    
def he_work_add(request,id):
    ids=request.session['userid']
    usr = user_registration.objects.get(id=ids)
    if request.method == 'POST':
        task = request.POST.get('task')
        des = request.POST.get('des')
        sdate=request.POST.get('sdate')
        edate=request.POST.get('edate')
        file=request.FILES.get('file')
        sub_tsk = request.POST.get('sub_tsk')
        target=request.POST.get('trgt')
        client=client_information.objects.get(id=id)
        json_data = request.POST.get('array', '')
        array = json.loads(json_data)
        w=Work(task=task,description=des,start_date=sdate,end_date=edate,file_attached=file,cl_name=client.bs_name,client_name=client)
        w.save()

        if w.task=="SEO":
            w.file_2=client.seo_file
            w.save()
            if sub_tsk=="On page":
                w.sub_task="On page"
                w.sub_des=client.on_pg_txt
                w.sub_file=client.on_pg_file
                w.target=request.POST.get('ontrgt')
                w.save()
            if sub_tsk=="Off page":
                w.sub_task="Off page"
                w.sub_des=client.off_pg_txt
                w.sub_file=client.off_pg_file
                w.target=request.POST.get('offtrgt')
                w.save()

        if w.task=="SMM":
            w.file_2=client.smm_file
            w.target=target
            w.save()
        if w.task=="SEM/PPC":
            w.file_2=client.sem_file
            w.target=target
            w.save()
        if w.task=="Email Marketing":
            w.file_2=client.em_file
            w.target=target
            w.save()   
        if w.task=="Content Marketing":
            w.file_2=client.cm_file
            w.target=target
            w.save() 
        if w.task=="Affiliate Marketing":
            w.file_2=client.am_file
            w.target=target
            w.save()   
        if w.task=="Mobile marketing":
            w.file_2=client.mm_file
            w.target=target
            w.save()  
        if w.task=="Video Marketing":
            w.file_2=client.vm_file
            w.target=target
            w.save() 
        if w.task=="SMO":
            w.file_2=client.smo_file
            w.target=target
            w.save() 
        if w.task=="Leads Collection":
            w.file_2=client.lc_file
            w.target=target
            w.save()            
        w=Work.objects.latest('id')
        for i in array:
            b=user_registration.objects.get(department="Digital Marketing Executive",fullname=i)
            c=work_asign(work_id=w.id,exe_name_id=b.id,client_name_id=client.id)
            c.save()
        return HttpResponse({"message": "success"})


def he_add_correction_daily(request,id):
    if request.method=='POST':
        cor=request.POST.get('cor')
        daily=daily_work.objects.get(id=id)
        print(daily.user_id)
        c=correction(description=cor,daily_id=daily.id,executive_id=daily.user_id,event=None)
        c.save()
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    
def he_change_pass(request):
    ids=request.session['userid']
    usr = user_registration.objects.get(id=ids)
    if request.session.has_key('userid'):
        devid = request.session['userid']
    else:
        return redirect('/')
    dev = user_registration.objects.filter(id=devid)

    if request.method == 'POST':
        abc = user_registration.objects.get(id=devid)
        cur = abc.password
        oldps = request.POST["currentPassword"]
        newps = request.POST["newPassword"]
        cmps = request.POST["confirmPassword"]
        if oldps == cur:
            if oldps != newps:
                if newps == cmps:
                    abc.password = request.POST.get('confirmPassword')
                    abc.save()
                    return render(request, 'head/he_ch_pass.html', {'dev': dev,"usr":usr})
            elif oldps == newps:
                messages.add_message(request, messages.INFO, 'Current and New password same')
            else:
                messages.info(request, 'Incorrect password same')

            return render(request, 'head/he_ch_pass.html', {'dev': dev,"usr":usr})
        else:
            messages.add_message(request, messages.INFO, 'old password wrong')
            return render(request, 'head/he_ch_pass.html', {'dev': dev,"usr":usr})
    return render(request, 'head/he_ch_pass.html', {'dev': dev,"usr":usr})


def he_accountset(request):
    ids=request.session['userid']
    usr = user_registration.objects.get(id=ids)
    if request.session.has_key('userid'):
        devid = request.session['userid']
    else:
        return redirect('/')
    dev = user_registration.objects.filter(id=devid)
    return render(request, 'head/he_accountset.html', {'dev': dev,"usr":usr})

def he_imagechange(request, id):
    ids=request.session['userid']
    usr = user_registration.objects.get(id=ids)
    if request.session.has_key('userid'):
        devid = request.session['userid']
    else:
        return redirect('/')
    dev = user_registration.objects.filter(id=devid)
    if request.method == 'POST':
        abc = user_registration.objects.get(id=id)
        abc.photo = request.FILES['filename']
        abc.save()
        return redirect('he_accountset')
    return render(request, 'head/he_accountset.html',{'dev': dev,"usr":usr})


def he_flt_progress(request):
    ids=request.session['userid']
    usr = user_registration.objects.get(id=ids)
    st_dt=request.POST.get('str_dt')
    en_dt=request.POST.get('end_dt')
  
    pr_work=progress_report.objects.filter(start_date__gte=st_dt,start_date__lte=en_dt)
    context={
        "usr":usr,
        "prgs":pr_work

    }
    return render(request, 'head/he_workprogress_executive.html',context)

def he_view_post(request,id):
    ids=request.session['userid']
    usr = user_registration.objects.get(id=ids)
    today = date.today()
    event=Events.objects.filter(executive=id, start__date=today)
    hr_list=["09:00:00","10:00:00","11:00:00","12:00:00","13:00:00","14:00:00","15:00:00","16:00:00"]
    start_values = [i.start.strftime("%H:%M:%S") for i in event]
    unschedule = [datetime.strptime(elem, '%H:%M:%S').strftime('%I:%M %p') for elem in hr_list if elem not in start_values]
    return render(request,'head/he_view_post.html',{"usr":usr,'evnt':event,'unsh':unschedule})

def he_add_correction(request,id):
    if request.method=='POST':
        cor=request.POST.get('cor')
        event=Events.objects.get(id=id)
        c=correction(description=cor,executive_id=event.executive.id,event_id=event.id,daily=None)
        c.save()
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

        
def he_add_status(request,id):
    if request.method=='POST':
        status=request.POST.get('status')   
        daily=daily_work.objects.get(id=id)
        daily.status=status
        daily.save()
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    
def he_add_event_status(request,id):
    if request.method=='POST':
        status=request.POST.get('status')   
        event=Events.objects.get(id=id)
        event.status=status
        event.save()
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))    
    

def he_smo_exe(request):
    ids=request.session['userid']
    usr = user_registration.objects.get(id=ids)
    exe=user_registration.objects.filter(department="Digital Marketing Executive")
    return render(request, 'head/he_smo_exe.html',{'exe':exe,"usr":usr})

def he_cor_exe(request):
    ids=request.session['userid']
    usr = user_registration.objects.get(id=ids)
    exe=user_registration.objects.filter(department="Digital Marketing Executive")
    return render(request, 'head/he_cor_exe.html',{'exe':exe,"usr":usr})

def he_cor_exe_det(request,id):
    ids=request.session['userid']
    usr = user_registration.objects.get(id=ids)
    cor=correction.objects.filter(executive=id)
    

    context={
        "usr":usr,
        "warn":cor,
        

    }
    return render(request, 'head/he_cor_exe_det.html',context)


#-------------------------------------------------------------------------------Smo Submission
def smo_base(request):
    ids=request.session['smo_userid']
    usr = smo_registration.objects.get(id=ids)
   
    

    context={
        "usr":usr,
      
    }
    return render(request, 'smo/publishing/smo_base.html',context)

def smo_login(request,id):
    work=Work.objects.get(id=id)
    return render(request, 'smo/index/smo_login.html', {'id':work.client_name_id})

def smo_signup(request,id):
    return render(request, 'smo/index/smo_signup.html', {'id':id})



def smo_reg(request,id):

 
    a = smo_registration()
    
    
    
    client=client_information.objects.get(id=id)
    if request.method == 'POST':
        if  smo_registration.objects.filter(email=request.POST['email']).exists():
            
            msg_error = "Mail id already exist"
            return render(request, 'smo/index/smo_signup.html',{'msg_error': msg_error})
        else:
            if request.POST['password'] == request.POST['re_password']:
                a.fullname = request.POST['fname']
                a.email = request.POST['email']
                a.password = request.POST['password']
                a.photo = request.FILES['photo']
                a.client=client
                a.save()
                return redirect('smo_login',id)
            else:
                msg_error = "Mail id already exist"
                return render(request, 'smo/index/smo_signup.html',{'msg_error': msg_error, "id": id})

def smo_signin(request,id):  
    if request.method == 'POST':
        email  = request.POST['email']
        password = request.POST['password']
        
        if smo_registration.objects.filter(email=request.POST['email'], password=request.POST['password']).exists():
            smo_ex = smo_registration.objects.get(email=request.POST['email'],password=request.POST['password'])

            #---------------------- executive session id
            ids=request.session['userid']
            usr = user_registration.objects.get(id=ids)
            request.session['userid'] = usr.id
            #---------------------- smo submission login session id
            request.session['smo_userid'] = smo_ex.id
            
            return redirect('smo_dash')
    return redirect('smo_login',id) 

def smo_dash(request):
    ids=request.session['smo_userid']
    usr = smo_registration.objects.get(id=ids)
    context={
            "usr":usr,
        }
    return render(request, 'smo/publishing/smo_dashboard.html',context)

def smo_cnt_chnl(request):
    ids=request.session['smo_userid']
    usr = smo_registration.objects.get(id=ids)
    context={
            "usr":usr,
        }
    return render(request, 'smo/publishing/connect_channel.html',context) 


def published_post(request):
    ids=request.session['smo_userid']
    usr = smo_registration.objects.get(id=ids)
    context={
            "usr":usr,
        }
    return render(request, 'smo/publishing/published_post.html',context)


def create_post(request):
    ids=request.session['smo_userid']
    usr = smo_registration.objects.get(id=ids) 
    post = smo_post.objects.filter(smo=usr)
    addi_post = addi_smo_post.objects.all()
    
    dt=date.today()
    context={
            "usr":usr,
            "post":post,
            "dt":dt,
            "addi_post":addi_post
        }
    return render(request, 'smo/publishing/create_post.html',context)


def edit_post_drft(request,id):
    if request.method == 'POST':
        ids=request.session['smo_userid']
        usr = smo_registration.objects.get(id=ids)
        b=smo_post.objects.get(id=id)
        b.description = request.POST['description']
        b.status=request.POST['status']
        b.st_file=request.FILES.get('cmpl_file',None)
        if request.FILES.get('filed',None) == None:
            pass
        else:
            dct_file = dict(request.FILES)
            try:
                lst_screenshot = dct_file['filed']
                lst_file = []
                for ins_screenshot in lst_screenshot:
                    str_img_path = ""
                    if ins_screenshot:
                        img_emp = ins_screenshot
                        fs = FileSystemStorage(location=settings.MEDIA_ROOT,base_url=settings.MEDIA_URL)
                        str_img = fs.save(''.join(filter(str.isalnum, str(img_emp))), img_emp)
                        str_img_path = fs.url(''.join(filter(str.isalnum, str_img)))
                        lst_file.append('/media/'+''.join(filter(str.isalnum, str(img_emp))))
                        b.json_testerscreenshot = lst_file
            except:
                b.json_testerscreenshot=b.json_testerscreenshot
        b.smo=usr
     
        b.save()
        return redirect('create_post')

    return redirect('create_post')


def save_post_drft(request):
    idr=request.session['userid']
    usr_lg = user_registration.objects.get(id=idr)

    if request.method == 'POST':

        ids=request.session['smo_userid']
        usr = smo_registration.objects.get(id=ids)
        b=smo_post()
        b.description = request.POST['description']
        b.status="draft"
        dct_file = dict(request.FILES)
        lst_screenshot = dct_file['filed']
        lst_file = []
        for ins_screenshot in lst_screenshot:
            str_img_path = ""
            if ins_screenshot:
                img_emp = ins_screenshot
                fs = FileSystemStorage(location=settings.MEDIA_ROOT,base_url=settings.MEDIA_URL)
                str_img = fs.save(''.join(filter(str.isalnum, str(img_emp))), img_emp)
                str_img_path = fs.url(''.join(filter(str.isalnum, str_img)))
                lst_file.append('/media/'+''.join(filter(str.isalnum, str(img_emp))))
                b.json_testerscreenshot = lst_file

        
        b.json_testerscreenshot=b.json_testerscreenshot
        b.smo=usr
        b.executive=usr_lg


        b.fb = request.POST.get('fb',None)
        b.fb_dt = request.POST.get('fb_txt',None)
        b.fb_file = request.FILES.get('fb_file',None)
        b.tw = request.POST.get('tw',None)
        b.tw_dt = request.POST.get('tw_txt',None)
        b.tw_file = request.FILES.get('tw_file',None)
        b.pin = request.POST.get('pin',None)
        b.pin_dt = request.POST.get('pin_txt',None)
        b.pin_file = request.FILES.get('pin_file',None)
        b.link = request.POST.get('link',None)
        b.link_dt = request.POST.get('link_txt',None)
        b.link_file = request.FILES.get('link_file',None)
        b.insta = request.POST.get('insta',None)
        b.insta_dt = request.POST.get('insta_txt',None)
        b.insta_file = request.FILES.get('insta_file',None)
        b.tumb = request.POST.get('tumb',None)
        b.tumb_dt = request.POST.get('tumb_txt',None)
        b.tumb_file = request.FILES.get('tumb_file',None)
        b.diry = request.POST.get('diry',None)
        b.diry_dt = request.POST.get('diry_txt',None)
        b.diry_file = request.FILES.get('diry_file',None)
        b.yt = request.POST.get('yt',None)
        b.yt_dt = request.POST.get('yt_txt',None)
        b.yt_file = request.FILES.get('yt_file',None)
        b.qra = request.POST.get('qra',None)
        b.qra_dt = request.POST.get('qra_txt',None)
        b.qra_file = request.FILES.get('qra_file',None)
        b.sbms = request.POST.get('sbms',None)
        b.sbms_dt = request.POST.get('sbms_txt',None)
        b.sbms_file = request.FILES.get('sbms_file',None)
        
        b.save()

        
        label_req =request.POST.getlist('sub_lb[]')
        dt =request.POST.getlist('dates[]') 
        files_req =request.FILES.getlist('sub_file[]') 
      

        
        if len(files_req)==len(label_req)==len(dt):
            mapped2 = zip(label_req,dt,files_req)
            mapped2=list(mapped2)
         
            for ele in mapped2:
                created = addi_smo_post.objects.get_or_create(label=ele[0],date=ele[1],file=ele[2],executive=usr_lg,smo=usr,post=b)
        return redirect('create_post')
    return redirect('create_post')


def content(request):
    ids=request.session['smo_userid']
    usr = smo_registration.objects.get(id=ids) 
    post = smo_post.objects.filter(smo=usr)
    addi_post=addi_smo_post.objects.all()

    context={
            "usr":usr,
            "post":post,
            "addi_post":addi_post
        }
    return render(request, 'smo/publishing/content.html',context)


def logout_smo(request):
    if 'smo_userid' in request.session:  
        request.session.flush()
        return redirect('/')
    else:
        return redirect('/') 

def smo_change_pass(request):
    ids=request.session['smo_userid']
    usr = smo_registration.objects.get(id=ids)
    if request.session.has_key('smo_userid'):
        devid = request.session['smo_userid']
    else:
        return redirect('/')
    dev = smo_registration.objects.filter(id=devid)

    if request.method == 'POST':
        abc = smo_registration.objects.get(id=devid)
        cur = abc.password
        oldps = request.POST["currentPassword"]
        newps = request.POST["newPassword"]
        cmps = request.POST["confirmPassword"]
        if oldps == cur:
            if oldps != newps:
                if newps == cmps:
                    abc.password = request.POST.get('confirmPassword')
                    abc.save()
                    return render(request, 'smo/index/smo_change_password.html', {'dev': dev,"usr":usr})
            elif oldps == newps:
                messages.add_message(request, messages.INFO, 'Current and New password same')
            else:
                messages.info(request, 'Incorrect password same')

            return render(request, 'smo/index/smo_change_password.html', {'dev': dev,"usr":usr})
        else:
            messages.add_message(request, messages.INFO, 'old password wrong')
            return render(request, 'smo/index/smo_change_password.html', {'dev': dev,"usr":usr})
    return render(request, 'smo/index/smo_change_password.html', {'dev': dev,"usr":usr})


def sm_calendar(request):
    ids=request.session['smo_userid']
    usr = smo_registration.objects.get(id=ids)
    all_events = Events.objects.all()
    context = {
        "events":all_events,
        "usr":usr,
    }
    return render(request, 'smo/publishing/calendar.html',context)


   
def all_events(request):
    all_events = Events.objects.all()
    out=[]
    for event in all_events:
        out.append({
            "title":event.name,
            "id":event.id,
            "start":event.start.strftime("%m/%d/%Y, %H:%M:%S"), 
        })
    return JsonResponse(out, safe=False) 
 
 
def add_event(request):
    ids=request.session['userid']
    usr = user_registration.objects.get(id=ids)
    if request.method == 'POST':
        start = request.POST.get('start', None)
        title = request.POST.get('title', None)
        img = request.FILES.get('file', None)
        date_obj = datetime.strptime(start, "%Y-%m-%d %H:%M:%S")
        one_hour = timedelta(hours=1)
        new_date_obj = date_obj + one_hour
        end = new_date_obj.strftime("%Y-%m-%d %H:%M:%S.%f")
        event = Events(name=title, start=start,end=end, img=img,executive=usr, status="draft") 
        event.save()
        data = {}
        return JsonResponse(data)
 
def update(request):
    start = request.GET.get("start", None)
    end = request.GET.get("end", None)
    title = request.GET.get("title", None)
    id = request.GET.get("id", None)
    event = Events.objects.get(id=id)
    event.start = start
    event.end = end
    event.name = title
    event.save()
    data = {}
    return JsonResponse(data)
 
def remove(request):
    id = request.GET.get("id", None)
    event = Events.objects.get(id=id)
    event.delete()
    data = {}
    return JsonResponse(data)







