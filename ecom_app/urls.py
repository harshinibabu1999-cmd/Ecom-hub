from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_view, name='login_view'),
    path('home/', views.home, name='home'),
    path('admin-dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('logout/', views.logout_view, name='logout_view'),
    path('register/', views.register_view, name='register_view'),
    path('add-project/', views.add_project, name='add_project'),
    path('delete-project/<int:id>/', views.delete_project, name='delete_project'),
    path('edit-project/<int:id>/', views.edit_project, name='edit_project'),
    path('payment_page/', views.payment_page, name='payment_page'),
    path('block-user/<int:id>/', views.block_user, name='block_user'),
    path('delete-user/<int:user_id>/', views.delete_user, name='delete_user'),
    path('upload-project/', views.upload_project, name='upload_project'),
    path('projects/', views.project_list, name='project_list'),
    path('student/', views.student_details, name='student_details'),
    path('project/', views.project, name='project'),

    path('upload-project/', views.upload_project, name='upload_project'),
    path('projects/', views.project_list, name='project_list'),
    path('student/<int:id>/ ', views.student_details, name='student_details'),
    path('project/<int:pk>/', views.project, name='project'),
    path('students/', views.student_list, name='student_list'),

    









    path('projects/',views.user_project_list,name='user_project_list'),
    path('projects/<int:pk>/', views.project_detail, name='project_detail'),
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    path('student-register/',views.student_register,name='student_register'),
    path('payment-details/',views.payment_details,name='payment_details'),
    path('user-home/',views.user_home,name='user_home'),
    path("view-projects/", views.user_project_list, name="user_project_list"),
    path('user/projects/',views.user_project_list,name='user_project_list'),
    path('projects/<int:pk>/', views.project_detail, name='project_detail'),
    path('student-register/',views.student_register,name='student_register'),
    path('projects/<int:pk>/', views.project_detail, name='project_detail'),
    path('buy/<int:pk>/', views.initiate_payment, name='initiate_payment'),
    path('payment/<int:pk>/', views.user_payment_page, name='user_payment_page'),
    path('payment-form/<int:pk>/', views.payment_form, name='payment_form'),
    path('payment-success/<int:pk>/', views.payment_success, name='payment_success'),
    path('purchased-projects/', views.purchased_projects, name='purchased_projects'),
]

