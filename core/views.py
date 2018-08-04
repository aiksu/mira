from django.shortcuts import render, get_object_or_404

# Create your views here.

from django.shortcuts import render

# Create your views here.
from django.views import View
from django.views.generic import TemplateView, ListView, CreateView, DetailView
from .models import *


# from bug.models import WebsiteBug
# from core.models import Website


class IndexView(TemplateView):
    template_name = "main.html"

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in the website
        if self.request.user.is_authenticated:
            context['answer_list'] = Answer.objects.filter(user = self.request.user)
        return context


class AnswerTemplateView(TemplateView):
    template_name = "core/answer_form.html"

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in the website
        context['target'] = get_object_or_404(User, pk=self.kwargs['user_id'])
        return context


class AnswerCreateView(CreateView):
    model = Answer
    fields = ['answer1', 'answer2', 'answer3']
    # form_class = WebsiteBugForm
    template_name = "core/answer_form.html"

    def form_valid(self, form):
        target = get_object_or_404(User, pk=self.kwargs['user_id'])
        form.instance.user = target

        return super(AnswerCreateView, self).form_valid(form)


class AnswerListView(ListView):
    model = Answer
    paginate_by = 1000  # if pagination is desired

    def get_queryset(self):
        return Answer.objects.filter(user=self.request.user)


# class AnswerDetailView(DetailView):
#     model = Answer


class AnswerSuccessTemplateView(TemplateView):
    template_name = "core/answer_success.html"

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in the website
        context['target'] = get_object_or_404(User, pk=self.kwargs['user_id'])
        return context

