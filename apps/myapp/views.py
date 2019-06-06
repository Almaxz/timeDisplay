from django.shortcuts import render
from time import strftime

# Create your views here.
def index(request):
    context = {
        "date": strftime("%a, %m-%d-%Y "),
        "time": strftime("%H:%M %p")
    }
    return render(request,'myapp/index.html', context)