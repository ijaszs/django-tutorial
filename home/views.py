from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import departments
from .models import doctors
from .forms import BookingForm
def home(request):
    return render(request, 'home.html')


def about(request):
    return render(request, 'about.html', )


def base(request):
    return render(request, 'base.html', )


def booking(request):
    if request.method == "POST":
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request,'confirmation.html')
    form = BookingForm()
    dict_form ={
        'form':form
    }


    return render(request, 'booking.html',dict_form)


def doctorspage(request):
    dict_docs ={
        'doctors': doctors.objects.all()
    }
    return render(request, 'doctors.html',dict_docs)



def department(request):
    dict_dept ={
        'dept': departments.objects.all
    }
    return render(request, 'department.html',dict_dept)



def contact(request):
    return render(request, 'contact.html',)


def index(request):
    return render(request, 'index.html')


