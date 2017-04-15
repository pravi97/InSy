from django.conf.urls import include, url

urlpatterns = [

    url(r'^departments/', include('insy.urls.department_urls')),  # NOQA
    url(r'^facultys/', include('insy.urls.faculty_urls')),
    url(r'^subjects/', include('insy.urls.subject_urls')),
    url(r'^academic_historys/', include('insy.urls.academic_history_urls')),
    url(r'^attendances/', include('insy.urls.attendance_urls')),
    url(r'^students/', include('insy.urls.student_urls')),
]
