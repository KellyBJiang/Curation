from django.shortcuts import render

# Create your views here.

def curator(request):  
    return render(request, 'stores/basic.html');
def index(request):
    return render(request,'stores/home.html',{'content':['See the datasets assigned to you, please log in','input your user name and password']});