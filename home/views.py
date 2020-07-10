from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import logout,authenticate,login

# Create your views here.


def landing(request):
    if request.user.is_anonymous:
       return render(request,"welcome.html")

    return render(request, 'landing.html')


def loginuser(request):
    if request.method == "POST":
           username = request.POST.get('username')
           password = request.POST.get('password')
           print(username,password)
           user = authenticate(username=username, password=password)
           if user is not None:
               login(request ,user )
               return render(request,'index.html')       
           else:
                  return redirect('/loginuser')
               
    return render(request, 'login.html')



def logoutuser(request):
    logout(request)
    print(logout(request))
    return redirect("/loginuser")
