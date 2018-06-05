from django.urls import path
from . import views
from rest_framework.documentation import include_docs_urls

from . import views

from rest_framework import routers

urlpatterns = [
    path('search', views.Search, name='home'),
]
