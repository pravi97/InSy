from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from ..models import Academic_History
from ..forms import Academic_HistoryForm
from django.core.urlresolvers import reverse_lazy
from django.core.urlresolvers import reverse
from django.http import Http404


class Academic_HistoryListView(ListView):
    model = Academic_History
    template_name = "insy/academic_history_list.html"
    paginate_by = 20
    context_object_name = "academic_history_list"
    allow_empty = True
    page_kwarg = 'page'
    paginate_orphans = 0

    def __init__(self, **kwargs):
        return super(Academic_HistoryListView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(Academic_HistoryListView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(Academic_HistoryListView, self).get(request, *args, **kwargs)

    def get_queryset(self):
        return super(Academic_HistoryListView, self).get_queryset()

    def get_allow_empty(self):
        return super(Academic_HistoryListView, self).get_allow_empty()

    def get_context_data(self, *args, **kwargs):
        ret = super(Academic_HistoryListView, self).get_context_data(*args, **kwargs)
        return ret

    def get_paginate_by(self, queryset):
        return super(Academic_HistoryListView, self).get_paginate_by(queryset)

    def get_context_object_name(self, object_list):
        return super(Academic_HistoryListView, self).get_context_object_name(object_list)

    def paginate_queryset(self, queryset, page_size):
        return super(Academic_HistoryListView, self).paginate_queryset(queryset, page_size)

    def get_paginator(self, queryset, per_page, orphans=0, allow_empty_first_page=True):
        return super(Academic_HistoryListView, self).get_paginator(queryset, per_page, orphans=0, allow_empty_first_page=True)

    def render_to_response(self, context, **response_kwargs):
        return super(Academic_HistoryListView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(Academic_HistoryListView, self).get_template_names()


class Academic_HistoryDetailView(DetailView):
    model = Academic_History
    template_name = "insy/academic_history_detail.html"
    context_object_name = "academic_history"
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    pk_url_kwarg = 'pk'

    def __init__(self, **kwargs):
        return super(Academic_HistoryDetailView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(Academic_HistoryDetailView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(Academic_HistoryDetailView, self).get(request, *args, **kwargs)

    def get_object(self, queryset=None):
        return super(Academic_HistoryDetailView, self).get_object(queryset)

    def get_queryset(self):
        return super(Academic_HistoryDetailView, self).get_queryset()

    def get_slug_field(self):
        return super(Academic_HistoryDetailView, self).get_slug_field()

    def get_context_data(self, **kwargs):
        ret = super(Academic_HistoryDetailView, self).get_context_data(**kwargs)
        return ret

    def get_context_object_name(self, obj):
        return super(Academic_HistoryDetailView, self).get_context_object_name(obj)

    def render_to_response(self, context, **response_kwargs):
        return super(Academic_HistoryDetailView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(Academic_HistoryDetailView, self).get_template_names()


class Academic_HistoryCreateView(CreateView):
    model = Academic_History
    form_class = Academic_HistoryForm
    # fields = ['university_roll_no', 'semester', 'month_of_registration', 'Whether_condonation_availed']
    template_name = "insy/academic_history_create.html"
    success_url = reverse_lazy("academic_history_list")

    def __init__(self, **kwargs):
        return super(Academic_HistoryCreateView, self).__init__(**kwargs)

    def dispatch(self, request, *args, **kwargs):
        return super(Academic_HistoryCreateView, self).dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(Academic_HistoryCreateView, self).get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return super(Academic_HistoryCreateView, self).post(request, *args, **kwargs)

    def get_form_class(self):
        return super(Academic_HistoryCreateView, self).get_form_class()

    def get_form(self, form_class=None):
        return super(Academic_HistoryCreateView, self).get_form(form_class)

    def get_form_kwargs(self, **kwargs):
        return super(Academic_HistoryCreateView, self).get_form_kwargs(**kwargs)

    def get_initial(self):
        return super(Academic_HistoryCreateView, self).get_initial()

    def form_invalid(self, form):
        return super(Academic_HistoryCreateView, self).form_invalid(form)

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.save()
        return super(Academic_HistoryCreateView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        ret = super(Academic_HistoryCreateView, self).get_context_data(**kwargs)
        return ret

    def render_to_response(self, context, **response_kwargs):
        return super(Academic_HistoryCreateView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(Academic_HistoryCreateView, self).get_template_names()

    def get_success_url(self):
        return reverse("academic_history_detail", args=(self.object.pk,))


class Academic_HistoryUpdateView(UpdateView):
    model = Academic_History
    form_class = Academic_HistoryForm
    # fields = ['university_roll_no', 'semester', 'month_of_registration', 'Whether_condonation_availed']
    template_name = "insy/academic_history_update.html"
    initial = {}
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    pk_url_kwarg = 'pk'
    context_object_name = "academic_history"

    def __init__(self, **kwargs):
        return super(Academic_HistoryUpdateView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(Academic_HistoryUpdateView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(Academic_HistoryUpdateView, self).get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return super(Academic_HistoryUpdateView, self).post(request, *args, **kwargs)

    def get_object(self, queryset=None):
        return super(Academic_HistoryUpdateView, self).get_object(queryset)

    def get_queryset(self):
        return super(Academic_HistoryUpdateView, self).get_queryset()

    def get_slug_field(self):
        return super(Academic_HistoryUpdateView, self).get_slug_field()

    def get_form_class(self):
        return super(Academic_HistoryUpdateView, self).get_form_class()

    def get_form(self, form_class=None):
        return super(Academic_HistoryUpdateView, self).get_form(form_class)

    def get_form_kwargs(self, **kwargs):
        return super(Academic_HistoryUpdateView, self).get_form_kwargs(**kwargs)

    def get_initial(self):
        return super(Academic_HistoryUpdateView, self).get_initial()

    def form_invalid(self, form):
        return super(Academic_HistoryUpdateView, self).form_invalid(form)

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.save()
        return super(Academic_HistoryUpdateView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        ret = super(Academic_HistoryUpdateView, self).get_context_data(**kwargs)
        return ret

    def get_context_object_name(self, obj):
        return super(Academic_HistoryUpdateView, self).get_context_object_name(obj)

    def render_to_response(self, context, **response_kwargs):
        return super(Academic_HistoryUpdateView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(Academic_HistoryUpdateView, self).get_template_names()

    def get_success_url(self):
        return reverse("academic_history_detail", args=(self.object.pk,))


class Academic_HistoryDeleteView(DeleteView):
    model = Academic_History
    template_name = "insy/academic_history_delete.html"
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    pk_url_kwarg = 'pk'
    context_object_name = "academic_history"

    def __init__(self, **kwargs):
        return super(Academic_HistoryDeleteView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(Academic_HistoryDeleteView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        raise Http404

    def post(self, request, *args, **kwargs):
        return super(Academic_HistoryDeleteView, self).post(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return super(Academic_HistoryDeleteView, self).delete(request, *args, **kwargs)

    def get_object(self, queryset=None):
        return super(Academic_HistoryDeleteView, self).get_object(queryset)

    def get_queryset(self):
        return super(Academic_HistoryDeleteView, self).get_queryset()

    def get_slug_field(self):
        return super(Academic_HistoryDeleteView, self).get_slug_field()

    def get_context_data(self, **kwargs):
        ret = super(Academic_HistoryDeleteView, self).get_context_data(**kwargs)
        return ret

    def get_context_object_name(self, obj):
        return super(Academic_HistoryDeleteView, self).get_context_object_name(obj)

    def render_to_response(self, context, **response_kwargs):
        return super(Academic_HistoryDeleteView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(Academic_HistoryDeleteView, self).get_template_names()

    def get_success_url(self):
        return reverse("academic_history_list")
