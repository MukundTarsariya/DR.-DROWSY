from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpResponse

#Dashborad page route
def index_show(request):
   return render(request, 'index.html')

#Login page route
def pagelogin_show(request):
   return render(request, 'page_login.html')

#SignUp page route
def pageregister_show(request):
   return render(request, 'page_register.html')



