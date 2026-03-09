from django.urls import path
from . import views

urlpatterns = [
    path('', views.admin_login_view, name='login_view'),
    path('home/', views.admin_home, name='home'),
    path('admin-dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('logout/', views.admin_logout_view, name='logout_view'),
    path('register/', views.admin_register_view, name='register_view'),
    path('add-project/', views.admin_add_project, name='add_project'),
    path('delete-project/<int:id>/', views.admin_delete_project, name='delete_project'),
    path('edit-project/<int:id>/', views.admin_edit_project, name='edit_project'),
    path('payment_page/', views.payment_page, name='payment_page'),
    path('block-user/<int:id>/', views.admin_block_user, name='block_user'),
    path('delete-user/<int:user_id>/', views.admin_delete_user, name='delete_user'),
    path('upload-project/', views.admin_upload_project, name='upload_project'),
    path('projects/', views.admin_project_list, name='project_list'),
    path('student/', views.admin_student_details, name='student_details'),
    path('project/', views.admin_project, name='project'),

    path('upload-project/', views.admin_upload_project, name='upload_project'),
    path('projects/', views.admin_project_list, name='project_list'),
    path('student/<int:id>/', views.admin_student_details, name='student_details'),
    path('project/', views.admin_project, name='project'),
    path('students/', views.admin_student_list, name='student_list'),

    









    path('projects/',views.user_project_list,name='user_project_list'),
    path('projects/<int:pk>/', views.project_detail, name='project_detail'),
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    path('student-register/',views.student_register,name='student_register'),
    path('payment-details/',views.payment_details,name='payment_details'),
    path('user-home/',views.user_home,name='user_home'),
    path("view-projects/", views.user_project_list, name="user_project_list"),
    path('projects/',views.user_project_list,name='user_project_list'),
    path('projects/<int:pk>/', views.project_detail, name='project_detail'),
    path('student-register/',views.student_register,name='student_register'),
    
    

]

