from django.shortcuts import render
# from django.contrib import messages, auth
# from django.contrib.auth.models import User
# from django.shortcuts import render, redirect
#
# # Create your views here.
# def register(request):
#
#     if request.method=='POST':
#         usern=request.POST['username']
#         fname=request.POST['first_name']
#         lname=request.POST['last_name']
#         email=request.POST['email']
#         password=request.POST['password']
#         cpassword=request.POST['cpassword']
#         if password==cpassword:
#             if User.objects.filter(username=usern).exists():
#                 messages.info(request,"username already taken")
#                 return redirect('register')
#             elif User.objects.filter(email=email).exists():
#                 messages.info(request,"email already used")
#                 return redirect('register')
#             else:
#                 user=User.objects.create_user(username=usern,password=password,first_name=fname,last_name=lname,email=email)
#                 user.save();
#                 return redirect('login')
#                 print("user created")
#         else:
#             messages.info(request,"password not matching")
#             return redirect('register')
#         return redirect('/')
#
#     return render(request,"reg_index.html")
#
#
# def login(request):
#     if request.method=='POST':
#         usern=request.POST['username']
#         password=request.POST['password']
#         user=auth.authenticate(username=usern,password=password)
#
#         if user:
#             auth.login(request,user)
#             return redirect('/')
#         else:
#
#             messages.info(request,"invalid user")
#
#
#     return render(request,"login_index.html")
#
#
def register(request):
    return render(request,"register.html")