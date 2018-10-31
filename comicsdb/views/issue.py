from functools import reduce
import operator

from django.db.models import Q
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from comicsdb.forms.issue import IssueForm
from comicsdb.models import Issue


PAGINATE = 30


class IssueList(ListView):
    model = Issue
    paginate_by = PAGINATE
    queryset = (
        Issue.objects
        .select_related('series')
    )


class IssueDetail(DetailView):
    model = Issue
    queryset = (
        Issue.objects
        .select_related('series')
    )


class SearchIssueList(IssueList):

    # Currently only searching the Series Name but down the road
    # I'll look at implementing a better search engine.
    def get_queryset(self):
        result = super(SearchIssueList, self).get_queryset()
        query = self.request.GET.get('q')
        if query:
            query_list = query.split()
            result = result.filter(
                reduce(operator.and_,
                       (Q(series__name__icontains=q) for q in query_list)))

        return result


class IssueCreate(CreateView):
    model = Issue
    form_class = IssueForm


class IssueUpdate(UpdateView):
    model = Issue
    form_class = IssueForm


class IssueDelete(DeleteView):
    model = Issue
    template_name = 'comicsdb/confirm_delete.html'
    success_url = reverse_lazy('issue:list', kwargs={'page': 1})