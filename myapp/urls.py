
from django.contrib import admin
from django.urls import path, include

from myapp import views

urlpatterns = [
    path('login/', views.login),
    path('login_post/', views.login_post),
    path('logout/', views.logout),
    path('admin_home/', views.home),
    path('admin_change_password/', views.admin_change_password),
    path('admin_change_password_post/', views.admin_change_password_post),
    path('add_skill/', views.add_skill),
    path('add_skill_post/', views.add_skill_post),
    path('view_skill/', views.view_skill),
    path('view_skill_post/', views.view_skill_post),
    path('category/', views.category),
    path('category_post/', views.category_post),
    path('view_category/', views.view_category),
    path('view_category_post/', views.view_category_post),
    path('edit_category_post/', views.edit_category_post),
    path('edit_category/<id>', views.edit_category),
    path('delete_category/<id>', views.delete_category),
    path('edit_skill/<id>', views.edit_skill),
    path('edit_skill_post/', views.edit_skill_post),
    path('delete_skill/<id>/', views.delete_skill),

    path('view_Company/',views.view_Company),
    path('view_Company_post/',views.view_Company_post),
    path('view_aproved_Comapany_post/',views.view_aproved_Comapany_post),
    path('view_aproved_Comapany/',views.view_aproved_Comapany),
    path('view_rejected_Comapany/',views.view_rejected_Comapany),
    path('view_rejected_Comapany_post/',views.view_rejected_Comapany_post),
    path('aproving_company/<id>',views.aproving_company),
    path('reject_company/<id>',views.reject_company),
    path('send_reply_post/',views.send_reply_post),
    path('send_reply/<id>',views.send_reply),
    path('view_complaint_post/',views.view_complaint_post),
    path('view_complaint/',views.view_complaint),
    path('view_review/',views.view_review),
    path('view_review_post/',views.view_review_post),
    path('view_user/',views.view_user),
    path('view_user_post/',views.view_user_post),




#     company

    path('company/',views.company),
    path('company_post/',views.company_post),
    path('company_home/',views.company_home),
    path('company_change_password/',views.company_change_password),
    path('company_change_password_post/',views.company_change_password_post),
    path('company_profile/',views.company_profile),
    path('edit_company/<id>',views.edit_company),
    path('edit_company_post/',views.edit_company_post),
    path('add_jobs/',views.add_jobs),
    path('add_jobs_post/',views.add_jobs_post),
    path('view_jobs/',views.view_jobs),
    path('view_jobs_post/',views.view_jobs_post),
    path('delete_job/<id>',views.delete_job),
    path('edit_jobs/<id>',views.edit_jobs),
    path('edit_jobs_post/',views.edit_jobs_post),
    path('add_job_skill/',views.add_job_skill),
    path('add_job_skill_post/',views.add_job_skill_post),
    path('view_jobs_skill/',views.view_jobs_skill),
    path('view_jobs_skill_post/',views.view_jobs_skill_post),
    path('delete_jobskill/<id>',views.delete_jobskill),
    path('edit_jobskill/<id>',views.edit_jobskill),
    path('edit_jobskill_post/',views.edit_jobskill_post),
    path('view_job_review/',views.view_job_review),
    path('view_job_review_post/',views.view_job_review_post),
    path('view_job_application/',views.view_job_application),
    path('view_job_application_post/',views.view_job_application_post),
    path('view_confirmed_job_application/',views.view_confirmed_job_application),
    path('view_confirmed_job_application_post/',views.view_confirmed_job_application_post),
    path('view_rejected_job_application_post/',views.view_rejected_job_application_post),
    path('view_rejected_job_application/',views.view_rejected_job_application),
    path('confirm_application/<id>',views.confirm_application),
    path('reject_application/<id>',views.reject_application),




#     user
    path('login2/',views.login2),
    path('user_post_new/',views.user_post_new),
    path('user_profile_new/',views.user_profile_new),
    path('user_profile_new/',views.user_profile_new),
    path('edit_userprofile/',views.edit_userprofile),
    path('user_view_complaints/',views.user_view_complaints),
    path('user_complaint_post/',views.user_complaint_post),
    path('user_changepassword/',views.user_changepassword),
    path('user_review_post/',views.user_review_post),
    path('user_view_application/',views.user_view_application),
    path('user_view_jobs/',views.user_view_jobs),
    path('user_view_company/',views.user_view_company),
    path('user_experience_post/',views.user_experience_post),
    path('view_experience/',views.view_experience),
    path('user_qualification_post/',views.user_qualification_post),
    path('user_view_qualification/',views.user_view_qualification),
    path('user_addskills/',views.user_addskills),
    path('user_ViewSkills/',views.user_ViewSkills),
    path('user_ViewMySkills/',views.user_ViewMySkills),
    path('user_deleteskills/',views.user_deleteskills),

    path('user_view_own_qualification/',views.user_view_own_qualification),
    path('delete_qualification/',views.delete_qualification),

    path('user_qualification_edit_post/',views.user_qualification_edit_post),
    path('view_user_edit_experience/',views.view_user_edit_experience),
    path('user_edit_experience_post/',views.user_edit_experience_post),

    path('delete_experience/',views.delete_experience),

    path('add_refference/',views.add_refference),
    path('user_view_own_refference/',views.user_view_own_refference),

    path('user_edit_reffernce/',views.user_edit_reffernce),
    path('user_edit_refference_post/',views.user_edit_refference_post),
    path('delete_refference/',views.delete_refference),
    path('sent_job_review1/',views.sent_job_review1),


    path('user_view_select_jobs/',views.user_view_select_jobs),
    path('user_apply_post/',views.user_apply_post),
    path('admin_view_jobs/<id>',views.admin_view_jobs),
    path('company_view_jobs_skill/<id>',views.company_view_jobs_skill),



]
