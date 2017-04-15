from django.conf.urls import url
from ..views import (Academic_HistoryListView, Academic_HistoryCreateView, Academic_HistoryDetailView,
                     Academic_HistoryUpdateView, Academic_HistoryDeleteView)
from django.contrib.auth.decorators import login_required


urlpatterns = [
    url(r'^create/$',  # NOQA
        login_required(Academic_HistoryCreateView.as_view()),
        name="academic_history_create"),

    url(r'^(?P<pk>\d+)/update/$',
        login_required(Academic_HistoryUpdateView.as_view()),
        name="academic_history_update"),

    url(r'^(?P<pk>\d+)/delete/$',
        login_required(Academic_HistoryDeleteView.as_view()),
        name="academic_history_delete"),

    url(r'^(?P<pk>\d+)/$',
        Academic_HistoryDetailView.as_view(),
        name="academic_history_detail"),

    url(r'^$',
        Academic_HistoryListView.as_view(),
        name="academic_history_list"),
]
