from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpResponse

def index_show(request):
   return render(request, 'index.html')

def pagelogin_show(request):
   return render(request, 'page_login.html')

def pageregister_show(request):
   return render(request, 'page_register.html')



