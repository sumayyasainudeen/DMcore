from django.db import models
from email.policy import default

from unittest.util import _MAX_LENGTH
from xmlrpc.client import boolean
from django.contrib.auth.models import User

# from django.contrib.postgres.fields import JSONField
from django.db.models import JSONField
# Create your models here.


# login

class user_registration(models.Model):
    designation = models.CharField(max_length=240, null=True)
    department = models.CharField(max_length=240, null=True)
    fullname = models.CharField(max_length=240, null=True)
    fathername = models.CharField(max_length=240, null=True)
    mothername = models.CharField(max_length=240, null=True)
    dateofbirth = models.DateField(
        auto_now_add=False, auto_now=False,  null=True, blank=True)
    gender = models.CharField(max_length=240, null=True)
    presentaddress1 = models.CharField(max_length=240, null=True)
    presentaddress2 = models.CharField(max_length=240, null=True)
    presentaddress3 = models.CharField(max_length=240, null=True)
    pincode = models.CharField(max_length=240, null=True)
    district = models.CharField(max_length=240, null=True)
    state = models.CharField(max_length=240, null=True)
    country = models.CharField(max_length=240, null=True)
    permanentaddress1 = models.CharField(max_length=240, null=True)
    permanentaddress2 = models.CharField(max_length=240, null=True)
    permanentaddress3 = models.CharField(max_length=240, null=True)
    permanentpincode = models.CharField(max_length=240, null=True)
    permanentdistrict = models.CharField(max_length=240, null=True)
    permanentstate = models.CharField(max_length=240, null=True)
    permanentcountry = models.CharField(max_length=240, null=True)
    mobile = models.CharField(max_length=240, null=True)
    alternativeno = models.CharField(max_length=240, null=True)
    employee_id = models.CharField(max_length=240,null=True,default='')
    email = models.EmailField(max_length=240, null=True)
    password = models.CharField(max_length=240, null=True)
    idproof = models.FileField(upload_to='images/', null=True, blank=True)
    photo = models.FileField(upload_to='images/', null=True, blank=True)
    attitude = models.IntegerField(default='0')
    creativity = models.IntegerField(default='0')
    workperformance = models.IntegerField(default='0')
    joiningdate = models.DateField(
        auto_now_add=True, auto_now=False,  null=True, blank=True)
    startdate = models.DateField(
        auto_now_add=True, auto_now=False,  null=True, blank=True)
    enddate = models.DateField(
        auto_now_add=True, auto_now=False,  null=True, blank=True)
    status = models.CharField(max_length=240, null=True, default="active")
    tl_id = models.IntegerField(default='0',null=True, blank=True)
    projectmanager_id = models.IntegerField(default='0',null=True, blank=True)
    total_pay=models.IntegerField(default='0')
    payment_balance = models.IntegerField( default='0')
    account_no = models.CharField(max_length=200, null=True,blank=True, default='')
    ifsc =  models.CharField(max_length=200, null=True, default='')
    bank_name = models.CharField(max_length=240, null=True,blank=True, default='')
    bank_branch = models.CharField(max_length=240, null=True, default='')
    payment_status = models.CharField(max_length=200, null=True, default='')
    offerqr = models.CharField(max_length=500, default='',null=True,blank=True)
    relieveqr = models.CharField(max_length=500, default='',null=True,blank=True)
    expqr = models.CharField(max_length=500, default='',null=True,blank=True)
    hrmanager = models.CharField(max_length=500, default='',null=True,blank=True)
    confirm_salary = models.CharField(max_length=10, default='')
    confirm_salary_status = models.CharField(max_length=255, default='0')
    payment_file_downlod = models.FileField(upload_to = 'images/', null=True, blank=True)
    total_amount=models.IntegerField(default='0')
    payment_amount_date =models.DateField(auto_now_add=False, auto_now=False,  null=True, blank=True)
    salary_pending = models.CharField(max_length=100, default='')
    salary_status =  models.CharField(max_length=10, default='')
    trainer_level = models.CharField(max_length=20, default='',null=True, blank=True)
    hr_designation = models.CharField(max_length=120, default='',null=True, blank=True)
    reg_status =  models.CharField(max_length=10, default='0')
    trainee_delay=models.IntegerField(default=0)
 
    def __str__(self):
        return self.fullname

    @property
    def avg(self):
        return (self.attitude+self.creativity+self.workperformance)/3

