from django.contrib.auth.decorators import login_required
from django.urls import path

from .views import *

app_name = 'core'
urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('results/', login_required(AnswerListView.as_view()), name='results'),
    path('answer/<int:user_id>/create/', AnswerCreateView.as_view(), name='answer-create'),
    path('poll/<int:user_id>/create/', PollCreateView.as_view(), name='poll-create'),
    path('answer/<int:user_id>/get/', AnswerTemplateView.as_view(), name='answer-get'),
    path('poll/<int:user_id>/get/', PollTemplateView.as_view(), name='poll-get'),
    path('answer/<int:user_id>/success/', AnswerSuccessTemplateView.as_view(), name='answer-success'),
    path('poll/<int:user_id>/success/', PollSuccessTemplateView.as_view(), name='poll-success'),

    # path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    # ...
]