import base64
import hashlib
import json
import uuid
import requests
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

def user_project_list(request):
    projects = Project.objects.all()
    return render(request, "user/user_project_list.html", {"projects": projects})


@login_required
def payment_details(request):

    payments = Payment.objects.filter(user=request.user).order_by('-created_at')

    return render(request, "user/payment_details.html", {"payments": payments})



@login_required
def user_home(request):

    if not request.user.is_student_registered:
        return redirect("student_register")

    return render(request,"user/user_home.html")

@login_required
def initiate_payment(request, pk):

    project = get_object_or_404(Project, pk=pk)

    transaction_id = str(uuid.uuid4())

    payment = Payment.objects.create(
        user=request.user,
        project=project,
        transaction_id=transaction_id,
        amount=project.price,
        status='PENDING',
        payment_mode='UPI'
    )

    return redirect('user_payment_page', pk=payment.id)

def user_payment_page(request, pk):

    payment = get_object_or_404(Payment, id=pk)

    return render(request, 'user/user_payment_page.html', {'payment': payment})


def payment_form(request, pk):
    payment = get_object_or_404(Payment, id=pk)

    if request.method == "POST":
        payment.status = "SUCCESS"
        payment.payment_mode = request.POST.get("payment_method")
        payment.save()

        return redirect("payment_success", pk=payment.id)

    return render(request, "user/payment_form.html", {"payment": payment})

def payment_success(request, pk):
    payment = get_object_or_404(Payment, id=pk)

    return render(request, "user/payment_success.html", {"payment": payment})


@login_required
def purchased_projects(request):
    payments = Payment.objects.filter(user=request.user, status="SUCCESS")

    return render(request, "user/purchased_projects.html", {"payments": payments})

def project_detail(request, pk):
    project = get_object_or_404(Project, pk=pk)
    return render(request, 'user/project_detail.html', {'project': project})

def download_project(request, pk):

    project = get_object_or_404(Project, pk=pk)

    return render(request, "user/download_project.html", {
        "project": project
    })