class qualification(models.Model):
    user = models.ForeignKey(user_registration, on_delete=models.SET_NULL,
                             related_name='qualificationuser', null=True, blank=True)
    plustwo = models.CharField(max_length=240, null=True)
    schoolaggregate = models.CharField(max_length=240, null=True)
    schoolcertificate = models.FileField(
        upload_to='images/', null=True, blank=True)
    ugdegree = models.CharField(max_length=240, null=True)
    ugstream = models.CharField(max_length=240, null=True)
    ugpassoutyr = models.CharField(max_length=240, null=True)
    ugaggregrate = models.CharField(max_length=240, null=True)
    backlogs = models.CharField(max_length=240, null=True)
    ugcertificate = models.FileField(
        upload_to='images/', null=True, blank=True)
    pg = models.CharField(max_length=240, null=True)
    status = models.CharField(max_length=100, default='')


    def __str__(self):
        return self.user

class extracurricular(models.Model):
    user = models.ForeignKey(user_registration, on_delete=models.SET_NULL,
                             related_name='extracurricularuser', null=True, blank=True)
    internshipdetails = models.CharField(max_length=240, null=True)
    internshipduration = models.CharField(max_length=240, null=True)
    internshipcertificate = models.FileField(
        upload_to='images/', null=True, blank=True)
    onlinetrainingdetails = models.CharField(max_length=240, null=True)
    onlinetrainingduration = models.CharField(max_length=240, null=True)
    onlinetrainingcertificate = models.FileField(
        upload_to='images/', null=True, blank=True)
    projecttitle = models.CharField(max_length=240, null=True)
    projectduration = models.CharField(max_length=240, null=True)
    projectdescription = models.TextField(null=True)
    projecturl = models.CharField(
        max_length=240, default='', null=True, blank=True)
    skill1 = models.CharField(
        max_length=240, default='', null=True, blank=True)
    skill2 = models.CharField(
        max_length=240, default='', null=True, blank=True)
    skill3 = models.CharField(
        max_length=240, default='', null=True, blank=True)
    status = models.CharField(max_length=240, default='')


    def __str__(self):
        return self.projecttitle

class internship(models.Model):

    reg_date = models.DateField(
        auto_now_add=False, auto_now=False,  null=True, blank=True)
    fullname = models.CharField(max_length=200)
    collegename = models.CharField(max_length=200)
    reg_no = models.CharField(max_length=200)
    course = models.CharField(max_length=200)
    stream = models.CharField(max_length=200)
    platform = models.CharField(max_length=200)
    start_date = models.CharField(max_length=200)
    end_date = models.CharField(max_length=200)
    mobile = models.CharField(max_length=200)
    alternative_no = models.CharField(max_length=200)
    email = models.EmailField()
    profile_pic = models.ImageField(upload_to='images/internship/', null=True, blank=True)
    qr = models.CharField(max_length=200, default='')
    
    def __str__(self):
        return self.fullname

