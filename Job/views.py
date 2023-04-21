from django.shortcuts import render,redirect
from api.models import User,CandidateProfile,CompanyProfile,Job,Application
from Job.forms import RegistrationForm,LoginForm,CompanyProfileForm,JobForm
from django.views.generic import View,CreateView,FormView,TemplateView,UpdateView,ListView
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
                if request.user.role == 'employer':
                    return redirect("company-home")
                elif request.user.role == 'candidate':
                    return redirect("home")
            else:
                return render(request,"login.html",{"form":form})
            

def signout_view(request,*args,**kwargs):
    logout(request)
    return redirect("signin")

class IndexView(TemplateView):
    template_name="index.html"

class EmployerIndexView(TemplateView):
    template_name="company.html"

class CompanyProfileCreateView(CreateView):
    model = CompanyProfile
    form_class = CompanyProfileForm
    template_name ='companyprofile.html'
    success_url = reverse_lazy("companydetails")

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)



class CompanyProfileDetailView(TemplateView):
    template_name='companyprofile_detail.html'



class CompanyProfileUpdateView(UpdateView):
    model=CompanyProfile
    form_class=CompanyProfileForm
    template_name="companyprofile_edit.html"
    success_url=reverse_lazy("company")
    pk_url_kwarg="id"

class JobAddView(CreateView):
    model=Job
    form_class=JobForm
    template_name='job-add.html'
    success_url=reverse_lazy('employer-home')

    def form_valid(self, form):
        company=CompanyProfile.objects.get(user=self.request.user)
        form.instance.company=company
        return super().form_valid(form)

class JobEditView(UpdateView):
    model=Job
    form_class=JobForm
    template_name='job-add.html'
    success_url=reverse_lazy('employer-home')

class JobListView(ListView):
    model=Job
    template_name='job-list.html'
    context_object_name='jobs'

class JobDeleteView(View):
    def get(self,request,*args,**kwargs):
        id=kwargs.get('pk')
        Job.objects.get(id=id).delete()
        return redirect('job-list')

