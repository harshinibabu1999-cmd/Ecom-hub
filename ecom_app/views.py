from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout, get_user_model
from django.contrib.auth.decorators import login_required
from .models import *
from .user_side import *
from .models import CustomUser, Project, Payment
from django.shortcuts import render, redirect
from .forms import ProjectForm



User = get_user_model()


from django.contrib.auth import get_user_model

User = get_user_model()

from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
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
                    return redirect("admin_student_register")
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

        return redirect('admin_login_view')

    return render(request, 'store/admin_register.html')



@login_required

def admin_home(request):
    projects = Project.objects.all()
    return render(request, 'store/admin_home.html', {
        'projects': projects
    })


# ---------------- LOGOUT ----------------
def admin_logout_view(request):
    logout(request)
    return redirect('admin_login_view')










@login_required
def admin_dashboard(request):
   projects = Project.objects.all()
   return render(request, 'store/admin_dashboard.html', {
       'projects': projects
   })





def admin_add_project(request):
    if request.method == "POST":
        Project.objects.create(
            name=request.POST['name'],
            description=request.POST['description'],
            price=request.POST['price'],
            drive_link=request.POST['drive_link'],
            thumbnail=request.FILES['thumbnail']
        )
        return redirect('admin_dashboard')

    return render(request, 'admin_add_project.html')


@login_required
def admin_edit_project(request, id):
    project = get_object_or_404(Project, id=id)

    if request.method == "POST":
        project.title = request.POST.get("title")
        project.description = request.POST.get("description")
        project.category = request.POST.get("category")
        project.price = request.POST.get("price")
        project.drive_link = request.POST.get("drive_link")

        if request.FILES.get("image"):
            project.image = request.FILES.get("image")

        project.save()
        return redirect("project")

    return render(request, "store/admin_edit_project.html", {"project": project})


@login_required
def admin_delete_project(request, id):
    project = get_object_or_404(Project, id=id)
    project.delete()
    return redirect("admin_project")

@login_required
def admin_block_user(request, id):
    user = get_object_or_404(User, id=id)
    user.is_active = False
    user.save()
    return redirect("admin_view_students")

# @login_required
def admin_delete_user(request, user_id):
    user = get_object_or_404(User, id=user_id)
    user.delete()
    # This string MUST match the 'name' in urls.py
    return redirect('admin_view_students')

@login_required
def admin_add_project(request):
    if not request.user.is_superuser:
        return redirect("login")

    if request.method == "POST":
        Project.objects.create(
            title=request.POST.get("title"),
            description=request.POST.get("description"),
            category=request.POST.get("category"),
            price=request.POST.get("price"),
            google_drive_link=request.POST.get("drive_link"),
            project_image=request.FILES.get("image"),
        )
        return redirect("project")

    return render(request, "store/admin_add_project.html")

@login_required
def admin_view_students(request):
    if not request.user.is_superuser:
        return redirect("login")

    students = StudentProfile.objects.select_related("user")

    return render(request, "store/admin_students_detail.html", {"students": students})

@login_required
def project(request):
    if not request.user.is_superuser:
        return redirect("login")

    projects = Project.objects.all()
    return render(request, "store/project.html", {"projects": projects})


def admin_student_list(request):
    students = CustomUser.objects.all()
    return render(request, 'store/admin_student_list.html', {'students': students})




def payment_page(request, project_id):

    project = Project.objects.get(id=project_id)

    return render(request, 'user/payment.html', {'project': project})


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


def admin_project_list(request):

    projects = Project.objects.all().order_by('-created_at')

    return render(request, 'store/admin_project_list.html', {'projects': projects})



def admin_student_details(request, id):


    students = User.objects.all()

    return render(request, 'store/student_details.html', {'students': students})
    student = get_object_or_404(CustomUser, id=id)
    return render(request, 'store/student_details.html', {'student': student})