class client_information(models.Model):
    user = models.ForeignKey(user_registration, on_delete=models.SET_NULL, null=True, blank=True)
    client_name = models.CharField(max_length=200,default='', null=True, blank=True)
    client_address = models.CharField(max_length=200,default='', null=True, blank=True)
    client_mail = models.CharField(max_length=200,default='', null=True, blank=True)
    bs_name = models.CharField(max_length=200,default='', null=True, blank=True)
    bs_website = models.CharField(max_length=200,default='', null=True, blank=True)
    bs_location = models.CharField(max_length=200,default='', null=True, blank=True)
    client_files = models.ImageField(upload_to='images/client/', null=True, blank=True)

    seo = models.CharField(max_length=200,default='', null=True, blank=True)
    seo_txt = models.TextField(default='', null=True, blank=True)
    seo_file = models.ImageField(upload_to='images/requirement/', null=True, blank=True)
    seo_target =models.TextField(default='', null=True, blank=True)
    on_pg = models.CharField(max_length=200,default='', null=True, blank=True)
    on_pg_txt = models.TextField(default='', null=True, blank=True)
    on_pg_file = models.ImageField(upload_to='images/requirement/', null=True, blank=True)
    on_pg_target =models.TextField(default='', null=True, blank=True)
    off_pg = models.CharField(max_length=200,default='', null=True, blank=True)
    off_pg_txt = models.TextField(default='', null=True, blank=True)
    off_pg_file = models.ImageField(upload_to='images/requirement/', null=True, blank=True)
    off_pg_target =models.TextField(default='', null=True, blank=True)

    smo = models.CharField(max_length=200,default='', null=True, blank=True)
    smo_txt = models.TextField(default='', null=True, blank=True)
    smo_file = models.ImageField(upload_to='images/requirement/', null=True, blank=True)
    smo_target =models.TextField(default='', null=True, blank=True)
    smm = models.CharField(max_length=200,default='', null=True, blank=True)
    smm_txt = models.TextField(default='', null=True, blank=True)
    smm_file = models.ImageField(upload_to='images/requirement/', null=True, blank=True)
    smm_target =models.TextField(default='', null=True, blank=True)
    sem = models.CharField(max_length=200,default='', null=True, blank=True)
    sem_txt = models.TextField(default='', null=True, blank=True)
    sem_file =models.ImageField(upload_to='images/requirement/', null=True, blank=True)
    sem_target =models.TextField(default='', null=True, blank=True)
    em = models.CharField(max_length=200,default='', null=True, blank=True)
    em_txt = models.TextField(default='', null=True, blank=True)
    em_file = models.ImageField(upload_to='images/requirement/', null=True, blank=True)
    em_target =models.TextField(default='', null=True, blank=True)
    cm = models.CharField(max_length=200,default='', null=True, blank=True)
    cm_txt = models.TextField(default='', null=True, blank=True)
    cm_file = models.ImageField(upload_to='images/requirement/', null=True, blank=True)
    cm_target =models.TextField(default='', null=True, blank=True)
    am = models.CharField(max_length=200,default='', null=True, blank=True)
    am_txt = models.TextField(default='', null=True, blank=True)
    am_file = models.ImageField(upload_to='images/requirement/', null=True, blank=True)
    am_target =models.TextField(default='', null=True, blank=True)
    mm = models.CharField(max_length=200,default='', null=True, blank=True)
    mm_txt = models.TextField(default='', null=True, blank=True)
    mm_file = models.ImageField(upload_to='images/requirement/', null=True, blank=True)
    mm_target =models.TextField(default='', null=True, blank=True)
    vm = models.CharField(max_length=200,default='', null=True, blank=True)
    vm_txt = models.TextField(default='', null=True, blank=True)
    vm_file = models.ImageField(upload_to='images/requirement/', null=True, blank=True)
    vm_target =models.TextField(default='', null=True, blank=True)

    lc = models.CharField(max_length=200,default='', null=True, blank=True)
    lc_txt = models.TextField(default='', null=True, blank=True)
    lc_file = models.ImageField(upload_to='images/requirement/', null=True, blank=True)
    lc_target =models.TextField(default='', null=True, blank=True)



class addi_client_info(models.Model):
    user = models.ForeignKey(user_registration, on_delete=models.SET_NULL, null=True, blank=True)
    client = models.ForeignKey(client_information, on_delete=models.SET_NULL, null=True, blank=True)
    labels = models.CharField(max_length=220,default='', null=True, blank=True)
    discription =models.TextField(default='', null=True, blank=True)
    file =models.ImageField(upload_to='images/requirement/', null=True, blank=True)

    section = models.CharField(max_length=220,default='', null=True, blank=True)
    target = models.TextField(default='', null=True, blank=True)



