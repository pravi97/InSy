from django import forms
from .models import Faculty, Student, Subject, Department, Academic_History, Attendance


class FacultyForm(forms.ModelForm):

    class Meta:
        model = Faculty
        fields = ['user', 'name', 'designation', 'department', 'email', 'phone_number']
        exclude = []
        widgets = None
        localized_fields = None
        labels = {}
        help_texts = {}
        error_messages = {}

    def __init__(self, *args, **kwargs):
        return super(FacultyForm, self).__init__(*args, **kwargs)

    def is_valid(self):
        return super(FacultyForm, self).is_valid()

    def full_clean(self):
        return super(FacultyForm, self).full_clean()

    def clean_user(self):
        user = self.cleaned_data.get("user", None)
        return user

    def clean_name(self):
        name = self.cleaned_data.get("name", None)
        return name

    def clean_designation(self):
        designation = self.cleaned_data.get("designation", None)
        return designation

    def clean_department(self):
        department = self.cleaned_data.get("department", None)
        return department

    def clean_email(self):
        email = self.cleaned_data.get("email", None)
        return email

    def clean_phone_number(self):
        phone_number = self.cleaned_data.get("phone_number", None)
        return phone_number

    def clean(self):
        return super(FacultyForm, self).clean()

    def validate_unique(self):
        return super(FacultyForm, self).validate_unique()

    def save(self, commit=True):
        return super(FacultyForm, self).save(commit)


class StudentForm(forms.ModelForm):

    class Meta:
        model = Student
        fields = ['user', 'department', 'semester', 'date_of_registration', 'name', 'name_of_parent', 'address', 'Academic_History', 'Whether_eligible_for_registration', 'Hosteler_or_dayscholar', 'name_of_hostel']
        exclude = []
        widgets = None
        localized_fields = None
        labels = {}
        help_texts = {}
        error_messages = {}

    def __init__(self, *args, **kwargs):
        return super(StudentForm, self).__init__(*args, **kwargs)

    def is_valid(self):
        return super(StudentForm, self).is_valid()

    def full_clean(self):
        return super(StudentForm, self).full_clean()

    def clean_user(self):
        user = self.cleaned_data.get("user", None)
        return user

    def clean_department(self):
        department = self.cleaned_data.get("department", None)
        return department

    def clean_semester(self):
        semester = self.cleaned_data.get("semester", None)
        return semester

    def clean_date_of_registration(self):
        date_of_registration = self.cleaned_data.get("date_of_registration", None)
        return date_of_registration

    def clean_name(self):
        name = self.cleaned_data.get("name", None)
        return name

    def clean_name_of_parent(self):
        name_of_parent = self.cleaned_data.get("name_of_parent", None)
        return name_of_parent

    def clean_address(self):
        address = self.cleaned_data.get("address", None)
        return address

    def clean_Academic_History(self):
        Academic_History = self.cleaned_data.get("Academic_History", None)
        return Academic_History

    def clean_Whether_eligible_for_registration(self):
        Whether_eligible_for_registration = self.cleaned_data.get("Whether_eligible_for_registration", None)
        return Whether_eligible_for_registration

    def clean_Hosteler_or_dayscholar(self):
        Hosteler_or_dayscholar = self.cleaned_data.get("Hosteler_or_dayscholar", None)
        return Hosteler_or_dayscholar

    def clean_name_of_hostel(self):
        name_of_hostel = self.cleaned_data.get("name_of_hostel", None)
        return name_of_hostel

    def clean(self):
        return super(StudentForm, self).clean()

    def validate_unique(self):
        return super(StudentForm, self).validate_unique()

    def save(self, commit=True):
        return super(StudentForm, self).save(commit)


