from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def get_user(request):
    return render(request,'user.html')

def index(request):
    return HttpResponse('This is app 1')