class Work(models.Model):
    client_name = models.ForeignKey(client_information, on_delete=models.CASCADE, null=True,related_name='client_works', blank=True) 
    cl_name = models.CharField(max_length=200,default='', null=True, blank=True)
    task=models.TextField(default='', null=True, blank=True)
    sub_task=models.TextField(default='', null=True, blank=True)
    sub_des=models.TextField(default='', null=True, blank=True)
    sub_file=models.ImageField(upload_to='images/pdf/',default='', null=True, blank=True)
    description=models.TextField(default='', null=True, blank=True)
    file_attached=models.FileField(upload_to='images/pdf/',default='', null=True, blank=True)
    start_date=models.DateField(auto_now_add=False, auto_now=False,  null=True, blank=True)
    end_date=models.DateField(auto_now_add=False, auto_now=False,  null=True, blank=True)
    file_2=models.FileField(upload_to='images/pdf/',default='', null=True, blank=True)
    target=models.CharField(max_length=255,null=True,blank=True)

class work_asign(models.Model):
    client_name = models.ForeignKey(client_information, on_delete=models.CASCADE, null=True, blank=True) 
    work=models.ForeignKey(Work,on_delete=models.CASCADE,null=True,blank=True)   
    exe_name=models.ForeignKey(user_registration, on_delete=models.CASCADE,related_name='exe_works' ,null=True, blank=True)

class daily_work(models.Model):
    work=models.ForeignKey(Work,on_delete=models.CASCADE,null=True,blank=True)  
    user = models.ForeignKey(user_registration, on_delete=models.SET_NULL, null=True, blank=True)
    cl_name = models.CharField(max_length=200,default='', null=True, blank=True)
    task=models.TextField(default='', null=True, blank=True)
    date=models.DateField(auto_now_add=False, auto_now=False,  null=True, blank=True)
    workdone=models.TextField(default='', null=True, blank=True)
    json=models.FileField(upload_to = 'images/pdf/', null=True, blank=True,default='')
    json_testerscreenshot = JSONField(blank=True, null=True,default='')

    fb = models.CharField(max_length=200,default='', null=True, blank=True)
    fb_txt = models.TextField(default='', null=True, blank=True)
    fb_file = models.ImageField(upload_to='images/sub/', null=True, blank=True)
    tw = models.CharField(max_length=200,default='', null=True, blank=True)
    tw_txt = models.TextField(default='', null=True, blank=True)
    tw_file = models.ImageField(upload_to='images/sub/', null=True, blank=True)
    pin = models.CharField(max_length=200,default='', null=True, blank=True)
    pin_txt = models.TextField(default='', null=True, blank=True)
    pin_file = models.ImageField(upload_to='images/sub/', null=True, blank=True)
    link = models.CharField(max_length=200,default='', null=True, blank=True)
    link_txt = models.TextField(default='', null=True, blank=True)
    link_file = models.ImageField(upload_to='images/sub/', null=True, blank=True)
    insta = models.CharField(max_length=200,default='', null=True, blank=True)
    insta_txt = models.TextField(default='', null=True, blank=True)
    insta_file = models.ImageField(upload_to='images/sub/', null=True, blank=True)
    tumb = models.CharField(max_length=200,default='', null=True, blank=True)
    tumb_txt = models.TextField(default='', null=True, blank=True)
    tumb_file = models.ImageField(upload_to='images/sub/', null=True, blank=True)
    diry = models.CharField(max_length=200,default='', null=True, blank=True)
    diry_txt = models.TextField(default='', null=True, blank=True)
    diry_file = models.ImageField(upload_to='images/sub/', null=True, blank=True)
    yt = models.CharField(max_length=200,default='', null=True, blank=True)
    yt_txt = models.TextField(default='', null=True, blank=True)
    yt_file = models.ImageField(upload_to='images/sub/', null=True, blank=True)
    qra = models.CharField(max_length=200,default='', null=True, blank=True)
    qra_txt = models.TextField(default='', null=True, blank=True)
    qra_file = models.ImageField(upload_to='images/sub/', null=True, blank=True)
    sbms = models.CharField(max_length=200,default='', null=True, blank=True)
    sbms_txt = models.TextField(default='', null=True, blank=True)
    sbms_file = models.ImageField(upload_to='images/sub/', null=True, blank=True)

    pr = models.CharField(max_length=200,default='', null=True, blank=True)
    pr_txt = models.TextField(default='', null=True, blank=True)
    pr_file = models.ImageField(upload_to='images/sub/', null=True, blank=True)
    art = models.CharField(max_length=200,default='', null=True, blank=True)
    art_txt = models.TextField(default='', null=True, blank=True)
    art_file = models.ImageField(upload_to='images/sub/', null=True, blank=True)
    blg = models.CharField(max_length=200,default='', null=True, blank=True)
    blg_txt = models.TextField(default='', null=True, blank=True)
    blg_file = models.ImageField(upload_to='images/sub/', null=True, blank=True)
    clss = models.CharField(max_length=200,default='', null=True, blank=True)
    clss_txt = models.TextField(default='', null=True, blank=True)
    clss_file = models.ImageField(upload_to='images/sub/', null=True, blank=True)
    gst = models.CharField(max_length=200,default='', null=True, blank=True)
    gst_txt = models.TextField(default='', null=True, blank=True)
    gst_file = models.ImageField(upload_to='images/sub/', null=True, blank=True)
    bk = models.CharField(max_length=200,default='', null=True, blank=True)
    bk_txt = models.TextField(default='', null=True, blank=True)
    bk_file = models.ImageField(upload_to='images/sub/', null=True, blank=True)
    status= models.CharField(max_length=200,default='', null=True, blank=True)
    
