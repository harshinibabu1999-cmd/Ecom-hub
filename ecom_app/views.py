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

def login_view(request):

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
            return render(request, "store/login.html", {"error": "Invalid username or password"})

    return render(request, "store/login.html")


def register_view(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        role = request.POST.get('role')

        if password != confirm_password:
            return render(request, 'store/register.html', {'error': 'Passwords do not match'})

        if User.objects.filter(username=username).exists():
            return render(request, 'store/register.html', {'error': 'Username already exists'})

        if User.objects.filter(email=email).exists():
            return render(request, 'store/register.html', {'error': 'Email already exists'})

        # 🔥 Create CustomUser with role
        user = CustomUser.objects.create_user(
            username=username,
            email=email,
            password=password,
            role=role,
            
        )

        user.save()

        return redirect('login_view')

    return render(request, 'store/register.html')


@login_required
def admin_dashboard(request):
   projects = Project.objects.all()
   return render(request, 'store/admin_dashboard.html', {
       'projects': projects
   })


@login_required

def home(request):
    projects = Project.objects.all()
    return render(request, 'store/home.html', {
        'projects': projects
    })


# ---------------- LOGOUT ----------------
def logout_view(request):
    logout(request)
    return redirect('login_view')

def add_project(request):
    if request.method == "POST":
        Project.objects.create(
            name=request.POST['name'],
            description=request.POST['description'],
            price=request.POST['price'],
            drive_link=request.POST['drive_link'],
            thumbnail=request.FILES['thumbnail']
        )
        return redirect('admin_dashboard')

    return render(request, 'add_project.html')


@login_required
def edit_project(request, id):
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
        return redirect("manage_projects")

    return render(request, "store/edit_project.html", {"project": project})


@login_required
def delete_project(request, id):
    project = get_object_or_404(Project, id=id)
    project.delete()
    return redirect("manage_projects")

@login_required
def block_user(request, id):
    user = get_object_or_404(User, id=id)
    user.is_active = False
    user.save()
    return redirect("view_students")

@login_required
def delete_user(request, id):
    user = get_object_or_404(User, id=id)
    user.delete()
    return redirect("view_students")


@login_required
def add_project(request):
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

    return render(request, "store/add_project.html")

@login_required
def view_students(request):
    if not request.user.is_superuser:
        return redirect("login")

    students = StudentProfile.objects.select_related("user")

    return render(request, "store/view_students.html", {"students": students})

@login_required
def project(request):
    if not request.user.is_superuser:
        return redirect("login")

    projects = Project.objects.all()
    return render(request, "store/project.html", {"projects": projects})


def student_list(request):
    students = CustomUser.objects.all()
    return render(request, 'store/student_list.html', {'students': students})




def payment_page(request, project_id):

    project = Project.objects.get(id=project_id)

    return render(request, 'store/payment.html', {'project': project})


@login_required
def upload_project(request):

    if request.method == "POST":
        form = ProjectForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return redirect('project_list')

    else:
        form = ProjectForm()

    return render(request, 'store/upload_project.html', {'form': form})


def project_list(request):

    projects = Project.objects.all().order_by('-created_at')

    return render(request, 'store/project_list.html', {'projects': projects})



def student_details(request, id):


    students = User.objects.all()

    return render(request, 'store/student_details.html', {'students': students})
    student = get_object_or_404(CustomUser, id=id)
    return render(request, 'store/student_details.html', {'student': student})


