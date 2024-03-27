from django.contrib import admin
from app import views
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .import Hod_views,staff_views,Student_views

urlpatterns = [
   path('base',views.base, name='base'), 
   #login path
   path('',views.LOGIN, name='login' ),#login path
   path('doLogin',views.doLogin, name='doLogin'),
   path('doLogout',views.doLogout, name='logout'),
   #profile update
   path('profile',views.PROFILE,name='profile'),
   path('profile/update',views.PROFILE_UPDATE ,name='profile_update'),
   #for Hod panel url
   path('HOD/home',Hod_views.Home, name='Hod_home'),
   path('Hod/Student/Add',Hod_views.ADD_STUDENT,name='add_student'),
   path('Hod/Student/View',Hod_views.VIEW_STUDENT,name='view_student'),
   path('Hod/Student/Edit/<str:id>',Hod_views.EDIT_STUDENT,name='edit_student'),
   path('Hod/Student/Update',Hod_views.UPDATE_STUDENT,name='update_student'),
   path('Hod/Student/Delete/<str:admin>',Hod_views.DELETE_STUDENT,name='delete_student'),

   path('Hod/Staff/Add',Hod_views.ADD_STAFF,name='add_staff'),
   path('Hod/Staff/View',Hod_views.VIEW_STAFF,name='view_staff'),
   path('Hod/Staff/Edit/<str:id>',Hod_views.EDIT_STAFF,name='edit_staff'),
   path('Hod/Staff/Update',Hod_views.UPDATE_STAFF,name='update_staff'),
   path('Hod/Staff/Delete/<str:admin>',Hod_views.DELETE_STAFF,name='delete_staff'),


   path('Hod/Course/Add',Hod_views.ADD_COURSE,name='add_course'),
   path('Hod/Course/view',Hod_views.VIEW_COURSE,name='view_course'),
   path('Hod/Course/Edit/<str:id>',Hod_views.EDIT_COURSE,name='edit_course'),
   path('Hod/Course/Update',Hod_views.UPDATE_COURSE,name='update_course'),
   path('Hod/Course/Delete/<str:id>',Hod_views.DELETE_COURSE,name='delete_course'),


   path('Hod/Subject/Add',Hod_views.ADD_SUBJECT,name='add_subject'),
   path('Hod/Subject/View',Hod_views.VIEW_SUBJECT,name='view_subject'),
   path('Hod/Subject/Update',Hod_views.UPDATE_SUBJECT,name='update_subject'),
   path('Hod/Subject/Edit/<str:id>',Hod_views.EDIT_SUBJECT,name='edit_subject'),
   path('Hod/Subject/Delete/<str:id>',Hod_views.DELETE_SUBJECT,name='delete_subject'),

   path('Hod/Session/Add',Hod_views.ADD_SESSION,name='add_session'),
   path('Hod/Session/View',Hod_views.VIEW_SESSION,name='view_session'),
   path('Hod/Session/Edit/<str:id>',Hod_views.EDIT_SESSION,name='edit_session'),
   path('Hod/Session/Update',Hod_views.UPDATE_SESSION,name='update_session'),
   path('Hod/Session/Delete/<str:id>',Hod_views.DELETE_SESSION,name='delete_session'),

   path('Hod/Staff/Send_Notification',Hod_views.STAFF_SEND_NOTIFICATION,name='staff_send_notification'),
   path('Hod/Staff/Save_Notification',Hod_views.SAVE_STAFF_NOTIFICATION,name='save_staff_notification'),
   path('Hod/Student/Send_Notification',Hod_views.STUDENT_SEND_NOTIFICATION,name='student_send_notification'),
   path('Hod/Student/save_Notification',Hod_views.SAVE_STUDENT_NOTIFICATION,name='save_student_notification'),

  
   path('Hod/Staff/Leave_view',Hod_views.STAFF_LEAVE_VIEW,name='staff_leave_view'),
   path('Hod/Staff/approve_leave/<str:id>',Hod_views.STAFF_APPROVE_LEAVE,name='staff_approve_leave'),
   path('Hod/Staff/disapprove_leave/<str:id>',Hod_views.STAFF_DISAPPROVE_LEAVE,name='staff_disapprove_leave'),
   path('Hod/Student/Leave_view',Hod_views.STUDENT_LEAVE_VIEW,name='student_leave_view'),
   path('Hod/Student/approve_leave/<str:id>',Hod_views.STUDENT_APPROVE_LEAVE,name='student_approve_leave'),
   path('Hod/Student/disapprove_leave/<str:id>',Hod_views.STUDENT_DISAPPROVE_LEAVE,name='student_disapprove_leave'),
   

   path('Hod/Staff/feedback',Hod_views.STAFF_FEEDBACK,name='staff_feedback_replay'),
   path('Hod/Staff/feeback_save',Hod_views.STAFF_FEEDBACK_SAVE,name='staff_feedback_replay_save'),
   path('Hod/Student/feedback',Hod_views.STUDENT_FEEDBACK,name='get_feedback_replay'),
   path('Hod/Student/feeback_save',Hod_views.STUDENT_FEEDBACK_SAVE,name='student_feedback_replay_save'),

   path('Hod/View_attendance',Hod_views.VIEW_ATTENDANCE,name='view_attendance'),
  


#This is staff urls

   path('Staff/Home',staff_views.HOME,name='staff_home'),
   path('Staff/Notifications',staff_views.NOTIFICATIONS,name='notifications'),
   path('Staff/mark_as_done/<str:status>',staff_views.MARK_AS_DONE,name='staff_notification_mark_as_done'),
   path('Staff/Applay_leave',staff_views.STAFF_APPLAY_LEAVE,name='staff_applay_leave'),
   path('Staff/Applay_leave_save',staff_views.STAFF_APPLAY_LEAVE_SAVE,name='staff_applay_leave_save'),
   path('Staff/Feedback',staff_views.STAFF_FEEDBACK,name='staff_feedback'),
   path('Staff/Feedback/Save',staff_views.STAFF_FEEDBACK_SAVE,name='staff_feedback_save'),
   path('Staff/Take_Attendance',staff_views.STAFF_TAKE_ATTENDANCE,name='staff_take_attendance'),
   path('Staff/Save_Attendance',staff_views.STAFF_SAVE_ATTENDANCE,name='staff_save_attendance'),
   
   path('Staff/View_Attendance',staff_views.STAFF_VIEW_ATTENDANCE,name='staff_view_attendance'),

   path('Staff/Add/Result',staff_views.STAFF_ADD_RESULT,name='staff_add_result'),
   path('Staff/Save/Result',staff_views.STAFF_SAVE_RESULT,name='staff_save_result'),


#This is student urls
   path('Student/Home',Student_views.HOME,name='student_home'),
   path('Student/Notifications',Student_views.STUDENT_NOTIFICATIONS,name='student_notifications'),
   path('Student/mark_as_done/<str:status>',Student_views.STUDENT_NOTIFICATION_MARK_AS_DONE,name='student_notification_mark_as_done'),
   path('Student/Feedback',Student_views.STUDENT_FEEDBACK,name='student_feedback'),
   path('Student/Feedback/Save',Student_views.STUDENT_FEEDBACK_SAVE,name='student_feedback_save'),
   path('Student/applay_for_leave',Student_views.STUDENT_LEAVE,name='student_leave'),
   path('Student/Leave_save',Student_views.STUDENT_LEAVE_SAVE,name='student_leave_save'),
   path('Student/View_Attendance',Student_views.STUDENT_VIEW_ATTENDANCE,name='student_view_attendance'),
   path('Student/View_Result',Student_views.VIEW_RESULT,name='view_result'),



] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

