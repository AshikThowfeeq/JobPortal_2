from django.shortcuts import render,redirect
from api.models import User
from Job.forms import RegistrationForm,LoginForm
from django.views.generic import View,CreateView,FormView,TemplateView
from django.urls import reverse_lazy
from django.contrib.auth import authenticate,login,logout

class SignUpView(CreateView):

    model=User
    form_class=RegistrationForm
    template_name="register.html"
    success_url=reverse_lazy("signin")

    def form_valid(self, form):
        form.instance.role=form.cleaned_data['role']
        return super().form_valid(form)


class SignInView(FormView):
    form_class=LoginForm
    template_name="login.html"

    def post(self,request,*args,**kw):
        form=LoginForm(request.POST)
        if form.is_valid():
            usrn=form.cleaned_data.get("username")
            passw=form.cleaned_data.get("password")
            usr=authenticate(request,username=usrn,password=passw)
            if usr:
                login(request,usr)
                return redirect("home")
            else:
                return render(request,"login.html",{"form":form})
            

def signout_view(request,*args,**kwargs):
    logout(request)
    return redirect("signin")

class IndexView(TemplateView):
    template_name="index.html"