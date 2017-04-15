from django.conf.urls import url
from ..views import (DepartmentListView, DepartmentCreateView, DepartmentDetailView,
                     DepartmentUpdateView, DepartmentDeleteView)
from django.contrib.auth.decorators import login_required


urlpatterns = [
    url(r'^create/$',  # NOQA
        login_required(DepartmentCreateView.as_view()),
        name="department_create"),

    url(r'^(?P<pk>\d+)/update/$',
        login_required(DepartmentUpdateView.as_view()),
        name="department_update"),

    url(r'^(?P<pk>\d+)/delete/$',
        login_required(DepartmentDeleteView.as_view()),
        name="department_delete"),

    url(r'^(?P<pk>\d+)/$',
        DepartmentDetailView.as_view(),
        name="department_detail"),

    url(r'^$',
        DepartmentListView.as_view(),
        name="department_list"),
]
