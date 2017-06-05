from django.shortcuts import render, HttpResponse, redirect
from .models import UserDB, AppointDB
from django.contrib import messages
import datetime
# Create your views here.

def index(request):
    return render(request, "appoint/index.html")

def log_register(request):
    if request.method == "POST":
        print request.POST["type"] * 10
        if request.POST["type"] == 'Register':
            response = UserDB.objects.check_create(request.POST)
        elif request.POST['type'] == "Login":
            response = UserDB.objects.check_log(request.POST)
        if not response[0]:
            for message in response[1]:
                messages.error(request, message[1])
            return redirect('appoint:index')
        else:
            request.session['user'] = {
            "id":response[1].id,
            'username': response[1].username,
            }
            return redirect('appoint:appointments')
    return redirect('appoint:index')

def appointments(request):
    today = datetime.date.today()
    today_appoint = AppointDB.objects.filter(date=today)
    other_appoint = AppointDB.objects.filter(date__gte=today)
    context = {
    "today_appoint": today_appoint,
    "other_appoint": other_appoint
    }
    return render(request,'appoint/appointment.html',context)

def addappoint(request):
    response = AppointDB.objects.create(request.POST,request.session['user']['id'])
    if not response[0]:
        for message in response[1]:
            messages.error(request, message[1])
    return redirect('appoint:appointments')

def logout(request):
	request.session.clear()
	return redirect('appoint:index')

def edit(request,id):
    return render(request,'appoint/update.html')

def delete(request,id):
    if request.method == "GET":
        id = request.GET.get('id')
        print id
        print id
        print id
        print id
        print id
        print id
        print id
    # response = AppointDB.objects.delete(id)
    return redirect('appoint:appointments')
