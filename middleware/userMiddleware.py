from django.utils.deprecation import MiddlewareMixin
from django.shortcuts import render,redirect

class UserMiddleware(MiddlewareMixin):
    def process_request(self,request):
        if request.path == "/app/login/" or request.path == "/app/register/":
            return None
        else:
            # '/app/home'
            if not request.session.get("username"):
                return redirect("/app/login/")
            else:
                return None

    def precess_view(self,request,view_func,view_args,view_kwargs):
        return None

    def process_response(self,request,response):
        return response