class daily_work_sub(models.Model):
    daily=models.ForeignKey(daily_work,on_delete=models.CASCADE,null=True,blank=True)
    sub = models.CharField(max_length=200,default='', null=True, blank=True)
    sub_txt = models.TextField(default='', null=True, blank=True)
    sub_file = models.ImageField(upload_to='images/sub/', null=True, blank=True)


class daily_off_sub(models.Model):
    daily=models.ForeignKey(daily_work,on_delete=models.CASCADE,null=True,blank=True)
    sub = models.CharField(max_length=200,default='', null=True, blank=True)
    sub_txt = models.TextField(default='', null=True, blank=True)
    sub_file = models.ImageField(upload_to='images/sub/', null=True, blank=True)

class daily_leeds(models.Model):
    daily=models.ForeignKey(daily_work,on_delete=models.CASCADE,null=True,blank=True)
    sub = models.CharField(max_length=200,default='', null=True, blank=True)
    sub_txt = models.TextField(default='', null=True, blank=True)
    sub_file = models.ImageField(upload_to='images/sub/', null=True, blank=True)

class progress_report(models.Model):
    work=models.ForeignKey(Work,on_delete=models.CASCADE,null=True,blank=True)
    user = models.ForeignKey(user_registration, on_delete=models.SET_NULL, null=True, blank=True)
    cl_name = models.CharField(max_length=200,default='', null=True, blank=True)
    task=models.TextField(default='', null=True, blank=True)
    audit_rprt=models.FileField(upload_to='images/pdf/',default='', null=True, blank=True)
    graph=models.FileField(upload_to='images/graph/',default='', null=True, blank=True)
    start_date=models.DateField(auto_now_add=False, auto_now=False,  null=True, blank=True)
    end_date=models.DateField(auto_now_add=False, auto_now=False,  null=True, blank=True)

    
class Warning(models.Model):
    executive=models.ForeignKey(user_registration, on_delete=models.CASCADE, null=True, blank=True)
    description=models.TextField()
    type=models.CharField(max_length=255)
    date=models.DateField(auto_now_add=True, null=False)
    reply=models.TextField(null=True)



