from django.shortcuts import render,redirect
from app.models import User,History
from django.http import HttpResponse
from app.utils import errorResponse

# Create your views here.
def login(request):
    if request.method == "GET":
        return render(request,"login.html")
    else:
        username = request.POST.get("username")
        password = request.POST.get("password")
        try:
            user = User.objects.get(username = username)
        except:
            return errorResponse.errorResponse(request,"用户名不存在")
        if user.password == password:
            request.session["username"] = username
            return redirect("/app/index")
        return errorResponse.errorResponse(request,"密码错误")

def register(request):
    if request.method == "GET":
        return render(request,"register.html")
    else:
        username = request.POST.get("username")
        password = request.POST.get("password")
        confirmPassword = request.POST.get("confirmPassword")
        try:
            User.objects.get(username = username)
        except:
            if not username or not password or not confirmPassword:
                return HttpResponse("用户名或密码不能为空")
            if password != confirmPassword:
                return HttpResponse("两次输入密码不一致")
            User.objects.create(username = username,password = password)
            return redirect("/app/login")
        return HttpResponse("该账号已存在")