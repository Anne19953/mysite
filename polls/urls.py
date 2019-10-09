#!/usr/bin/env python
# coding:utf-8
"""
Name : urls.py
Author  : anne
Time    : 2019-09-29 15:12
Desc:
"""
from django.urls import path

from . import views
app_name = 'polls'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
]