from django.conf.urls import url
from ..views import (AttendanceListView, AttendanceCreateView, AttendanceDetailView,
                     AttendanceUpdateView, AttendanceDeleteView)
from django.contrib.auth.decorators import login_required


urlpatterns = [
    url(r'^create/$',  # NOQA
        login_required(AttendanceCreateView.as_view()),
        name="attendance_create"),

    url(r'^(?P<pk>\d+)/update/$',
        login_required(AttendanceUpdateView.as_view()),
        name="attendance_update"),

    url(r'^(?P<pk>\d+)/delete/$',
        login_required(AttendanceDeleteView.as_view()),
        name="attendance_delete"),

    url(r'^(?P<pk>\d+)/$',
        AttendanceDetailView.as_view(),
        name="attendance_detail"),

    url(r'^$',
        AttendanceListView.as_view(),
        name="attendance_list"),
]
