from django.shortcuts import render

# Create your views here.
def home(request, month):
    return render(request, 'home.html', )
