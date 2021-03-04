from django.shortcuts import render, HttpResponse
from home import models
# Create your views here.

def home(request):
    # return HttpResponse("This is my homepage (/)")
    context = {'name': 'Praveen', 'course': 'django'}
    return render(request, 'home.html', context)

def about(request):
    # return HttpResponse("Thid is my aboutpage (/about)")
    return render(request, 'about.html')

def projects(request):
    # return HttpResponse("Thid is my projectspage (/projects)")
    return render(request, 'projects.html')

def contact(request):
    if request.method=="POST":
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        # password = request.POST['password']
        desc = request.POST['desc']
        # print(name, email, phone, password, desc)
        ins = models.Contact(name=name, email=email, phone=phone, desc=desc)
        ins.save()
        print('database updated')
    # return HttpResponse("Thid is my contactpage (/contact)")
    return render(request, 'contact.html')

def register(request):
    return render(request, 'register.html')