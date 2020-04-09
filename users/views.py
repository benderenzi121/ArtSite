from django.shortcuts import render
from django.http import HttpResponse
from polls.models import Poll
from users import views


def index(request,*args , **kargs):
    print(request.user)
    return HttpResponse("<em>my second proj<em>")
def home(request):
  #  print(request.user.email)
    helpdict = {'help_insert': "HELP PAGE " }
    return render(request,'users/home.html', context = helpdict)
    
def help(request):
   # print(request.user.email)
    
    return render(request,'users/help.html')

def grid(request):
  #  print(request.user.email)
    return render(request,'users/gridView.html')
    
def polls(request):
  #  print(request.user.email)
    user_list = Poll.objects.all()
    user_dict = {'polls' : user_list } 
    return render(request,'users/polls.html', context=user_dict)
    
  
# Create your views here.