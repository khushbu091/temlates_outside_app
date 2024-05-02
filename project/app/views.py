from django.shortcuts import render
#from  .views import home
# Create your views here.
def home(request):
    return render(request, "app1/home.html")