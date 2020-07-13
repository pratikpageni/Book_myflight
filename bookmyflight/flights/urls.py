from django.urls import path 
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns



urlpatterns=[
    path("",views.log,name="log"),
    path("login",views.login_view,name="login"),
    path("logout",views.logout_view,name="logout"),
    path("register/",views.registerPage,name="register"),
    path("flights",views.flights_view,name="flights"),
    path("<int:flight_id>",views.flight,name="flight"),
    path("<int:flight_id>/book",views.book,name="book"),
    path("passenger",views.addpassenger,name="addpassenger"),
    path("about",views.aboutus,name="about"),
    path("contact",views.contactus,name="contact"),
    
 
 ]

urlpatterns += staticfiles_urlpatterns()