#------------------------------------------------------------------------smo Registration
class smo_registration(models.Model):
    
    fullname = models.CharField(max_length=240, null=True)
    email = models.CharField(max_length=240, null=True)
    password = models.CharField(max_length=240, null=True)
    photo = models.FileField(upload_to='images/', null=True, blank=True)
    client = models.ForeignKey(client_information, on_delete=models.SET_NULL, null=True, blank=True)

class smo_post(models.Model):
    description = models.TextField(null=True)
    status = models.CharField(max_length=240,null=True)
    st_file = models.ImageField(upload_to='images/smo_post/', null=True, blank=True)
    json=models.FileField(upload_to = 'images/smo_post/', null=True, blank=True,default='')
    json_testerscreenshot = JSONField(blank=True, null=True,default='')
    smo = models.ForeignKey(smo_registration, on_delete=models.SET_NULL, null=True, blank=True)
    executive=models.ForeignKey(user_registration, on_delete=models.CASCADE, null=True, blank=True)
    date = models.DateField(null=True,blank=True)
    fb = models.CharField(max_length=255,null=True,blank=True,default='')
    fb_dt = models.CharField(max_length=255,null=True,blank=True)
    fb_file = models.ImageField(upload_to='images/smo_post/', null=True, blank=True)
    tw = models.CharField(max_length=255,null=True,blank=True,default='')
    tw_dt = models.CharField(max_length=255,null=True,blank=True)
    tw_file = models.ImageField(upload_to='images/smo_post/', null=True, blank=True)
    pin = models.CharField(max_length=255,null=True,blank=True,default='')
    pin_dt = models.CharField(max_length=255,null=True,blank=True)
    pin_file = models.ImageField(upload_to='images/smo_post/', null=True, blank=True)
    link = models.CharField(max_length=255,null=True,blank=True,default='')
    link_dt = models.CharField(max_length=255,null=True,blank=True)
    link_file = models.ImageField(upload_to='images/smo_post/', null=True, blank=True)
    insta = models.CharField(max_length=255,null=True,blank=True,default='')
    insta_dt = models.CharField(max_length=255,null=True,blank=True)
    insta_file = models.ImageField(upload_to='images/smo_post/', null=True, blank=True)
    tumb = models.CharField(max_length=255,null=True,blank=True,default='')
    tumb_dt = models.CharField(max_length=255,null=True,blank=True)
    tumb_file = models.ImageField(upload_to='images/smo_post/', null=True, blank=True)
    diry = models.CharField(max_length=255,null=True,blank=True,default='')
    diry_dt = models.CharField(max_length=255,null=True,blank=True)
    diry_file = models.ImageField(upload_to='images/smo_post/', null=True, blank=True)
    yt = models.CharField(max_length=255,null=True,blank=True,default='')
    yt_dt = models.CharField(max_length=255,null=True,blank=True)
    yt_file = models.ImageField(upload_to='images/smo_post/', null=True, blank=True)
    qra = models.CharField(max_length=255,null=True,blank=True,default='')
    qra_dt = models.CharField(max_length=255,null=True,blank=True)
    qra_file = models.ImageField(upload_to='images/smo_post/', null=True, blank=True)
    sbms = models.CharField(max_length=255,null=True,blank=True,default='')
    sbms_dt = models.CharField(max_length=255,null=True,blank=True)
    sbms_file = models.ImageField(upload_to='images/smo_post/', null=True, blank=True)

class addi_smo_post(models.Model):
    smo = models.ForeignKey(smo_registration, on_delete=models.SET_NULL, null=True, blank=True)
    executive=models.ForeignKey(user_registration, on_delete=models.CASCADE, null=True, blank=True)
    post=models.ForeignKey(smo_post, on_delete=models.CASCADE, null=True, blank=True)
    label = models.CharField(max_length=255,null=True,blank=True)
    date = models.DateField(null=True,blank=True)
    file =models.ImageField(upload_to='images/smo_post/', null=True, blank=True)

