from django.urls import path 
from . import views


urlpatterns=[
    path("",views.log,name="log"),
    path("login",views.login_view,name="login"),
    path("logout",views.logout_view,name="logout"),
    path("signup",views.signup_view,name="signup"),
   
    path("flights",views.index,name="index"),
    path("<int:flight_id>",views.flight,name="flight"),
    path("<int:flight_id>/book",views.book,name="book")
 
 ]