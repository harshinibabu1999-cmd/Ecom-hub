from django.urls import path
from . import views

urlpatterns = [



    path('', views.admin_login_view, name='admin_login_view'),

    path('home/', views.admin_home, name='home'),

    path('admin-dashboard/', views.admin_dashboard, name='admin_dashboard'),

    path('logout/', views.admin_logout_view, name='logout_view'),



    path('register/', views.admin_register_view, name='admin_register_view'),
    path('add-project/', views.admin_add_project, name='admin_add_project'),
    path('delete-project/<int:pk>/', views.admin_delete_project, name='admin_delete_project'),
    path('edit-project/<int:pk>/', views.admin_edit_project, name='admin_edit_project'),
    path('admin-payment_history/', views.admin_payment_history, name='admin_payment_history'),
    path('delete-user/<int:user_id>/', views.admin_delete_user, name='admin_delete_user'),
    path('upload-project/', views.admin_upload_project, name='upload_project'),
    path('projects/', views.admin_project_list, name='admin_project_list'),
    path('student/<int:pk>', views.admin_student_details, name='admin_student_details'),
    path('projects/', views.admin_projects, name='admin_projects'),
    path('upload-project/', views.admin_upload_project, name='admin_upload_project'),
    path('students/', views.admin_student_list, name='admin_student_list'),
    path('admin-project/<int:pk>/', views.admin_project_detail, name='admin_project_detail'),
    path('delete-student/<int:id>/', views.admin_delete_student, name='admin_delete_student'),
    path('view-projects/', views.admin_view_project, name='admin_view_project'),
    path('payment-details/<int:id>/', views.admin_payment_details, name='admin_payment_details'),
    









    path('projects/',views.user_project_list,name='user_project_list'),
    path('projects/<int:pk>/', views.project_detail, name='project_detail'),
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    path('student-register/',views.student_register,name='student_register'),
    path('payment-details/',views.payment_details,name='payment_details'),
    path('user-home/',views.user_home,name='user_home'),
    path("user_view-projects/", views.user_project_list, name="user_project_list"),
    path('projects/<int:pk>/', views.project_detail, name='project_detail'),
    path('student-register/',views.student_register,name='student_register'),
    path('buy/<int:pk>/', views.initiate_payment, name='initiate_payment'),
    path('payment/<int:pk>/', views.user_payment_page, name='user_payment_page'),
    path('payment-form/<int:pk>/', views.payment_form, name='payment_form'),
    path('payment-success/<int:pk>/', views.payment_success, name='payment_success'),
    path('purchased-projects/', views.purchased_projects, name='purchased_projects'),
    path('download-project/<int:pk>/', views.download_project, name='download_project'),
    path('payment-success/<str:transaction_id>/', views.payment_success, name='payment_success'),
    path('payment-process/', views.payment_process, name='payment_process'),
    path('phonepe-pay/<int:pk>/', views.phonepe_payment, name='phonepe_pay'),
   
]   


