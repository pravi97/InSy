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

class Academic_History(models.Model):
    semester = models.CharField(max_length=50,choices=(('S1','Semester I'),('S2','Semester II'),('S3','Semester III'),('S4','Semester IV'),('S5','Semester V'),('S6','Semester VI'),('S7','Semester VII'),('S8','Semester VIII')),default=1)
    month_of_registration = models.DateField()
    Whether_condonation_availed = models.CharField(max_length=50,choices=((1,'No'),(2,'Yes')),default=2)


class Student(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,null=True)
    department = models.CharField(max_length=100,choices=(('CE','Civil Engineering'),('CHE','Chemical Engineering'),('CSE','Computer Science & Engineering'),('ECE','Electronics & Commmunication Engineering'),('EEE','Electrical & Electronics Engineering'),('ME','Mechanical Engineering'),('PE','Production Engineering')),default='CSE')
    semester = models.CharField(max_length=50,choices=(('S1','Semester I'),('S2','Semester II'),('S3','Semester III'),('S4','Semester IV'),('S5','Semester V'),('S6','Semester VI'),('S7','Semester VII'),('S8','Semester VIII')),default=1)
    date_of_registration = models.DateField()
    name = models.CharField(max_length=30)
    university_roll_no = models.CharField(max_length=20)
    name_of_parent = models.CharField(max_length=30)
    address = models.TextField(max_length=100)
    Academic_History = models.ForeignKey(to=Academic_History,related_name="examdetails",null=True, blank=True)
    Whether_eligible_for_registration = models.CharField(max_length=50,choices=((1,'No'),(2,'Yes')),default=2)
    Hosteler_or_dayscholar = models.CharField(max_length=10,choices=(('D','Dayscholar'),('H','Hosteler')),default='D')
    name_of_hostel = models.CharField(max_length=50,null=True,blank=True)

    def __str__(self):
        return self.user

class Subject(models.Model):
    subject_code = models.CharField(max_length=10)
    subject_name = models.CharField(max_length=100)
    faculty = models.ForeignKey(to=Faculty,related_name="teaches",null=True, blank=True)

    def __str__(self):
        return self.subject_name

class Attendance(models.Model):
    student = models.ForeignKey(to=Student,related_name="attends",null=True, blank=True)
    subject = models.ForeignKey(to=Subject,related_name="attended",null=True, blank=True)
    month = models.DateField()
    hours_in_total = models.IntegerField()
    hours_attended = models.IntegerField()

    def __str__(self):
        return self.student
