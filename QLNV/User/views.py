from django.shortcuts import render

# Create your views here.
def get_user(request):
    return render(request,'user.html')