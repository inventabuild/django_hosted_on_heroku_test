from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('invoice_new/', views.invoice_new, name='invoice_new'),
]