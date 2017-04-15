from django.conf.urls import url
from ..views import (SubjectListView, SubjectCreateView, SubjectDetailView,
                     SubjectUpdateView, SubjectDeleteView)
from django.contrib.auth.decorators import login_required


urlpatterns = [
    url(r'^create/$',  # NOQA
        login_required(SubjectCreateView.as_view()),
        name="subject_create"),

    url(r'^(?P<pk>\d+)/update/$',
        login_required(SubjectUpdateView.as_view()),
        name="subject_update"),

    url(r'^(?P<pk>\d+)/delete/$',
        login_required(SubjectDeleteView.as_view()),
        name="subject_delete"),

    url(r'^(?P<pk>\d+)/$',
        SubjectDetailView.as_view(),
        name="subject_detail"),

    url(r'^$',
        SubjectListView.as_view(),
        name="subject_list"),
]
