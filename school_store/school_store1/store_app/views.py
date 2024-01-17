from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from .models import Department,Course
from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.http import JsonResponse
from django import forms
from .forms import DropdownForm


# Create your views here.
def home(request,c_slug=None):
    c_page=None
    dep=None
    if c_slug != None:
        c_page = get_object_or_404(Department, slug=c_slug)
        dep=Department.objects.all()
    else:
        dep=Department.objects.all()

    return render(request, "index.html",{'c':c_page,'dep':dep})

def dep_det(request,product_slug):
    try:
        prod=Department.objects.get(slug=product_slug)
        print(prod)
    except Exception as e:
        raise e
    return render(request,"team.html",{'product':prod})

def form(request,c_slug=None):
    c_page=None
    dep=None
    if c_slug != None:
        c_page = get_object_or_404(Department, slug=c_slug)
        dep=Course.objects.all()
        country_id = Department.objects.get(slug=c_slug)
        print(country_id)
    else:
        dep=Course.objects.all()


    return render(request, "base.html",{'c':c_page,'dep':dep})

def form_submit(request):




        html = "Form Submitted Successfully" + '<a href = "/" > Return to home </a>'
        return HttpResponse(html)


def load_cities(request):
    department_id = request.GET.get('department_id')
    print (department_id)
    course = Course.objects.filter(department_id=department_id).all()
    return render(request, 'dropdown.html', {'cities': course})
    # return JsonResponse(list(cities.values('id', 'name')), safe=False)






def course(request):
    form = DropdownForm()
    cities = Department.objects.all()
    course = request.GET.get('courses')



    return render(request,"base.html",{'form':form})

def login(request):
    if request.method == 'POST':
            usern=request.POST['username']
            password=request.POST['password']
            user=auth.authenticate(username=usern,password=password)

            if user:
                auth.login(request,user)
                return redirect('/course')
            else:

                messages.info(request,"invalid user")
    return render(request,'login.html')

def register(request):
    if request.method == 'POST':
            name=request.POST['name']
            uname=request.POST['username']
            password=request.POST['password']
            cpassword=request.POST['cpassword']
            if password==cpassword:
                if User.objects.filter(username=uname).exists():
                    messages.info(request,"username already taken")
                    return render(request,"register.html")

                else:
                    user=User.objects.create_user(username=uname,first_name=name,password=password)
                    user.save();
                    return redirect('/login')
                    print("user created")
            else:
                messages.info(request,"password not matching")
                return render(request,"register.html")
            return render(request,"index.html")


    return render(request,'register.html')

def logout(request):
    auth.logout(request)
    return redirect('/')