class Events(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255,null=True,blank=True)
    start = models.DateTimeField(null=True,blank=True)
    end = models.DateTimeField(null=True,blank=True)
    img=models.ImageField(upload_to='images/smo_post/',null=True,blank=True)
    executive=models.ForeignKey(user_registration, on_delete=models.CASCADE, null=True, blank=True)
    status = models.CharField(max_length=240,null=True)
    fb = models.CharField(max_length=255,null=True,blank=True,default='')
    fb_dt = models.CharField(max_length=255,null=True,blank=True)
    fb_file = models.ImageField(upload_to='images/smo_post/', null=True,blank=True)
    tw = models.CharField(max_length=255,null=True,blank=True,default='')
    tw_dt = models.CharField(max_length=255,null=True,blank=True)
    tw_file = models.ImageField(upload_to='images/smo_post/', null=True,blank=True)
    pin = models.CharField(max_length=255,null=True,blank=True,default='')
    pin_dt = models.CharField(max_length=255,null=True,blank=True)
    pin_file = models.ImageField(upload_to='images/smo_post/', null=True,blank=True)
    link = models.CharField(max_length=255,null=True,blank=True,default='')
    link_dt = models.CharField(max_length=255,null=True,blank=True)
    link_file = models.ImageField(upload_to='images/smo_post/', null=True,blank=True)
    insta = models.CharField(max_length=255,null=True,blank=True,default='')
    insta_dt = models.CharField(max_length=255,null=True,blank=True)
    insta_file = models.ImageField(upload_to='images/smo_post/', null=True,blank=True)
    tumb = models.CharField(max_length=255,null=True,blank=True,default='')
    tumb_dt = models.CharField(max_length=255,null=True,blank=True)
    tumb_file = models.ImageField(upload_to='images/smo_post/', null=True,blank=True)
    diry = models.CharField(max_length=255,null=True,blank=True,default='')
    diry_dt = models.CharField(max_length=255,null=True,blank=True)
    diry_file = models.ImageField(upload_to='images/smo_post/', null=True,blank=True)
    yt = models.CharField(max_length=255,null=True,blank=True,default='')
    yt_dt = models.CharField(max_length=255,null=True,blank=True)
    yt_file = models.ImageField(upload_to='images/smo_post/', null=True,blank=True)
    qra = models.CharField(max_length=255,null=True,blank=True,default='')
    qra_dt = models.CharField(max_length=255,null=True,blank=True)
    qra_file = models.ImageField(upload_to='images/smo_post/', null=True,blank=True)
    sbms = models.CharField(max_length=255,null=True,blank=True,default='')
    sbms_dt = models.CharField(max_length=255,null=True,blank=True)
    sbms_file = models.ImageField(upload_to='images/smo_post/', null=True,blank=True)
    st_file = models.ImageField(upload_to='images/smo_post/', null=True,blank=True)

class correction(models.Model):
    executive=models.ForeignKey(user_registration, on_delete=models.CASCADE, null=True, blank=True)
    description=models.TextField()
    date=models.DateField(auto_now_add=True, null=False)
    reply=models.TextField(null=True)
    daily=models.ForeignKey(daily_work,on_delete=models.CASCADE,null=True,blank=True)
    event = models.ForeignKey(Events, on_delete=models.SET_NULL, null=True, blank=True)

class addi_events(models.Model):
    events = models.ForeignKey(Events, on_delete=models.SET_NULL, null=True, blank=True)
    executive=models.ForeignKey(user_registration, on_delete=models.CASCADE, null=True, blank=True)
    post=models.ForeignKey(smo_post, on_delete=models.CASCADE, null=True, blank=True)
    label = models.CharField(max_length=255,null=True,blank=True)
    date = models.DateField(null=True,blank=True)
    file =models.ImageField(upload_to='images/smo_post/', null=True, blank=True)