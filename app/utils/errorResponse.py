from django.shortcuts import render,redirect

def errorResponse(request, errorMsg):
    return render(request, "error-404.html.html", {"errorMsg": errorMsg})