from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from ..models import Subject
from ..forms import SubjectForm
from django.core.urlresolvers import reverse_lazy
from django.core.urlresolvers import reverse
from django.http import Http404


class SubjectListView(ListView):
    model = Subject
    template_name = "insy/subject_list.html"
    paginate_by = 20
    context_object_name = "subject_list"
    allow_empty = True
    page_kwarg = 'page'
    paginate_orphans = 0

    def __init__(self, **kwargs):
        return super(SubjectListView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(SubjectListView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(SubjectListView, self).get(request, *args, **kwargs)

    def get_queryset(self):
        return super(SubjectListView, self).get_queryset()

    def get_allow_empty(self):
        return super(SubjectListView, self).get_allow_empty()

    def get_context_data(self, *args, **kwargs):
        ret = super(SubjectListView, self).get_context_data(*args, **kwargs)
        return ret

    def get_paginate_by(self, queryset):
        return super(SubjectListView, self).get_paginate_by(queryset)

    def get_context_object_name(self, object_list):
        return super(SubjectListView, self).get_context_object_name(object_list)

    def paginate_queryset(self, queryset, page_size):
        return super(SubjectListView, self).paginate_queryset(queryset, page_size)

    def get_paginator(self, queryset, per_page, orphans=0, allow_empty_first_page=True):
        return super(SubjectListView, self).get_paginator(queryset, per_page, orphans=0, allow_empty_first_page=True)

    def render_to_response(self, context, **response_kwargs):
        return super(SubjectListView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(SubjectListView, self).get_template_names()


class SubjectDetailView(DetailView):
    model = Subject
    template_name = "insy/subject_detail.html"
    context_object_name = "subject"
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    pk_url_kwarg = 'pk'

    def __init__(self, **kwargs):
        return super(SubjectDetailView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(SubjectDetailView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(SubjectDetailView, self).get(request, *args, **kwargs)

    def get_object(self, queryset=None):
        return super(SubjectDetailView, self).get_object(queryset)

    def get_queryset(self):
        return super(SubjectDetailView, self).get_queryset()

    def get_slug_field(self):
        return super(SubjectDetailView, self).get_slug_field()

    def get_context_data(self, **kwargs):
        ret = super(SubjectDetailView, self).get_context_data(**kwargs)
        return ret

    def get_context_object_name(self, obj):
        return super(SubjectDetailView, self).get_context_object_name(obj)

    def render_to_response(self, context, **response_kwargs):
        return super(SubjectDetailView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(SubjectDetailView, self).get_template_names()


class SubjectCreateView(CreateView):
    model = Subject
    form_class = SubjectForm
    # fields = ['subject_code', 'subject_name', 'faculty']
    template_name = "insy/subject_create.html"
    success_url = reverse_lazy("subject_list")

    def __init__(self, **kwargs):
        return super(SubjectCreateView, self).__init__(**kwargs)

    def dispatch(self, request, *args, **kwargs):
        return super(SubjectCreateView, self).dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(SubjectCreateView, self).get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return super(SubjectCreateView, self).post(request, *args, **kwargs)

    def get_form_class(self):
        return super(SubjectCreateView, self).get_form_class()

    def get_form(self, form_class=None):
        return super(SubjectCreateView, self).get_form(form_class)

    def get_form_kwargs(self, **kwargs):
        return super(SubjectCreateView, self).get_form_kwargs(**kwargs)

    def get_initial(self):
        return super(SubjectCreateView, self).get_initial()

    def form_invalid(self, form):
        return super(SubjectCreateView, self).form_invalid(form)

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.save()
        return super(SubjectCreateView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        ret = super(SubjectCreateView, self).get_context_data(**kwargs)
        return ret

    def render_to_response(self, context, **response_kwargs):
        return super(SubjectCreateView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(SubjectCreateView, self).get_template_names()

    def get_success_url(self):
        return reverse("subject_detail", args=(self.object.pk,))


class SubjectUpdateView(UpdateView):
    model = Subject
    form_class = SubjectForm
    # fields = ['subject_code', 'subject_name', 'faculty']
    template_name = "insy/subject_update.html"
    initial = {}
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    pk_url_kwarg = 'pk'
    context_object_name = "subject"

    def __init__(self, **kwargs):
        return super(SubjectUpdateView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(SubjectUpdateView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(SubjectUpdateView, self).get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return super(SubjectUpdateView, self).post(request, *args, **kwargs)

    def get_object(self, queryset=None):
        return super(SubjectUpdateView, self).get_object(queryset)

    def get_queryset(self):
        return super(SubjectUpdateView, self).get_queryset()

    def get_slug_field(self):
        return super(SubjectUpdateView, self).get_slug_field()

    def get_form_class(self):
        return super(SubjectUpdateView, self).get_form_class()

    def get_form(self, form_class=None):
        return super(SubjectUpdateView, self).get_form(form_class)

    def get_form_kwargs(self, **kwargs):
        return super(SubjectUpdateView, self).get_form_kwargs(**kwargs)

    def get_initial(self):
        return super(SubjectUpdateView, self).get_initial()

    def form_invalid(self, form):
        return super(SubjectUpdateView, self).form_invalid(form)

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.save()
        return super(SubjectUpdateView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        ret = super(SubjectUpdateView, self).get_context_data(**kwargs)
        return ret

    def get_context_object_name(self, obj):
        return super(SubjectUpdateView, self).get_context_object_name(obj)

    def render_to_response(self, context, **response_kwargs):
        return super(SubjectUpdateView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(SubjectUpdateView, self).get_template_names()

    def get_success_url(self):
        return reverse("subject_detail", args=(self.object.pk,))


class SubjectDeleteView(DeleteView):
    model = Subject
    template_name = "insy/subject_delete.html"
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    pk_url_kwarg = 'pk'
    context_object_name = "subject"

    def __init__(self, **kwargs):
        return super(SubjectDeleteView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(SubjectDeleteView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        raise Http404

    def post(self, request, *args, **kwargs):
        return super(SubjectDeleteView, self).post(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return super(SubjectDeleteView, self).delete(request, *args, **kwargs)

    def get_object(self, queryset=None):
        return super(SubjectDeleteView, self).get_object(queryset)

    def get_queryset(self):
        return super(SubjectDeleteView, self).get_queryset()

    def get_slug_field(self):
        return super(SubjectDeleteView, self).get_slug_field()

    def get_context_data(self, **kwargs):
        ret = super(SubjectDeleteView, self).get_context_data(**kwargs)
        return ret

    def get_context_object_name(self, obj):
        return super(SubjectDeleteView, self).get_context_object_name(obj)

    def render_to_response(self, context, **response_kwargs):
        return super(SubjectDeleteView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(SubjectDeleteView, self).get_template_names()

    def get_success_url(self):
        return reverse("subject_list")
