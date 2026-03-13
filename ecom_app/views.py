from datetime import datetime

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout, get_user_model
from django.contrib.auth.decorators import login_required
from .models import *
from .user_side import *
from .models import CustomUser, Project, Payment
from django.shortcuts import render, redirect
from .forms import ProjectForm
from django.db.models import Sum
from django.shortcuts import get_object_or_404




from django.contrib.auth import get_user_model


User = get_user_model()

def admin_login_view(request):

    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)

            if user.is_superuser:
                return redirect("admin_dashboard")

            else:
                if not user.is_student_registered:
                    return redirect("student_register")
                else:
                    return redirect("user_home")

        else:
            return render(request, "store/admin_login.html", {"error": "Invalid username or password"})

    return render(request, "store/admin_login.html")


def admin_register_view(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        role = request.POST.get('role')

        phone_number = request.POST.get('phone_number')
        college_name = request.POST.get('college_name')
        department = request.POST.get('department')
        year_of_study = request.POST.get('year_of_study')
        address = request.POST.get('address')

        if password != confirm_password:
            return render(request, 'store/admin_register.html', {'error': 'Passwords do not match'})

        if User.objects.filter(username=username).exists():
            return render(request, 'store/admin_register.html', {'error': 'Username already exists'})

        if User.objects.filter(email=email).exists():
            return render(request, 'store/admin_register.html', {'error': 'Email already exists'})

        user = CustomUser.objects.create_user(
            username=username,
            email=email,
            password=password,
            role=role,
            phone_number=phone_number,
            college_name=college_name,
            department=department,
            year_of_study=year_of_study,
            address=address
        )

        user.save()

        return redirect('login_view')

    return render(request, 'store/admin_register.html')





# ---------------- ADMIN HOME ----------------
@login_required
def admin_home(request):
    projects = Project.objects.all()
    return render(request, 'store/admin_home.html', {'projects': projects})


# ---------------- LOGOUT ----------------
def admin_logout_view(request):
    logout(request)
    return redirect('login_view')


from datetime import datetime


@login_required
def admin_dashboard(request):
    total_students = CustomUser.objects.filter(is_superuser=False).count()
    total_projects = Project.objects.count()
    total_sales = Payment.objects.count()
    monthly_revenue = Payment.objects.aggregate(total=Sum('amount'))['total'] or 0
    today = datetime.now().date()
    today_students = CustomUser.objects.filter(date_joined__date=today, is_superuser=False)
    context = {
        'total_students': total_students,
        'total_projects': total_projects,
        'total_sales': total_sales,
        'monthly_revenue': monthly_revenue,
        'recent_students': today_students[:5],  # Show only the 5 most recent students
        'today_students': today_students
    }

    return render(request, 'store/admin_dashboard.html', context)


# ---------------- ADD PROJECT ----------------
@login_required
def admin_add_project(request):

    if request.method == "POST":
        Project.objects.create(
            title=request.POST.get("title"),
            description=request.POST.get("description"),
            category=request.POST.get("category"),
            price=request.POST.get("price"),
            google_drive_link=request.POST.get("drive_link"),
            project_image=request.FILES.get("image"),
        )
        return redirect("admin_project_list")

    return render(request, "store/admin_add_project.html")


# ---------------- EDIT PROJECT ----------------
@login_required
def admin_edit_project(request, id):
    project = get_object_or_404(Project, id=id)

    if request.method == "POST":
        project.title = request.POST.get("title")
        project.description = request.POST.get("description")
        project.category = request.POST.get("category")
        project.price = request.POST.get("price")

        if request.FILES.get("image"):
            project.project_image = request.FILES.get("image")

        project.save()
        return redirect("admin_project_list")

    return render(request, "store/admin_edit_project.html", {"project": project})


# ---------------- DELETE PROJECT ----------------
@login_required
def admin_delete_project(request, id):
    project = get_object_or_404(Project, id=id)
    project.delete()
    return redirect("admin_project_list")


# ---------------- PROJECT LIST ----------------
@login_required
def admin_project_list(request):
    projects = Project.objects.all().order_by('-created_at')
    return render(request, 'store/admin_project_list.html', {'projects': projects})



@login_required
def admin_project_detail(request, id):
    project = get_object_or_404(Project, id=id)
    return render(request, "store/admin_project_detail.html", {"project": project})


@login_required
def admin_delete_student(request, id):
    user = get_object_or_404(User, id=id)
    user.delete()
    return redirect('student_list')



@login_required
def admin_student_list(request):
    students = CustomUser.objects.filter(is_superuser=False)
    return render(request, 'store/admin_student_list.html', {'students': students})


@login_required
def admin_student_details(request, id):
    student = get_object_or_404(CustomUser, id=id)
    return render(request, 'store/admin_student_details.html', {'student': student})


@login_required
def admin_view_project(request):
    projects = Project.objects.all()
    return render(request, 'store/admin_view_project.html', {'projects': projects})




@login_required
def admin_upload_project(request):

    if request.method == "POST":
        form = ProjectForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return redirect('admin_project_list')

    else:
        form = ProjectForm()

    return render(request, 'store/admin_upload_project.html', {'form': form})


@login_required
def admin_payment_history(request):
    payments = Payment.objects.select_related('user', 'project').order_by('-created_at')

    context = {
        'payments': payments
    }

    return render(request, 'store/admin_payment_history.html', context)


@login_required
def payment_details(request, id):
    if id is None:
        from django.http import HttpResponse
        return HttpResponse("No ID was provided in the URL!")
    payment = get_object_or_404(Payment, id=id)
    return render(request, 'store/admin_payment_details.html', {'payment': payment})