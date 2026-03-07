import base64
import hashlib
import json
import uuid
from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from .user_side import *
from django.conf import settings
from .models import Project, Payment
from django.contrib.auth.decorators import login_required
from .models import CustomUser


@login_required
def student_register(request):

    if request.method == "POST":

        phone_number = request.POST.get("phone_number")
        college_name = request.POST.get("college_name")
        year_of_study = request.POST.get("year_of_study")


        request.user.phone_number = phone_number
        request.user.college_name = college_name
        request.user.year_of_study = year_of_study
        request.user.is_student_registered = True
        request.user.save()

        return redirect("user_home")

    return render(request, "user/student_register.html")

@login_required
def user_project_list(request):
    projects = Project.objects.all()
    return render(request, "user/user_project_list.html", {"projects": projects})

def project_detail(request, id):
    project = project.objects.get(id=id)
    return render(request, 'user/project_detail.html', {'project': project})


@login_required
def payment_details(request):

    payments = Payment.objects.filter(user=request.user).order_by('-created_at')

    return render(request, "user/payment_details.html", {"payments": payments})

@login_required
def user_home(request):

    if not request.user.is_student_registered:
        return redirect("student_register")

    return render(request,"user/user_home.html")