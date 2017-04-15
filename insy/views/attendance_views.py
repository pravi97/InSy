from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from ..models import Attendance
from ..forms import AttendanceForm
from django.core.urlresolvers import reverse_lazy
from django.core.urlresolvers import reverse
from django.http import Http404


class AttendanceListView(ListView):
    model = Attendance
    template_name = "insy/attendance_list.html"
    paginate_by = 20
    context_object_name = "attendance_list"
    allow_empty = True
    page_kwarg = 'page'
    paginate_orphans = 0

    def __init__(self, **kwargs):
        return super(AttendanceListView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(AttendanceListView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(AttendanceListView, self).get(request, *args, **kwargs)

    def get_queryset(self):
        return super(AttendanceListView, self).get_queryset()

    def get_allow_empty(self):
        return super(AttendanceListView, self).get_allow_empty()

    def get_context_data(self, *args, **kwargs):
        ret = super(AttendanceListView, self).get_context_data(*args, **kwargs)
        return ret

    def get_paginate_by(self, queryset):
        return super(AttendanceListView, self).get_paginate_by(queryset)

    def get_context_object_name(self, object_list):
        return super(AttendanceListView, self).get_context_object_name(object_list)

    def paginate_queryset(self, queryset, page_size):
        return super(AttendanceListView, self).paginate_queryset(queryset, page_size)

    def get_paginator(self, queryset, per_page, orphans=0, allow_empty_first_page=True):
        return super(AttendanceListView, self).get_paginator(queryset, per_page, orphans=0, allow_empty_first_page=True)

    def render_to_response(self, context, **response_kwargs):
        return super(AttendanceListView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(AttendanceListView, self).get_template_names()


class AttendanceDetailView(DetailView):
    model = Attendance
    template_name = "insy/attendance_detail.html"
    context_object_name = "attendance"
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    pk_url_kwarg = 'pk'

    def __init__(self, **kwargs):
        return super(AttendanceDetailView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(AttendanceDetailView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(AttendanceDetailView, self).get(request, *args, **kwargs)

    def get_object(self, queryset=None):
        return super(AttendanceDetailView, self).get_object(queryset)

    def get_queryset(self):
        return super(AttendanceDetailView, self).get_queryset()

    def get_slug_field(self):
        return super(AttendanceDetailView, self).get_slug_field()

    def get_context_data(self, **kwargs):
        ret = super(AttendanceDetailView, self).get_context_data(**kwargs)
        return ret

    def get_context_object_name(self, obj):
        return super(AttendanceDetailView, self).get_context_object_name(obj)

    def render_to_response(self, context, **response_kwargs):
        return super(AttendanceDetailView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(AttendanceDetailView, self).get_template_names()


class AttendanceCreateView(CreateView):
    model = Attendance
    form_class = AttendanceForm
    # fields = ['student', 'subject', 'month', 'hours_in_total', 'hours_attended']
    template_name = "insy/attendance_create.html"
    success_url = reverse_lazy("attendance_list")

    def __init__(self, **kwargs):
        return super(AttendanceCreateView, self).__init__(**kwargs)

    def dispatch(self, request, *args, **kwargs):
        return super(AttendanceCreateView, self).dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(AttendanceCreateView, self).get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return super(AttendanceCreateView, self).post(request, *args, **kwargs)

    def get_form_class(self):
        return super(AttendanceCreateView, self).get_form_class()

    def get_form(self, form_class=None):
        return super(AttendanceCreateView, self).get_form(form_class)

    def get_form_kwargs(self, **kwargs):
        return super(AttendanceCreateView, self).get_form_kwargs(**kwargs)

    def get_initial(self):
        return super(AttendanceCreateView, self).get_initial()

    def form_invalid(self, form):
        return super(AttendanceCreateView, self).form_invalid(form)

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.save()
        return super(AttendanceCreateView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        ret = super(AttendanceCreateView, self).get_context_data(**kwargs)
        return ret

    def render_to_response(self, context, **response_kwargs):
        return super(AttendanceCreateView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(AttendanceCreateView, self).get_template_names()

    def get_success_url(self):
        return reverse("attendance_detail", args=(self.object.pk,))


class AttendanceUpdateView(UpdateView):
    model = Attendance
    form_class = AttendanceForm
    # fields = ['student', 'subject', 'month', 'hours_in_total', 'hours_attended']
    template_name = "insy/attendance_update.html"
    initial = {}
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    pk_url_kwarg = 'pk'
    context_object_name = "attendance"

    def __init__(self, **kwargs):
        return super(AttendanceUpdateView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(AttendanceUpdateView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(AttendanceUpdateView, self).get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return super(AttendanceUpdateView, self).post(request, *args, **kwargs)

    def get_object(self, queryset=None):
        return super(AttendanceUpdateView, self).get_object(queryset)

    def get_queryset(self):
        return super(AttendanceUpdateView, self).get_queryset()

    def get_slug_field(self):
        return super(AttendanceUpdateView, self).get_slug_field()

    def get_form_class(self):
        return super(AttendanceUpdateView, self).get_form_class()

    def get_form(self, form_class=None):
        return super(AttendanceUpdateView, self).get_form(form_class)

    def get_form_kwargs(self, **kwargs):
        return super(AttendanceUpdateView, self).get_form_kwargs(**kwargs)

    def get_initial(self):
        return super(AttendanceUpdateView, self).get_initial()

    def form_invalid(self, form):
        return super(AttendanceUpdateView, self).form_invalid(form)

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.save()
        return super(AttendanceUpdateView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        ret = super(AttendanceUpdateView, self).get_context_data(**kwargs)
        return ret

    def get_context_object_name(self, obj):
        return super(AttendanceUpdateView, self).get_context_object_name(obj)

    def render_to_response(self, context, **response_kwargs):
        return super(AttendanceUpdateView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(AttendanceUpdateView, self).get_template_names()

    def get_success_url(self):
        return reverse("attendance_detail", args=(self.object.pk,))


class AttendanceDeleteView(DeleteView):
    model = Attendance
    template_name = "insy/attendance_delete.html"
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    pk_url_kwarg = 'pk'
    context_object_name = "attendance"

    def __init__(self, **kwargs):
        return super(AttendanceDeleteView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(AttendanceDeleteView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        raise Http404

    def post(self, request, *args, **kwargs):
        return super(AttendanceDeleteView, self).post(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return super(AttendanceDeleteView, self).delete(request, *args, **kwargs)

    def get_object(self, queryset=None):
        return super(AttendanceDeleteView, self).get_object(queryset)

    def get_queryset(self):
        return super(AttendanceDeleteView, self).get_queryset()

    def get_slug_field(self):
        return super(AttendanceDeleteView, self).get_slug_field()

    def get_context_data(self, **kwargs):
        ret = super(AttendanceDeleteView, self).get_context_data(**kwargs)
        return ret

    def get_context_object_name(self, obj):
        return super(AttendanceDeleteView, self).get_context_object_name(obj)

    def render_to_response(self, context, **response_kwargs):
        return super(AttendanceDeleteView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(AttendanceDeleteView, self).get_template_names()

    def get_success_url(self):
        return reverse("attendance_list")
