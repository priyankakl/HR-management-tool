from django.shortcuts import render, redirect
from django.http import HttpResponse
from track.models import Employee, Suggestion, Star
from django.contrib.auth.models import User
from django.contrib.auth import login,authenticate,logout
from django.contrib.auth.decorators import login_required
from django.core.mail import EmailMessage
from django.core.mail import send_mail
from django.conf import settings

# Create your views here.

def home(request):
    return render(request, "home.html")

def signup(request):
    if request.method=="POST":
        username=request.POST['username']
        email=request.POST['email']
        password=request.POST['password']
  
        exists=User.objects.filter(username=username).exists()

        if not exists:
            user=User.objects.create_user(username, email, password)
            return render(request, "success_msg.html")
    return render(request, "signup.html")

def signin(request):
    if request.method=="POST":
        username=request.POST['username']
        password=request.POST['password']
        user=authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/dashboard/')
        else:
            return render(request, "invalidlogin.html")
    return render(request, "signin.html")

def signout(request):
    logout(request)
    return redirect('/')

@login_required
def dashboard(request):
    number=Employee.objects.all().count()
    concerns=Suggestion.objects.all().count()
    stars=Star.objects.all().count()
    return render(request, "dashboard.html", {"number":number, "concerns":concerns, "stars":stars} )

@login_required
def directory(request):
    employees=Employee.objects.all()
    return render(request, "directory.html", {"employees":employees})

@login_required
def employee_page(request, ecode):
    employee=Employee.objects.get(ecode=ecode)
    return render(request, "employee.html", {"selected_emp":employee})

@login_required
def add_employee(request):
    if request.method=="POST":
        name=request.POST["name"]
        dob=request.POST["dob"]
        email=request.POST["email"]
        doj=request.POST["doj"]
        ecode=request.POST["ecode"]
        department=request.POST["department"]
        designation=request.POST["designation"]
        location=request.POST["location"]
        new=Employee.objects.create(name=name, ecode=ecode, doj=doj, email=email, dob=dob, department=department, designation=designation, location=location)
        return redirect("/directory/")
    return render(request, "add_employee.html")

@login_required
def edit(request, ecode):
    employee=Employee.objects.get(ecode=ecode)
    if request.method=="POST":
        name=request.POST["name"]
        ecode=request.POST["ecode"]
        doj=request.POST["doj"]
        email=request.POST["email"]
        dob=request.POST["dob"]
        department=request.POST["department"]
        designation=request.POST["designation"]
        location=request.POST["location"]
        employee.name=name
        employee.ecode=ecode
        employee.doj=doj
        employee.email=email
        employee.dob=dob
        employee.department=department
        employee.designation=designation
        employee.location=location
        employee.save()
        return redirect("/directory/")
    return render(request, "edit.html", {"employee":employee})

@login_required
def remove(request, ecode):
    employee=Employee.objects.get(ecode=ecode)
    employee.delete()
    return redirect("/directory/")

@login_required
def remove1(request, subject):
    suggest=Suggestion.objects.get(subject=subject)
    suggest.delete()
    return redirect("/suggestions/")

@login_required
def remove2(request, who):
    star=Star.objects.get(who=who)
    star.delete()
    return redirect("/sotw/")

@login_required
def suggestions(request):
    suggestions=Suggestion.objects.all()
    return render(request, "suggestions.html", {"suggestions":suggestions})

@login_required
def suggestion_form(request):
    if request.method=="POST":
        subject=request.POST["subject"]
        description=request.POST["description"]
        new=Suggestion.objects.create(subject=subject, description=description)
        message = 'Please visit the website for more details'
        msg = EmailMessage("Complaint Lodged", message, to=["priyankaraju22@gmail.com"])
        msg.send()
        return redirect("/suggestions/")     
    return render(request, "suggestion_form.html")

@login_required
def star_of_the_week(request):
    stars=Star.objects.all()
    return render(request, "staroftheweek.html", {"stars":stars})

@login_required
def sotw_form(request):
    if request.method=="POST":
        who=request.POST["who"]
        why=request.POST["why"]
        new=Star.objects.create(who=who, why=why)
        return redirect("/sotw/")
    return render(request, "staroftheweek_form.html")

# def birthday(request):
#     birthday=Employee.objects.order_by('dob')[0]
#     return render(request, "birthday.html", {"birthday":birthday})

# def email(request):
#     subject = 'Complaint has been lodged by an Employee'
#     message = 'Please visit the website for more details'
#     email_from = settings.EMAIL_HOST_USER
#     recipient_list = ['priyankaraju22@gmail.com',]
#     send_mail( subject, message, email_from, recipient_list ),
#     return redirect(request, "emailsuccess.html")

    