from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from ..models import Department
from ..forms import DepartmentForm
from django.core.urlresolvers import reverse_lazy
from django.core.urlresolvers import reverse
from django.http import Http404


class DepartmentListView(ListView):
    model = Department
    template_name = "insy/department_list.html"
    paginate_by = 20
    context_object_name = "department_list"
    allow_empty = True
    page_kwarg = 'page'
    paginate_orphans = 0

    def __init__(self, **kwargs):
        return super(DepartmentListView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(DepartmentListView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(DepartmentListView, self).get(request, *args, **kwargs)

    def get_queryset(self):
        return super(DepartmentListView, self).get_queryset()

    def get_allow_empty(self):
        return super(DepartmentListView, self).get_allow_empty()

    def get_context_data(self, *args, **kwargs):
        ret = super(DepartmentListView, self).get_context_data(*args, **kwargs)
        return ret

    def get_paginate_by(self, queryset):
        return super(DepartmentListView, self).get_paginate_by(queryset)

    def get_context_object_name(self, object_list):
        return super(DepartmentListView, self).get_context_object_name(object_list)

    def paginate_queryset(self, queryset, page_size):
        return super(DepartmentListView, self).paginate_queryset(queryset, page_size)

    def get_paginator(self, queryset, per_page, orphans=0, allow_empty_first_page=True):
        return super(DepartmentListView, self).get_paginator(queryset, per_page, orphans=0, allow_empty_first_page=True)

    def render_to_response(self, context, **response_kwargs):
        return super(DepartmentListView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(DepartmentListView, self).get_template_names()


class DepartmentDetailView(DetailView):
    model = Department
    template_name = "insy/department_detail.html"
    context_object_name = "department"
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    pk_url_kwarg = 'pk'

    def __init__(self, **kwargs):
        return super(DepartmentDetailView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(DepartmentDetailView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(DepartmentDetailView, self).get(request, *args, **kwargs)

    def get_object(self, queryset=None):
        return super(DepartmentDetailView, self).get_object(queryset)

    def get_queryset(self):
        return super(DepartmentDetailView, self).get_queryset()

    def get_slug_field(self):
        return super(DepartmentDetailView, self).get_slug_field()

    def get_context_data(self, **kwargs):
        ret = super(DepartmentDetailView, self).get_context_data(**kwargs)
        return ret

    def get_context_object_name(self, obj):
        return super(DepartmentDetailView, self).get_context_object_name(obj)

    def render_to_response(self, context, **response_kwargs):
        return super(DepartmentDetailView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(DepartmentDetailView, self).get_template_names()


class DepartmentCreateView(CreateView):
    model = Department
    form_class = DepartmentForm
    # fields = ['dept_id', 'dept_name']
    template_name = "insy/department_create.html"
    success_url = reverse_lazy("department_list")

    def __init__(self, **kwargs):
        return super(DepartmentCreateView, self).__init__(**kwargs)

    def dispatch(self, request, *args, **kwargs):
        return super(DepartmentCreateView, self).dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(DepartmentCreateView, self).get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return super(DepartmentCreateView, self).post(request, *args, **kwargs)

    def get_form_class(self):
        return super(DepartmentCreateView, self).get_form_class()

    def get_form(self, form_class=None):
        return super(DepartmentCreateView, self).get_form(form_class)

    def get_form_kwargs(self, **kwargs):
        return super(DepartmentCreateView, self).get_form_kwargs(**kwargs)

    def get_initial(self):
        return super(DepartmentCreateView, self).get_initial()

    def form_invalid(self, form):
        return super(DepartmentCreateView, self).form_invalid(form)

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.save()
        return super(DepartmentCreateView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        ret = super(DepartmentCreateView, self).get_context_data(**kwargs)
        return ret

    def render_to_response(self, context, **response_kwargs):
        return super(DepartmentCreateView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(DepartmentCreateView, self).get_template_names()

    def get_success_url(self):
        return reverse("department_detail", args=(self.object.pk,))


class DepartmentUpdateView(UpdateView):
    model = Department
    form_class = DepartmentForm
    # fields = ['dept_id', 'dept_name']
    template_name = "insy/department_update.html"
    initial = {}
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    pk_url_kwarg = 'pk'
    context_object_name = "department"

    def __init__(self, **kwargs):
        return super(DepartmentUpdateView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(DepartmentUpdateView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(DepartmentUpdateView, self).get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return super(DepartmentUpdateView, self).post(request, *args, **kwargs)

    def get_object(self, queryset=None):
        return super(DepartmentUpdateView, self).get_object(queryset)

    def get_queryset(self):
        return super(DepartmentUpdateView, self).get_queryset()

    def get_slug_field(self):
        return super(DepartmentUpdateView, self).get_slug_field()

    def get_form_class(self):
        return super(DepartmentUpdateView, self).get_form_class()

    def get_form(self, form_class=None):
        return super(DepartmentUpdateView, self).get_form(form_class)

    def get_form_kwargs(self, **kwargs):
        return super(DepartmentUpdateView, self).get_form_kwargs(**kwargs)

    def get_initial(self):
        return super(DepartmentUpdateView, self).get_initial()

    def form_invalid(self, form):
        return super(DepartmentUpdateView, self).form_invalid(form)

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.save()
        return super(DepartmentUpdateView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        ret = super(DepartmentUpdateView, self).get_context_data(**kwargs)
        return ret

    def get_context_object_name(self, obj):
        return super(DepartmentUpdateView, self).get_context_object_name(obj)

    def render_to_response(self, context, **response_kwargs):
        return super(DepartmentUpdateView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(DepartmentUpdateView, self).get_template_names()

    def get_success_url(self):
        return reverse("department_detail", args=(self.object.pk,))


class DepartmentDeleteView(DeleteView):
    model = Department
    template_name = "insy/department_delete.html"
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    pk_url_kwarg = 'pk'
    context_object_name = "department"

    def __init__(self, **kwargs):
        return super(DepartmentDeleteView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(DepartmentDeleteView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        raise Http404

    def post(self, request, *args, **kwargs):
        return super(DepartmentDeleteView, self).post(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return super(DepartmentDeleteView, self).delete(request, *args, **kwargs)

    def get_object(self, queryset=None):
        return super(DepartmentDeleteView, self).get_object(queryset)

    def get_queryset(self):
        return super(DepartmentDeleteView, self).get_queryset()

    def get_slug_field(self):
        return super(DepartmentDeleteView, self).get_slug_field()

    def get_context_data(self, **kwargs):
        ret = super(DepartmentDeleteView, self).get_context_data(**kwargs)
        return ret

    def get_context_object_name(self, obj):
        return super(DepartmentDeleteView, self).get_context_object_name(obj)

    def render_to_response(self, context, **response_kwargs):
        return super(DepartmentDeleteView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(DepartmentDeleteView, self).get_template_names()

    def get_success_url(self):
        return reverse("department_list")
