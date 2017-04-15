from django.db import models
from django.contrib.auth.models import AbstractUser,AbstractBaseUser,User
from phonenumber_field.modelfields import PhoneNumberField

class Faculty(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,null=True)
    name = models.CharField(max_length=30)
    designation = models.CharField(max_length=50, choices = (('Professor','Professor'),('Associate Professor','Associate Professor'),('Assistant Professor','Assistant Professor'),('ADHOC','ADHOC')))
    department = models.CharField(max_length=100,choices=(('CE','Civil Engineering'),('CHE','Chemical Engineering'),('CSE','Computer Science & Engineering'),('ECE','Electronics & Commmunication Engineering'),('EEE','Electrical & Electronics Engineering'),('ME','Mechanical Engineering'),('PE','Production Engineering')),default='CSE')
    phone_number = PhoneNumberField()
    email = models.EmailField()

    def __str__(self):
        return self.name

class Student(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,null=True)
    department = models.CharField(max_length=100,choices=(('CE','Civil Engineering'),('CHE','Chemical Engineering'),('CSE','Computer Science & Engineering'),('ECE','Electronics & Commmunication Engineering'),('EEE','Electrical & Electronics Engineering'),('ME','Mechanical Engineering'),('PE','Production Engineering')),default='CSE')
    semester = models.CharField(max_length=50,choices=(('S1','Semester I'),('S2','Semester II'),('S3','Semester III'),('S4','Semester IV'),('S5','Semester V'),('S6','Semester VI'),('S7','Semester VII'),('S8','Semester VIII')),default=1)
    date_of_registration = models.DateField()
    name = models.CharField(max_length=30)
    university_roll_no = models.CharField(max_length=20)
    name_of_parent = models.CharField(max_length=30)
    address = models.TextField(max_length=100)
    Hosteler_or_dayscholar = models.CharField(max_length=10,choices=(('D','Dayscholar'),('H','Hosteler')),default='D')
    name_of_hostel = models.CharField(max_length=50,null=True,blank=True)

    def __str__(self):
        return self.user

class Subject(models.Model):
    name = models.CharField(max_length=100)
    faculty = models.ForeignKey(to=Faculty,related_name="teaches",null=True, blank=True)

    def __str__(self):
        return self.name