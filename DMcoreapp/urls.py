from django.urls import re_path,path
from . import views
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.views.static import serve

urlpatterns = [
    path('', views.login, name='login'),
    path('signin', views.signin, name='signin'),
    path('signup', views.signup, name='signup'),
    path('registration_form', views.registration_form, name='registration_form'),

    path('reset_password', views.reset_password, name='reset_password'),
    path('internshipform', views.internshipform, name='internshipform'),
    path('internship_save', views.internship_save, name='internship_save'), 
    path('get_warns', views.get_warns, name='get_warns'),
    path('get_requ', views.get_requ, name='get_requ'), 
    path('logout', views.logout, name='logout'),
    
    #---------------------------------------------------------------------------Admin Section
    path('ad_base', views.ad_base, name='ad_base'),
    path('ad_profile', views.ad_profile, name='ad_profile'),
    path('ad_dashboard', views.ad_dashboard, name='ad_dashboard'),
    path('ad_create_work', views.ad_create_work, name='ad_create_work'),
    path('save_create_work', views.save_create_work, name='save_create_work'),
    path('ad_view_work', views.ad_view_work, name='ad_view_work'),
    path('ad_view_clint/<int:id>', views.ad_view_clint, name='ad_view_clint'), 
    path('update_client/<int:id>', views.update_client, name='update_client'),
    path('ad_daily_work_det', views.ad_daily_work_det, name='ad_daily_work_det'),
    path('ad_work_analiz_det', views.ad_work_analiz_det, name='ad_work_analiz_det'),
    path('flt_dt_analiz', views.flt_dt_analiz, name='flt_dt_analiz'),
    path('ad_work_progress', views.ad_work_progress, name='ad_work_progress'),
    path('flt_progress', views.flt_progress, name='flt_progress'),
    path('ad_work_progress_det/<int:id>', views.ad_work_progress_det, name='ad_work_progress_det'),
    path('ad_warning_ex', views.ad_warning_ex, name='ad_warning_ex'),
    path('ad_warning_sugg_dash/<int:id>', views.ad_warning_sugg_dash, name='ad_warning_sugg_dash'),
    path('ad_warning_det/<int:id>', views.ad_warning_det, name='ad_warning_det'),
    path('ad_suggestions_det/<int:id>', views.ad_suggestions_det, name='ad_suggestions_det'),  
    path('change_pass', views.change_pass, name='change_pass'),  
   
    path('ad_imagechange/<int:id>', views.ad_imagechange, name='ad_imagechange'),
    path('ad_accountset', views.ad_accountset, name='ad_accountset'),  
    path('get_dis', views.get_dis, name='get_dis'), 
    path('ad_exe_smopost', views.ad_exe_smopost, name='ad_exe_smopost'),
    path('ad_sv_smopost/<int:id>', views.ad_sv_smopost, name='ad_sv_smopost'), 
    path('ad_get_smo_pst', views.ad_get_smo_pst, name='ad_get_smo_pst'), 
    path('get_event_det', views.get_event_det, name='get_event_det'), 
    path('filter_shedule/<int:id>', views.filter_shedule, name='filter_shedule'),  
    path('ad_export_excel/<int:id>', views.ad_export_excel, name='ad_export_excel'),

    path('ad_exe_det', views.ad_exe_det, name='ad_exe_det'),
    path('view_exe_leave/<int:id>', views.view_exe_leave, name='view_exe_leave'),
    path('ad_tele_det', views.ad_tele_det, name='ad_tele_det'),
    path('view_tele_leave<int:id>', views.view_tele_leave, name='view_tele_leave'),
    path('flt_leave_tl/<int:id>', views.flt_leave_tl, name='flt_leave_tl'),
    path('flt_leave_exe/<int:id>', views.flt_leave_exe, name='flt_leave_exe'),
    path('flt_leave_tele/<int:id>', views.flt_leave_tele, name='flt_leave_tele'),
    path('all_leads_exe', views.all_leads_exe, name='all_leads_exe'),
    path('ad_filter_day_previous_leads/<str:date>/<int:id>',views.ad_filter_day_previous_leads,name='ad_filter_day_previous_leads'),
    path('ad_filter_month_previous_leads/<str:date>/<int:id>',views.ad_filter_month_previous_leads,name='ad_filter_month_previous_leads'),
    path('ad_assign_Leads', views.ad_assign_Leads, name='ad_assign_Leads'),
    
    path('ad_assigned_person_details/<int:id>',views.ad_assigned_person_details, name='ad_assigned_person_details'),
    path('ad_view_exe_det/<int:id>', views.ad_view_exe_det, name='ad_view_exe_det'),
    path('ad_view_all_leads/<str:date>/<int:id>', views.ad_view_all_leads, name='ad_view_all_leads'),

    path('ad_filter_day_previous_assign/<int:id>',views.ad_filter_day_previous_assign,name='ad_filter_day_previous_assign'),
    path('ad_filter_month_previous_assign/<int:id>',views.ad_filter_month_previous_assign,name='ad_filter_month_previous_assign'),
    path('all_follow_tele', views.all_follow_tele, name='all_follow_tele'),
    path('all_nocall_tele', views.all_nocall_tele, name='all_nocall_tele'),
    path('ad_follow_tele_datewise/<int:tid>', views.ad_follow_tele_datewise, name='ad_follow_tele_datewise'),
    path('ad_follow_tele_det/<int:tid>/<str:date>', views.ad_follow_tele_det, name='ad_follow_tele_det'),
    path('ad_follow_tele_det_month/<int:id>',views.ad_follow_tele_det_month,name='ad_follow_tele_det_month'),
    path('ad_follow_tele_det_day/<int:id>',views.ad_follow_tele_det_day,name='ad_follow_tele_det_day'),

    path('ad_nocall_tele_det/<int:id>', views.ad_nocall_tele_det, name='ad_nocall_tele_det'),
    path('ad_nocall_tele_det_month/<int:id>',views.ad_nocall_tele_det_month,name='ad_nocall_tele_det_month'),
    path('ad_nocall_tele_det_day/<int:id>',views.ad_nocall_tele_det_day,name='ad_nocall_tele_det_day'),
    path('ad_nocall_tele_details/<int:id>/<str:pk>', views.ad_nocall_tele_details, name='ad_nocall_tele_details'),

    path('ad_delay_det',views.ad_delay_det,name='ad_delay_det'),
   
    path('ad_delay_flt',views.ad_delay_flt,name='ad_delay_flt'),
    
    path('ad_waste_data', views.ad_waste_data, name='ad_waste_data'),
    path('ad_waste_data_det/<str:date>/', views.ad_waste_data_det, name='ad_waste_data_det'),
    
    path('ad_view_client>', views.ad_view_client, name='ad_view_client'),
    path('ad_daily_work_head/<int:pk>',views.ad_daily_work_head,name='ad_daily_work_head'),

    #---------------------------------------------------------------------------Executive Section
    path('ex_base', views.ex_base, name='ex_base'),
    path('ex_profile', views.ex_profile, name='ex_profile'),
    path('ex_dashboard', views.ex_dashboard, name='ex_dashboard'), 
    path('ex_daily_work_clint', views.ex_daily_work_clint, name='ex_daily_work_clint'), 
    path('ex_daily_work_det/<int:id>', views.ex_daily_work_det, name='ex_daily_work_det'),
    path('daily_work_done/<int:id>', views.daily_work_done, name='daily_work_done'),
    path('ex_weekly_rep_clint', views.ex_weekly_rep_clint, name='ex_weekly_rep_clint'),
    path('ex_weekly_rep_clint_det/<int:id>', views.ex_weekly_rep_clint_det, name='ex_weekly_rep_clint_det'),
    path('sv_wk_rp/<int:id>', views.sv_wk_rp, name='sv_wk_rp'),
    path('ex_view_work_clint', views.ex_view_work_clint, name='ex_view_work_clint'),
    path('ex_view_clint_det/<int:id>', views.ex_view_clint_det, name='ex_view_clint_det'),  
    path('ex_warning', views.ex_warning, name='ex_warning'),
    path('add_warning/<int:id>', views.add_warning, name='add_warning'),
    path('add_suggestion/<int:id>', views.add_suggestion, name='add_suggestion'),  

    path('ex_warnings_dash', views.ex_warnings_dash, name='ex_warnings_dash'),
    path('ex_suggestions', views.ex_suggestions, name='ex_suggestions'),
    path('ex_change_pass', views.ex_change_pass, name='ex_change_pass'),
    path('ex_accountset', views.ex_accountset, name='ex_accountset'),
    path('ex_imagechange/<int:id>', views.ex_imagechange, name='ex_imagechange'),
    path('get_sub', views.get_sub, name='get_sub'),
    path('corrections', views.corrections, name='corrections'),
    path('add_corrections/<int:id>', views.add_corrections, name='add_corrections'),
    path('get_corrections', views.get_corrections, name='get_corrections'),
    path('ex_schedule_dash', views.ex_schedule_dash, name='ex_schedule_dash'),
    path('ex_calander', views.ex_calander, name='ex_calander'),
    path('ex_all_events', views.ex_all_events, name='ex_all_events'), 
    path('ex_add_event', views.ex_add_event, name='ex_add_event'), 
    path('ex_update', views.ex_update, name='ex_update'),
    path('ex_remove', views.ex_remove, name='ex_remove'),
    path('ex_shedule_work', views.ex_shedule_work, name='ex_shedule_work'),
    path('ex_edit_post_status/<int:id>', views.ex_edit_post_status, name='ex_edit_post_status'),
    path('ex_save_shedule', views.ex_save_shedule, name='ex_save_shedule'),
    path('leave_home', views.leave_home, name='leave_home'),
    path('leave_aply', views.leave_aply, name='leave_aply'),
    path('ex_all_leave', views.ex_all_leave, name='ex_all_leave'),
    path('ex_leave_form', views.ex_leave_form, name='ex_leave_form'),
    path('ad_leave_home', views.ad_leave_home, name='ad_leave_home'),
    path('ad_tl_det', views.ad_tl_det, name='ad_tl_det'),
    path('view_tl_leave/<int:id>', views.view_tl_leave, name='view_tl_leave'),
    path('ex_delay',views.ex_delay,name='ex_delay'),
    path('ex_delay_det_month',views.ex_delay_det_month,name='ex_delay_det_month'),
    path('ex_delay_det_day',views.ex_delay_det_day,name='ex_delay_det_day'),

    path('ex_duplicate_leads',views.duplicate_leads,name='duplicate_leads'),
    path('ex_flt_day_duplicate/',views.ex_flt_day_duplicate,name='ex_flt_day_duplicate'),
    path('ex_flt_month_duplicate/',views.ex_flt_month_duplicate,name='ex_flt_month_duplicate'),
    #---------------marketing head 
    
    path('he_profile', views.he_profile, name='he_profile'),
    path('he_project', views.he_project, name='he_project'),
    path('he_view_works',views.he_view_works,name='he_view_works'),
    path('he_work_asign/<int:pk>',views.he_work_asign,name='he_work_asign'),
    path('he_daily_task',views.he_daily_task,name='he_daily_task'),
    path('he_workprogress_executive',views.he_workprogress_executive,name='he_workprogress_executive'),
    path('he_progress_report/<int:pk>',views.he_progress_report,name='he_progress_report'),
    path('he_feedback',views.he_feedback,name='he_feedback'),
    path('he_feedbacke1/<int:pk>',views.he_feedbacke1,name='he_feedbacke1'),
    path('he_feedback_submit/<int:pk>',views.he_feedback_submit,name='he_feedback_submit'),
    path('he_work_add/<int:id>',views.he_work_add,name='he_work_add'),
    path('he_change_pass',views.he_change_pass,name='he_change_pass'),
    path('he_accountset',views.he_accountset,name='he_accountset'),
    path('he_imagechange/<int:id>',views.he_imagechange,name='he_imagechange'),
    path('he_flt_progress',views.he_flt_progress,name='he_flt_progress'),
    path('he_view_work_asign_client/<int:tlid>',views.he_view_work_asign_client,name='he_view_work_asign_client'),
    path('he_view_work_asign_exe/<int:cid>/<int:tlid>',views.he_view_work_asign_exe,name='he_view_work_asign_exe'),
    path('he_view_post/<int:id>',views.he_view_post,name='he_view_post'),
    path('he_add_correction/<int:id>',views.he_add_correction,name='he_add_correction'),
    path('he_add_status/<int:id>',views.he_add_status,name='he_add_status'),
    path('he_smo_exe',views.he_smo_exe,name='he_smo_exe'),
    path('he_add_event_status/<int:id>',views.he_add_event_status,name='he_add_event_status'),
    path('he_add_correction_daily/<int:id>',views.he_add_correction_daily,name='he_add_correction_daily'),
    path('he_cor_exe',views.he_cor_exe,name='he_cor_exe'),
    path('he_cor_exe_det/<int:id>',views.he_cor_exe_det,name='he_cor_exe_det'),
    
    path('he_leave_home', views.he_leave_home, name='he_leave_home'),
    path('he_leave_aply', views.he_leave_aply, name='he_leave_aply'),
    path('he_all_leave', views.he_all_leave, name='he_all_leave'),
    path('he_leave_form', views.he_leave_form, name='he_leave_form'),
    
    path('he_waste_data', views.he_waste_data, name='he_waste_data'),
    path('he_waste_data_det/<str:date>/', views.he_waste_data_det, name='he_waste_data_det'),
    path('he_executive_home', views.he_executive_home, name='he_executive_home'),
    path('he_view_ex_clients/<int:id>/', views.he_view_ex_clients, name='he_view_ex_clients'),
    path('he_daily_work_det/<int:cid>/<int:eid>/', views.he_daily_work_det, name='he_daily_work_det'),
    path('he_change_status', views.he_change_status, name='he_change_status'),
    path('he_all_leads_exe', views.he_all_leads_exe, name='he_all_leads_exe'),
    path('he_view_exe_det/<int:id>/', views.he_view_exe_det, name='he_view_exe_det'),
    path('he_view_all_leads/<str:date>/<int:id>/', views.he_view_all_leads, name='he_view_all_leads'),
    
    path('he_create_work', views.he_create_work, name='he_create_work'),
    path('he_save_create_work', views.he_save_create_work, name='he_save_create_work'),
    path('he_view_work',views.he_view_work,name='he_view_work'),
    path('he_view_clint/<int:id>', views.he_view_clint, name='he_view_clint'), 
    path('he_update_client/<int:id>', views.he_update_client, name='he_update_client'),
    path('he_daily_work_client',views.he_daily_work_client,name='he_daily_work_client'),
    path('he_daily_work_det/<int:pk>',views.he_daily_work_det,name='he_daily_work_det'),
    path('he_daily_work_done/<int:pk>',views.he_daily_work_done,name='he_daily_work_done'),
    
    path('he_daily_work_details/<int:cid>/<int:eid>/', views.he_daily_work_details, name='he_daily_work_details'),
    
    
    #--------------------------------------------------------------Smo Submission
    
    path('smo_login/<int:id>',views.smo_login,name='smo_login'),
    path('smo_dash',views.smo_dash,name='smo_dash'),
    path('smo_signup/<int:id>',views.smo_signup,name='smo_signup'),
    path('smo_reg/<int:id>',views.smo_reg,name='smo_reg'),
    path('smo_signin/<int:id>',views.smo_signin,name='smo_signin'),
    path('smo_cnt_chnl',views.smo_cnt_chnl,name='smo_cnt_chnl'),
    path('create_post',views.create_post,name='create_post'),
    path('published_post',views.published_post,name='published_post'),
    path('save_post_drft',views.save_post_drft,name='save_post_drft'),
    path('content',views.content,name='content'),
    path('edit_post_drft/<int:id>',views.edit_post_drft,name='edit_post_drft'),    
    path('logout_smo',views.logout_smo,name='logout_smo'),
    path('smo_change_pass',views.smo_change_pass,name='smo_change_pass'),
    path('sm_calendar',views.sm_calendar,name='sm_calendar'),
    path('all_events', views.all_events, name='all_events'), 
    path('add_event', views.add_event, name='add_event'), 
    path('update', views.update, name='update'),
    path('remove', views.remove, name='remove'),
    path('work_shedule_exe', views.work_shedule_exe, name='work_shedule_exe'),
    path('work_shedule/<int:id>', views.work_shedule, name='work_shedule'),

#....................................................<muhammed anas ><datamanager >...............................................................#


    path('dm_dashboard', views.dm_dashboard, name='dm_dashboard'),
    path('view_leads', views.view_leads, name='view_leads'),
    path('view_all_leads/<str:date>/', views.view_all_leads, name='view_all_leads'),
    path('assign', views.assign, name='assign'),
    path('assign_all/<str:date>/', views.assign_all, name='assign_all'),
    path('save_assignment/', views.save_assignment, name='save_assignment'),
    path('assign_count/', views.assign_count, name='assign_count'),
    path('count_all/<str:telecaller>/', views.count_all, name='count_all'),
    path('delete_lead/<int:lead_id>/', views.delete_lead, name='delete_lead'),
    path('dm_profile/', views.dm_profile, name='dm_profile'),
    path('all_counts/', views.all_counts, name='all_counts'),
    path('pending_count/', views.pending_count, name='pending_count'),

# ------------------------------------------------------------------TeleCaller Section

    path('tc_profile', views.tc_profile, name='tc_profile'),
    path('tc_dashboard', views.tc_dashboard, name='tc_dashboard'),
    path('tc_view_leads', views.tc_view_leads, name='tc_view_leads'),
    path('tc_view_current_leads', views.tc_view_current_leads, name='tc_view_current_leads'),
    path('tc_view_previous_leads/<str:dt>/', views.tc_view_previous_leads, name='tc_view_previous_leads'),
    path('tc_update_status', views.tc_update_status, name='tc_update_status'),
    path('tc_update_followup_dt', views.tc_update_followup_dt, name='tc_update_followup_dt'),
    path('tc_view_notifications', views.tc_view_notifications, name='tc_view_notifications'),

    path('tc_accountset', views.tc_accountset, name='tc_accountset'),
    path('tc_imagechange', views.tc_imagechange, name='tc_imagechange'),
    path('tc_change_pass', views.tc_change_pass, name='tc_change_pass'),
    
    path('tc_leave_home', views.tc_leave_home, name='tc_leave_home'),
    path('tc_leave_aply', views.tc_leave_aply, name='tc_leave_aply'),
    path('tc_leave_form', views.tc_leave_form, name='tc_leave_form'),
    path('tc_all_leave', views.tc_all_leave, name='tc_all_leave'),
    


#----------------------------------------------------<Alen Antony> <datamanager>-------------------------------------------------------------
    path('dm_assigned_persons/',views.assigned_persons, name='assigned_persons'),
    path('dm_assigned_person_details/<int:id>/<str:pk>',views.assigned_person_details, name='assigned_person_details'),
    path('get_cust_mail/',views.get_cust_mail, name='get_cust_mail'),
    
    path('dm_accountset', views.dm_accountset, name='dm_accountset'),
    path('dm_imagechange', views.dm_imagechange, name='dm_imagechange'),
    path('dm_change_pass', views.dm_change_pass, name='dm_change_pass'),
    
    path('dm_waste_data', views.dm_waste_data, name='dm_waste_data'),
    path('dm_waste_data_det/<str:date>/', views.dm_waste_data_det, name='dm_waste_data_det'),





#----------------------------------------------------<Alen Antony> <Telecaller>---------------------------------------------------------------

    path('tc_follow/',views.tc_follow,name='tc_follow'),
    path('tc_followup/',views.tc_followup,name='tc_followup'),
    path('tc_followup_det/<str:pk>',views.tc_followup_det,name='tc_followup_det'),
    path('tc_close/',views.tc_close,name='tc_close'),
    path('tc_closed/',views.tc_closed,name='tc_closed'),
    path('tc_flt_day_closed/',views.tc_flt_day_closed,name='tc_flt_day_closed'),
    path('tc_flt_month_closed/',views.tc_flt_month_closed,name='tc_flt_month_closed'),
    path('tc_filter_day_previous_leads', views.tc_filter_day_previous_leads, name='tc_filter_day_previous_leads'),
    path('tc_filter_month_previous_leads', views.tc_filter_month_previous_leads, name='tc_filter_month_previous_leads'),
    path('tc_closed_det/<str:pk>',views.tc_closed_det,name='tc_closed_det'),



#--------------------------------------------------------------------------------------Sumayya--Data manager

    path('dm_telecallers', views.dm_telecallers, name='dm_telecallers'),
    path('dm_filter_day_followup/<int:pk>', views.dm_filter_day_followup, name='dm_filter_day_followup'),
    path('dm_filter_month_followup/<int:pk>', views.dm_filter_month_followup, name='dm_filter_month_followup'),

    path('dm_telecallers_no_calling', views.dm_telecallers_no_calling, name='dm_telecallers_no_calling'),
    path('dm_no_calling/<int:t_id>',views.dm_no_calling,name='dm_no_calling'),
    path('dm_filter_day_no_calling/<int:t_id>', views.dm_filter_day_no_calling, name='dm_filter_day_no_calling'),
    path('dm_filter_month_no_calling/<int:t_id>', views.dm_filter_month_no_calling, name='dm_filter_month_no_calling'),
    path('dm_no_calling_det/<int:t_id>/<str:pk>',views.dm_no_calling_det,name='dm_no_calling_det'),

    

    path('dm_executive_home', views.dm_executive_home, name='dm_executive_home'),
    path('dm_view_ex_clients/<int:id>/', views.dm_view_ex_clients, name='dm_view_ex_clients'),
    path('dm_daily_work_det/<int:cid>/<int:eid>/', views.dm_daily_work_det, name='dm_daily_work_det'),

    path('dm_view_leads_home', views.dm_view_leads_home, name='dm_view_leads_home'),
    path('dm_leads_datewise/<int:eid>/', views.dm_leads_datewise, name='dm_leads_datewise'),
    path('dm_view_all_leads/<int:eid>/<str:date>/', views.dm_view_all_leads, name='dm_view_all_leads'),
    path('dm_filter_status_leads/<int:eid>/<str:date>/', views.dm_filter_status_leads, name='dm_filter_status_leads'),

    path('dm_ad_delay_det', views.dm_ad_delay_det, name='dm_ad_delay_det'),
    path('dm_ad_delay_flt', views.dm_ad_delay_flt, name='dm_ad_delay_flt'),

    path('dm_follow_tele_det/<int:tid>/<str:date>/',views.dm_follow_tele_det,name='dm_follow_tele_det'),
    path('dm_followup_datewise/<int:tid>',views.dm_followup_datewise,name='dm_followup_datewise'),

#-------------------------------------------------------------------------------------------------Sumayya--Telecaller

    path('tc_no_calling', views.tc_no_calling, name='tc_no_calling'),
    path('tc_filter_day_no_calling', views.tc_filter_day_no_calling, name='tc_filter_day_no_calling'),
    path('tc_filter_month_no_calling', views.tc_filter_month_no_calling, name='tc_filter_month_no_calling'),
    path('tc_no_calling_det/<str:pk>', views.tc_no_calling_det, name='tc_no_calling_det'),
    path('tc_previous_leads_datewise', views.tc_previous_leads_datewise, name='tc_previous_leads_datewise'),

#-------------------------------------------------------------------------------------------------Alen Antony--Marketing head
    path('he_delay_det/', views.he_delay_det, name='he_delay_det'),
    path('he_delay_flt/', views.he_delay_flt, name='he_delay_flt'),
    
    path('he_warning_mail/<int:eid>/', views.he_warning_mail, name='he_warning_mail'),
    path('ad_delay_home/', views.ad_delay_home, name='ad_delay_home'),
    path('ad_delay',views.ad_delay,name='ad_delay'),
    path('ad_warning_mail1', views.ad_warning_mail1, name='ad_warning_mail1'),
    path('ad_warning_mail/<int:eid>/', views.ad_warning_mail, name='ad_warning_mail'),
    path('ad_delay_flt', views.ad_delay_flt, name='ad_delay_flt'),
    
    path('ad_delay_fltr', views.ad_delay_fltr, name='ad_delay_fltr'),
    
    #---------------------------------------------------------------------------------------------------Sumayya--Digital Marketing Head
    
    path('he_waste_data_home', views.he_waste_data_home, name='he_waste_data_home'),
    path('he_waste_data_exe', views.he_waste_data_exe, name='he_waste_data_exe'),
    path('he_waste_data_det_exe/<str:date>/', views.he_waste_data_det_exe, name='he_waste_data_det_exe'),
    

#---------------------------------------------------------------------------------------------------Sumayya--Admin

    path('ad_waste_data_home', views.ad_waste_data_home, name='ad_waste_data_home'),
    path('ad_waste_data_exe', views.ad_waste_data_exe, name='ad_waste_data_exe'),
    path('ad_waste_data_det_exe/<str:date>/', views.ad_waste_data_det_exe, name='ad_waste_data_det_exe'),
   

#---------------------------------------------------------------------------------------------------Sumayya--Data manager

    path('dm_waste_data_home', views.dm_waste_data_home, name='dm_waste_data_home'),
    path('dm_waste_data_exe', views.dm_waste_data_exe, name='dm_waste_data_exe'),
    path('dm_waste_data_det_exe/<str:date>/', views.dm_waste_data_det_exe, name='dm_waste_data_det_exe'),

#-----------------------------------------------------------------------------------------------sumayya--tl module--

    path('tl_profile', views.tl_profile, name='tl_profile'),
    path('tl_project', views.tl_project, name='tl_project'),
    path('tl_view_works',views.tl_view_works,name='tl_view_works'),
    path('tl_work_asign/<int:pk>',views.tl_work_asign,name='tl_work_asign'),
    path('tl_work_add/<int:id>',views.tl_work_add,name='tl_work_add'),
    path('tl_view_work_asign_client',views.tl_view_work_asign_client,name='tl_view_work_asign_client'),
    path('tl_view_work_asign_exe/<int:id>',views.tl_view_work_asign_exe,name='tl_view_work_asign_exe'),
    path('tl_daily_task',views.tl_daily_task,name='tl_daily_task'),
    path('tl_add_correction_daily/<int:id>',views.tl_add_correction_daily,name='tl_add_correction_daily'),
    path('tl_add_status/<int:id>',views.tl_add_status,name='tl_add_status'),
    path('tl_export_excel/<int:id>',views.tl_export_excel,name='tl_export_excel'),

    path('tl_workprogress_home',views.tl_workprogress_home,name='tl_workprogress_home'),
    path('tl_workprogress_executive',views.tl_workprogress_executive,name='tl_workprogress_executive'),
    path('tl_progress_report/<int:pk>',views.tl_progress_report,name='tl_progress_report'),
    path('tl_flt_progress', views.tl_flt_progress, name='tl_flt_progress'),
    path('tl_workprogress_monthly',views.tl_workprogress_monthly,name='tl_workprogress_monthly'),
    path('tl_progress_report_monthly/<int:pk>',views.tl_progress_report_monthly,name='tl_progress_report_monthly'),
    path('tl_flt_progress_monthly', views.tl_flt_progress_monthly, name='tl_flt_progress_monthly'),
    path('tl_smo_exe', views.tl_smo_exe, name='tl_smo_exe'),
    path('tl_view_post/<int:id>',views.tl_view_post,name='tl_view_post'),
    path('tl_add_correction/<int:id>',views.tl_add_correction,name='tl_add_correction'),
    path('tl_add_event_status/<int:id>',views.tl_add_event_status,name='tl_add_event_status'),
    path('tl_cor_exe', views.tl_cor_exe, name='tl_cor_exe'),
    path('tl_cor_exe_det/<int:id>',views.tl_cor_exe_det,name='tl_cor_exe_det'),
    path('tl_all_leads_exe', views.tl_all_leads_exe, name='tl_all_leads_exe'),
    path('tl_view_exe_det/<int:id>',views.tl_view_exe_det,name='tl_view_exe_det'),
    path('tl_view_all_leads/<str:date>/<int:id>/',views.tl_view_all_leads,name='tl_view_all_leads'),
    path('tl_executive_home', views.tl_executive_home, name='tl_executive_home'),
    path('tl_view_ex_clients/<int:id>',views.tl_view_ex_clients,name='tl_view_ex_clients'),
    path('tl_daily_work_details/<int:cid>/<int:eid>/', views.tl_daily_work_details, name='tl_daily_work_details'),
    path('tl_change_status', views.tl_change_status, name='tl_change_status'),
    path('tl_feedback', views.tl_feedback, name='tl_feedback'),
    path('tl_feedbacke1/<int:pk>',views.tl_feedbacke1,name='tl_feedbacke1'),
    path('tl_feedback_submit/<int:pk>',views.tl_feedback_submit,name='tl_feedback_submit'),
    path('tl_delay_det/', views.tl_delay_det, name='tl_delay_det'),
    path('tl_delay_flt/', views.tl_delay_flt, name='tl_delay_flt'),
    path('tl_warning_mail/<int:eid>/', views.tl_warning_mail, name='tl_warning_mail'),
    path('tl_waste_data_home', views.tl_waste_data_home, name='tl_waste_data_home'),
    path('tl_waste_data_exe', views.tl_waste_data_exe, name='tl_waste_data_exe'),
    path('tl_waste_data_det_exe/<str:date>/', views.tl_waste_data_det_exe, name='tl_waste_data_det_exe'),
    path('tl_waste_data', views.tl_waste_data, name='tl_waste_data'),
    path('tl_waste_data_det/<str:date>/', views.tl_waste_data_det, name='tl_waste_data_det'),
    path('tl_all_leave', views.tl_all_leave, name='tl_all_leave'),
    path('tl_leave_form', views.tl_leave_form, name='tl_leave_form'),
    path('tl_leave_home', views.tl_leave_home, name='tl_leave_home'),
    path('tl_leave_aply', views.tl_leave_aply, name='tl_leave_aply'),
    path('tl_exe_smopost', views.tl_exe_smopost, name='tl_exe_smopost'),
    path('tl_sv_smopost/<int:id>',views.tl_sv_smopost,name='tl_sv_smopost'),

#-----------------------------------------------------------------------------------------------sumayya--dm head--

    path('he_assign_tl', views.he_assign_tl, name='he_assign_tl'),
    path('he_assign_tl1', views.he_assign_tl1, name='he_assign_tl1'),
    path('he_view_work_asign_tl', views.he_view_work_asign_tl, name='he_view_work_asign_tl'),

    
    
    
    re_path(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}),


]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
