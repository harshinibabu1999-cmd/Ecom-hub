from django.db import models

from django.contrib.auth.models import AbstractUser

from django.utils import timezone
 
 


class CustomUser(AbstractUser):
 
    ROLE_CHOICES = (

        ('ADMIN', 'Admin'),

        ('STUDENT', 'Student'),

    )
 
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='STUDENT')
 
   

    phone_number = models.CharField(max_length=15, null=True, blank=True)

    college_name = models.CharField(max_length=255, null=True, blank=True)

    department = models.CharField(max_length=255, null=True, blank=True)

    year_of_study = models.CharField(max_length=50, null=True, blank=True)

    address = models.TextField(max_length=255, null=True, blank=True)

    city = models.CharField(max_length=100, null=True, blank=True)

    state = models.CharField(max_length=100, null=True, blank=True)

    pincode = models.CharField(max_length=10, null=True, blank=True)

    is_student_registered = models.BooleanField(default=False)

    is_student_registered = models.BooleanField(default=False)
 
    def __str__(self):

        return self.username
 
class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name
        


class Project(models.Model):
 
    CATEGORY_CHOICES = (

        ('AI', 'Artificial Intelligence'),

        ('ML', 'Machine Learning'),

        ('DL', 'Deep Learning'),

        ('WEB', 'Web Development'),

        ('IOT', 'Internet of Things'),

        ('DATA', 'Data Science'),

    )

 
    title = models.CharField(max_length=255)

    video = models.FileField(upload_to='videos/', null=True, blank=True)

    description = models.TextField()

    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)

    price = models.DecimalField(max_digits=10, decimal_places=2)

    google_drive_link = models.URLField()

    project_image = models.ImageField(upload_to='projects/', null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)

<<<<<<< HEAD
    file = models.FileField(upload_to="projects/")

=======
 
>>>>>>> 1993b0979d958b364ed65bff7682a57686414863
 
    def __str__(self):

        return self.title
 

class Payment(models.Model):
 
    PAYMENT_STATUS = (

        ('PENDING', 'Pending'),

        ('SUCCESS', 'Success'),

        ('FAILED', 'Failed'),

    )
 
    PAYMENT_MODE = (

        ('UPI', 'UPI'),

        ('DEBIT_CARD', 'Debit Card'),

        ('CREDIT_CARD', 'Credit Card'),

        ('WALLET', 'Wallet'),

    )
 
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

    project = models.ForeignKey(Project, on_delete=models.CASCADE)
 
    transaction_id = models.CharField(max_length=255, unique=True)

    phonepe_transaction_id = models.CharField(max_length=255, blank=True, null=True)
 
    payment_mode = models.CharField(max_length=20, choices=PAYMENT_MODE)

    amount = models.DecimalField(max_digits=10, decimal_places=2)
 
    status = models.CharField(max_length=10, choices=PAYMENT_STATUS, default='PENDING')

    payment_response = models.TextField(blank=True, null=True)
 
    created_at = models.DateTimeField(default=timezone.now)
 
    def __str__(self):

        return f"{self.user.username} - {self.project.title} - {self.status}"

class Purchase(models.Model):
 
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

    project = models.ForeignKey(Project, on_delete=models.CASCADE)

    payment = models.OneToOneField(Payment, on_delete=models.CASCADE)
 
    purchase_date = models.DateTimeField(auto_now_add=True)
 
    def __str__(self):

        return f"{self.user.username} purchased {self.project.title}"
 
 


class AdminAnalytics(models.Model):

    """

    Optional model to store monthly sales summary if needed.

    Otherwise analytics can be calculated dynamically.

    """
 
    month = models.CharField(max_length=20)

    year = models.IntegerField()

    total_sales = models.DecimalField(max_digits=12, decimal_places=2)

    total_projects_sold = models.IntegerField()
 
    def __str__(self):

        return f"{self.month} {self.year} Report"
 