class SubjectForm(forms.ModelForm):

    class Meta:
        model = Subject
        fields = ['subject_code', 'subject_name', 'faculty']
        exclude = []
        widgets = None
        localized_fields = None
        labels = {}
        help_texts = {}
        error_messages = {}

    def __init__(self, *args, **kwargs):
        return super(SubjectForm, self).__init__(*args, **kwargs)

    def is_valid(self):
        return super(SubjectForm, self).is_valid()

    def full_clean(self):
        return super(SubjectForm, self).full_clean()

    def clean_subject_code(self):
        subject_code = self.cleaned_data.get("subject_code", None)
        return subject_code

    def clean_subject_name(self):
        subject_name = self.cleaned_data.get("subject_name", None)
        return subject_name

    def clean_faculty(self):
        faculty = self.cleaned_data.get("faculty", None)
        return faculty

    def clean(self):
        return super(SubjectForm, self).clean()

    def validate_unique(self):
        return super(SubjectForm, self).validate_unique()

    def save(self, commit=True):
        return super(SubjectForm, self).save(commit)


class DepartmentForm(forms.ModelForm):

    class Meta:
        model = Department
        fields = ['dept_id', 'dept_name']
        exclude = []
        widgets = None
        localized_fields = None
        labels = {}
        help_texts = {}
        error_messages = {}

    def __init__(self, *args, **kwargs):
        return super(DepartmentForm, self).__init__(*args, **kwargs)

    def is_valid(self):
        return super(DepartmentForm, self).is_valid()

    def full_clean(self):
        return super(DepartmentForm, self).full_clean()

    def clean_dept_id(self):
        dept_id = self.cleaned_data.get("dept_id", None)
        return dept_id

    def clean_dept_name(self):
        dept_name = self.cleaned_data.get("dept_name", None)
        return dept_name

    def clean(self):
        return super(DepartmentForm, self).clean()

    def validate_unique(self):
        return super(DepartmentForm, self).validate_unique()

    def save(self, commit=True):
        return super(DepartmentForm, self).save(commit)


class Academic_HistoryForm(forms.ModelForm):

    class Meta:
        model = Academic_History
        fields = ['university_roll_no', 'semester', 'month_of_registration', 'Whether_condonation_availed']
        exclude = []
        widgets = None
        localized_fields = None
        labels = {}
        help_texts = {}
        error_messages = {}

    def __init__(self, *args, **kwargs):
        return super(Academic_HistoryForm, self).__init__(*args, **kwargs)

    def is_valid(self):
        return super(Academic_HistoryForm, self).is_valid()

    def full_clean(self):
        return super(Academic_HistoryForm, self).full_clean()

    def clean_university_roll_no(self):
        university_roll_no = self.cleaned_data.get("university_roll_no", None)
        return university_roll_no

    def clean_semester(self):
        semester = self.cleaned_data.get("semester", None)
        return semester

    def clean_month_of_registration(self):
        month_of_registration = self.cleaned_data.get("month_of_registration", None)
        return month_of_registration

    def clean_Whether_condonation_availed(self):
        Whether_condonation_availed = self.cleaned_data.get("Whether_condonation_availed", None)
        return Whether_condonation_availed

    def clean(self):
        return super(Academic_HistoryForm, self).clean()

    def validate_unique(self):
        return super(Academic_HistoryForm, self).validate_unique()

    def save(self, commit=True):
        return super(Academic_HistoryForm, self).save(commit)


class AttendanceForm(forms.ModelForm):

    class Meta:
        model = Attendance
        fields = ['student', 'subject', 'month', 'hours_in_total', 'hours_attended']
        exclude = []
        widgets = None
        localized_fields = None
        labels = {}
        help_texts = {}
        error_messages = {}

    def __init__(self, *args, **kwargs):
        return super(AttendanceForm, self).__init__(*args, **kwargs)

    def is_valid(self):
        return super(AttendanceForm, self).is_valid()

    def full_clean(self):
        return super(AttendanceForm, self).full_clean()

    def clean_student(self):
        student = self.cleaned_data.get("student", None)
        return student

    def clean_subject(self):
        subject = self.cleaned_data.get("subject", None)
        return subject

    def clean_month(self):
        month = self.cleaned_data.get("month", None)
        return month

    def clean_hours_in_total(self):
        hours_in_total = self.cleaned_data.get("hours_in_total", None)
        return hours_in_total

    def clean_hours_attended(self):
        hours_attended = self.cleaned_data.get("hours_attended", None)
        return hours_attended

    def clean(self):
        return super(AttendanceForm, self).clean()

    def validate_unique(self):
        return super(AttendanceForm, self).validate_unique()

    def save(self, commit=True):
        return super(AttendanceForm, self).save(commit)

