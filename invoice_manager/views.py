from django.shortcuts import render
from . import models

# Create your views here.
def invoice_new(request):
    return render(request, 'invoice_manager/invoice_new.html')