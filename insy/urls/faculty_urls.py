from django.conf.urls import url
from ..views import (FacultyListView, FacultyCreateView, FacultyDetailView,
                     FacultyUpdateView, FacultyDeleteView)
from django.contrib.auth.decorators import login_required


urlpatterns = [
    url(r'^create/$',  # NOQA
        login_required(FacultyCreateView.as_view()),
        name="faculty_create"),

    url(r'^(?P<pk>\d+)/update/$',
        login_required(FacultyUpdateView.as_view()),
        name="faculty_update"),

    url(r'^(?P<pk>\d+)/delete/$',
        login_required(FacultyDeleteView.as_view()),
        name="faculty_delete"),

    url(r'^(?P<pk>\d+)/$',
        FacultyDetailView.as_view(),
        name="faculty_detail"),

    url(r'^$',
        FacultyListView.as_view(),
        name="faculty_list"),
]
