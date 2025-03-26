from django.shortcuts import render

# Create your views here.
def login(request):
    if request.method == "GET":
        return render(request,"login.html")

def register(request):
    if request.method == "GET":
        return render(request,"register.html")