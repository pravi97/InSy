from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from ..models import Faculty
from ..forms import FacultyForm
from django.core.urlresolvers import reverse_lazy
from django.core.urlresolvers import reverse
from django.http import Http404


class FacultyListView(ListView):
    model = Faculty
    template_name = "insy/faculty_list.html"
    paginate_by = 20
    context_object_name = "faculty_list"
    allow_empty = True
    page_kwarg = 'page'
    paginate_orphans = 0

    def __init__(self, **kwargs):
        return super(FacultyListView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(FacultyListView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(FacultyListView, self).get(request, *args, **kwargs)

    def get_queryset(self):
        return super(FacultyListView, self).get_queryset()

    def get_allow_empty(self):
        return super(FacultyListView, self).get_allow_empty()

    def get_context_data(self, *args, **kwargs):
        ret = super(FacultyListView, self).get_context_data(*args, **kwargs)
        return ret

    def get_paginate_by(self, queryset):
        return super(FacultyListView, self).get_paginate_by(queryset)

    def get_context_object_name(self, object_list):
        return super(FacultyListView, self).get_context_object_name(object_list)

    def paginate_queryset(self, queryset, page_size):
        return super(FacultyListView, self).paginate_queryset(queryset, page_size)

    def get_paginator(self, queryset, per_page, orphans=0, allow_empty_first_page=True):
        return super(FacultyListView, self).get_paginator(queryset, per_page, orphans=0, allow_empty_first_page=True)

    def render_to_response(self, context, **response_kwargs):
        return super(FacultyListView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(FacultyListView, self).get_template_names()


class FacultyDetailView(DetailView):
    model = Faculty
    template_name = "insy/faculty_detail.html"
    context_object_name = "faculty"
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    pk_url_kwarg = 'pk'

    def __init__(self, **kwargs):
        return super(FacultyDetailView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(FacultyDetailView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(FacultyDetailView, self).get(request, *args, **kwargs)

    def get_object(self, queryset=None):
        return super(FacultyDetailView, self).get_object(queryset)

    def get_queryset(self):
        return super(FacultyDetailView, self).get_queryset()

    def get_slug_field(self):
        return super(FacultyDetailView, self).get_slug_field()

    def get_context_data(self, **kwargs):
        ret = super(FacultyDetailView, self).get_context_data(**kwargs)
        return ret

    def get_context_object_name(self, obj):
        return super(FacultyDetailView, self).get_context_object_name(obj)

    def render_to_response(self, context, **response_kwargs):
        return super(FacultyDetailView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(FacultyDetailView, self).get_template_names()


class FacultyCreateView(CreateView):
    model = Faculty
    form_class = FacultyForm
    # fields = ['user', 'name', 'designation', 'department', 'email', 'phone_number']
    template_name = "insy/faculty_create.html"
    success_url = reverse_lazy("faculty_list")

    def __init__(self, **kwargs):
        return super(FacultyCreateView, self).__init__(**kwargs)

    def dispatch(self, request, *args, **kwargs):
        return super(FacultyCreateView, self).dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(FacultyCreateView, self).get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return super(FacultyCreateView, self).post(request, *args, **kwargs)

    def get_form_class(self):
        return super(FacultyCreateView, self).get_form_class()

    def get_form(self, form_class=None):
        return super(FacultyCreateView, self).get_form(form_class)

    def get_form_kwargs(self, **kwargs):
        return super(FacultyCreateView, self).get_form_kwargs(**kwargs)

    def get_initial(self):
        return super(FacultyCreateView, self).get_initial()

    def form_invalid(self, form):
        return super(FacultyCreateView, self).form_invalid(form)

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.save()
        return super(FacultyCreateView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        ret = super(FacultyCreateView, self).get_context_data(**kwargs)
        return ret

    def render_to_response(self, context, **response_kwargs):
        return super(FacultyCreateView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(FacultyCreateView, self).get_template_names()

    def get_success_url(self):
        return reverse("faculty_detail", args=(self.object.pk,))


class FacultyUpdateView(UpdateView):
    model = Faculty
    form_class = FacultyForm
    # fields = ['user', 'name', 'designation', 'department', 'email', 'phone_number']
    template_name = "insy/faculty_update.html"
    initial = {}
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    pk_url_kwarg = 'pk'
    context_object_name = "faculty"

    def __init__(self, **kwargs):
        return super(FacultyUpdateView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(FacultyUpdateView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(FacultyUpdateView, self).get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return super(FacultyUpdateView, self).post(request, *args, **kwargs)

    def get_object(self, queryset=None):
        return super(FacultyUpdateView, self).get_object(queryset)

    def get_queryset(self):
        return super(FacultyUpdateView, self).get_queryset()

    def get_slug_field(self):
        return super(FacultyUpdateView, self).get_slug_field()

    def get_form_class(self):
        return super(FacultyUpdateView, self).get_form_class()

    def get_form(self, form_class=None):
        return super(FacultyUpdateView, self).get_form(form_class)

    def get_form_kwargs(self, **kwargs):
        return super(FacultyUpdateView, self).get_form_kwargs(**kwargs)

    def get_initial(self):
        return super(FacultyUpdateView, self).get_initial()

    def form_invalid(self, form):
        return super(FacultyUpdateView, self).form_invalid(form)

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.save()
        return super(FacultyUpdateView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        ret = super(FacultyUpdateView, self).get_context_data(**kwargs)
        return ret

    def get_context_object_name(self, obj):
        return super(FacultyUpdateView, self).get_context_object_name(obj)

    def render_to_response(self, context, **response_kwargs):
        return super(FacultyUpdateView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(FacultyUpdateView, self).get_template_names()

    def get_success_url(self):
        return reverse("faculty_detail", args=(self.object.pk,))


class FacultyDeleteView(DeleteView):
    model = Faculty
    template_name = "insy/faculty_delete.html"
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    pk_url_kwarg = 'pk'
    context_object_name = "faculty"

    def __init__(self, **kwargs):
        return super(FacultyDeleteView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(FacultyDeleteView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        raise Http404

    def post(self, request, *args, **kwargs):
        return super(FacultyDeleteView, self).post(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return super(FacultyDeleteView, self).delete(request, *args, **kwargs)

    def get_object(self, queryset=None):
        return super(FacultyDeleteView, self).get_object(queryset)

    def get_queryset(self):
        return super(FacultyDeleteView, self).get_queryset()

    def get_slug_field(self):
        return super(FacultyDeleteView, self).get_slug_field()

    def get_context_data(self, **kwargs):
        ret = super(FacultyDeleteView, self).get_context_data(**kwargs)
        return ret

    def get_context_object_name(self, obj):
        return super(FacultyDeleteView, self).get_context_object_name(obj)

    def render_to_response(self, context, **response_kwargs):
        return super(FacultyDeleteView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(FacultyDeleteView, self).get_template_names()

    def get_success_url(self):
        return reverse("faculty_list")
