from django.shortcuts import render, redirect
from app.models import User
from django.http import HttpResponse
from app.utils import errorResponse, getChangeSelfInfoData
from app.utils.getHomeData import getHomeData
import json


def login(request):
    if request.method == "GET":
        return render(request, "login.html")
    else:
        username = request.POST.get("username")
        password = request.POST.get("password")
        try:
            user = User.objects.get(username=username)
            if user.password == password:
                request.session["username"] = username
                return redirect("/app/home")
            else:
                return errorResponse.errorResponse(request, "密码错误")
        except User.DoesNotExist:
            return errorResponse.errorResponse(request, "用户名不存在")


def register(request):
    if request.method == "GET":
        return render(request, "register.html")
    else:
        username = request.POST.get("username")
        password = request.POST.get("password")
        confirmPassword = request.POST.get("confirmPassword")
        try:
            User.objects.get(username=username)
        except:
            if not username or not password or not confirmPassword:
                return errorResponse.errorResponse(request, "用户名或密码不能为空")
            if password != confirmPassword:
                return errorResponse.errorResponse(request, "两次输入密码不一致")
            User.objects.create(username=username, password=password)
            return redirect("/app/login")
        return errorResponse.errorResponse(request, "该账号已存在")


def logOut(request):
    request.session.clear()
    return redirect("/app/login")


def home(request):
    username = request.session.get("username")
    userInfo = User.objects.get(username=username)
    highest_consumption_city = getHomeData.get_highest_consumption_city()
    highest_consumption_city_by_total_spend = getHomeData.get_highest_consumption_city_by_total_spend()
    most_common_product_category = getHomeData.get_most_common_product_category()
    top_10_cities_by_consumption = getHomeData.get_top_10_cities_by_consumption()
    sales_proportion_by_product_type = getHomeData.get_sales_proportion_by_product_type()
    monthly_sales = getHomeData.get_monthly_sales()
    year, month, day = getHomeData.getNowTime()

    # 将数据序列化为 JSON 字符串，确保模板中能正确解析
    top_10_cities_json = json.dumps(top_10_cities_by_consumption)

    return render(request, "home.html", {
        'userInfo': userInfo,
        'highest_consumption_city': highest_consumption_city,
        'highest_consumption_city_by_total_spend': highest_consumption_city_by_total_spend,
        'most_common_product_category': most_common_product_category,
        'top_10_cities_by_consumption': top_10_cities_by_consumption,
        'sales_proportion_by_product_type': sales_proportion_by_product_type,
        'monthly_sales': monthly_sales,
        'nowTime': {
            'year': year,
            'month': month,
            'day': day
        }
    })


def chargeSelfInfo(request):
    username = request.session.get("username")
    userInfo = User.objects.get(username=username)
    year, month, day = getHomeData.getNowTime()
    if request.method == "POST":
        getChangeSelfInfoData.changeSelfInfo(username, request.POST, request.FILES)

    return render(request, "chargeSelfInfo.html", {
        'userInfo': userInfo,
        'nowTime': {
            'year': year,
            'month': month,
            'day': day
        }
    })

def changePassword(request):
    username = request.session.get("username")
    userInfo = User.objects.get(username=username)
    year, month, day = getHomeData.getNowTime()
    if request.method == "POST":
        res = getChangeSelfInfoData.getChangePassword(userInfo,request.POST)
        if res != None:
            return errorResponse.errorResponse(request,res)

    return render(request, "changePassword.html", {
        'userInfo': userInfo,
        'nowTime': {
            'year': year,
            'month': month,
            'day': day
        }
    })