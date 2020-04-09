from django.shortcuts import render
from basicForm import forms
# Create your views here.

def index(request):
    return render(request,'users/home.html')
    

def form_name_view(request):
    form = forms.FormName()
      #form = FormName(request.POST)
    return render(request,'basicForm/formpage.html', {'form':form})
    
    