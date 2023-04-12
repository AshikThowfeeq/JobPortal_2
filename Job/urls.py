from django.urls import path
from Job import views

urlpatterns = [
    path("signup/",views.SignUpView.as_view(),name="signup"),
    path("",views.SignInView.as_view(),name="signin"),
    path("home/",views.IndexView.as_view(),name="home"),
    path("logout/",views.signout_view,name="signout"),
]