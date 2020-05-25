from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse

# Create your views here.

def home(request):
    return render(request, 'loginpage.html')

def sending(request):
    username= request.POST['username']
    password= request.POST['password']
    option = request.POST['requestType']
    if(option=='HTML'):
        return render(request,'new.html',{'username':username,'password':option})
    else:
        return  JsonResponse({'username':username,'password':password})