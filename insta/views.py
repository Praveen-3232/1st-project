from django.shortcuts import render
from django.http import HttpResponse
from .forms import userprofileform,portfolioform
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponse,HttpResponseRedirect

def HOME(request):
    return HttpResponse("index page")
@login_required
def USER_LOGOUT(request):
    logout(request)
    return HttpResponseRedirect(reverse('user_login'))

@login_required
def SAM(request):
    return HttpResponse("MAIN PAGE")

def TEMP1(request):
    cone={'key':"hello world"}
    return render(request,'newtemp.html',cone)

def REGISTER(request):
    if request.method=='POST':
        user_form=userprofileform(request.POST)
        p_form= portfolioform(request.POST)
        if user_form.is_valid() and p_form.is_valid():
            user=user_form.save(commit=False)
            user.set_password(user_form.cleaned_data['password'])
            user.save()
            portfolio=p_form.save(commit=False)
            portfolio.user=user

            if 'profile_pic' in request.FILES:
                portfolio.profile_pic= request.FILES['profile_pic']
            else:
                print("no files")
            portfolio.save()
        else:print('form is not valid')
    else:
        user_form=userprofileform()
        p_form=portfolioform()
    cone={'user_form':user_form,'pform':p_form}
    return render(request,'register.html',cone)


def USER_LOGIN(request):
    if request.method=='POST':
        uname=request.POST.get('U_name')
        password= request.POST.get('password')
        user=authenticate(username=uname,password=password)
        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('register'))
            else:
                return HttpResponse('Account_inactive')
        else:
            print(f"some one try to login but failed username={uname},password={password}")
            return HttpResponse('invalid credentials')

    else:
        return render(request,"login.html")

def SAMPLE(request):
    return render(request,'Sample.html')