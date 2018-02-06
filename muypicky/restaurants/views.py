import random
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
# Function based view

def home(request):
    num = random.randint(0,56)
    some_list = [num,random.randint(0,56), random.randint(0,56)]
    context = {
        "html_var":"html variable filling. kinda like php it woud seem. ||| ",
        "num":num,
        "some_list": some_list,
    }
    return render(request, "base.html", context) #response
