from django.shortcuts import redirect
from django.utils.deprecation import MiddlewareMixin

class CustomAuth(MiddlewareMixin):
    def process_request(self,request):
        url=request.path
        if "admin" in url: #allow all admin urls
            url="admin"
        if url and not url=="/":
            url=url.replace("/","")
        if self.is_authenticated(request):
            self.get_response(request)
        else:
            if url in ["sigin_up","login","admin"]:
                self.get_response(request)
            else:
                return redirect("login")
    def is_authenticated(self,request):
        try:
            if request.session["user"]:
                return True
            else:
                return False
        except:
            request.session["user"]=None
            return False
            
            