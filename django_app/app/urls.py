from django.urls import path
from .views import *

urlpatterns = [
    path("login",login,name="login"),
    path("sigin_up",register,name="sigin_up"),
    path("",home,name="home"),
    path("logout",logout,name="logout"),
    
]
