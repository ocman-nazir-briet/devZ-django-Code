from django.http import HttpResponse
from django.shortcuts import redirect, render
from base.models import *
from django.template.loader import render_to_string
from django.core.mail import send_mail
from django.contrib.auth import logout, authenticate, login



def index(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    return HttpResponse('<a href="/login">Login to Dashboard</a>')

def dashboard(request):
    if request.user.is_superuser:
        clients = Client.objects.all()[:100]
    else:
        clients = Client.objects.filter(assignee = request.user)
    return render(request, 'dashboard.html', {'clients': clients, 'user': request.user})

def detail(request, pk):
    if request.user.is_authenticated:
        client = Client.objects.get(id = pk)
        return render(request, 'detail.html', {'client': client})
    else:
        return HttpResponse('<a href="/login">Login to Dashboard</a>')


def loginUser(request):
    if request.method=="POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            return render(request, '404.html')
    else:    
        return render(request, 'login.html')


def logoutUser(request):
    logout(request)
    return redirect("/")



def sendMassMail(request):
    if request.user.is_superuser:           
        clients = Client.objects.filter(is_mailed = False)[:1000]
        count_send = 0
        count_fail = 0
        for c in clients:
            if c.email:
                header = 'DevZol Solutions | Maximize Your Profits and boost productivity with a Cutting-Edge Web or Mobile App.'
                html_message = render_to_string('email.html', {'subject': header, 'company_name':c.company_name})

                email_list = [c.email]

                try:
                    check = send_mail(
                        header,
                        'DevZol Info',
                        'info@devzol.com',
                        email_list,
                        fail_silently=False,
                        html_message=html_message
                    )
                    if check:
                        count_send = count_send + 1
                        print(c.email)
                        print(count_send)
                        print("*****email Successfull *****")
                        c.count = c.count + 1
                        c.is_mailed = True
                        c.save()
                    else:
                        count_fail = count_fail + 1
                        print(count_fail)
                        print("***** Failed Check *****")
                except:
                    count_fail = count_fail + 1
                    print(count_fail)
                    print("***** Failed *****")
    else:
        return HttpResponse("You are not Allowed to send, go back to <a href='/dashboard'>Dashboard</a>")