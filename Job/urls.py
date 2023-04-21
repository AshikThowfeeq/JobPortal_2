from django.urls import path
from Job import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("signup/",views.SignUpView.as_view(),name="signup"),
    path("",views.SignInView.as_view(),name="signin"),
    path("home/",views.IndexView.as_view(),name="home"),
    path("company/",views.EmployerIndexView.as_view(),name="company-home"),
    path("logout/",views.signout_view,name="signout"),
    path("company/" ,views.CompanyProfileCreateView.as_view(),name="company"),
    path("companydetails/",views.CompanyProfileDetailView.as_view(),name="companydetails"),
    path("companyupdate/",views.CompanyProfileUpdateView.as_view(),name="companyupdate"),
    
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)