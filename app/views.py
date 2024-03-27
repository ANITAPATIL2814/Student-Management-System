from django.shortcuts import render,redirect,HttpResponse
from app.EmailBackEnd import EmailBackEnd
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from app.models import CustomUser
# Create your views here.
def base(request):
     return render(request,'base.html')
def LOGIN(request):
     return render(request,'login.html')

def doLogin(request):
     if request.method == "POST":
          user=EmailBackEnd.authenticate(request,
               username=request.POST.get('email'), 
            password=request.POST.get('password'),) # this email and password from our login page input field ka name name="email"
          if user!=None:
               login(request, user)
               user_type = user.user_type
               if user_type == '1':
                    return redirect('Hod_home')
               elif user_type == '2':
                    return redirect('staff_home')
               elif user_type == '3':
                    return redirect('student_home')
               else:
                    messages.error(request,'Email and password are Invalid !!')
                    return redirect('login')
          else:
               messages.error(request,'Email and password are Invalid !!')
               return redirect('login'
                               )
def doLogout(request):
     logout(request)
     return redirect('login') #redirect on login page

#for profile
@login_required(login_url='/')
def PROFILE(request):
     user = CustomUser.objects.get(id = request.user.id)
     # print(user) #print the which user is login
     context ={
          "user":user,
     }
     return render(request,'profile.html',context)

#to update profile
@login_required(login_url='/')
def PROFILE_UPDATE(request):
     if request.method == "POST":
          profile_pic=request.FILES.get('profile_pic') #to fetch data from database here we fetch all admin data 
          first_name=request.POST.get('first_name')
          last_name=request.POST.get('last_name')
          password=request.POST.get('password')
     try:
          Customuser = CustomUser.objects.get(id = request.user.id) #when we want to update data  in django we nedd id
          Customuser.first_name = first_name
          Customuser.last_name = last_name
          if profile_pic !=None and profile_pic != "" :
              Customuser.profile_pic = profile_pic
          if password !=None and password != "" :
               Customuser.set_password(password) 
          Customuser.save()
          messages.success(request,'Your Profile Updated Successfully !!')
          return redirect('profile')
     except:
          messages.error(request, 'Failed To Update Profile')
     return render (request,'profile.html')
