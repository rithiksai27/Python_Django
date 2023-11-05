from django.core.paginator import Paginator
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, redirect
from .forms import UserRegisterForm, LoginForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.conf import settings
from .models import Events,Admin
def Homepage(request):

    events = []
    return render(request, 'events/Homepage.html', {'events': events})

def events_list(request):
    event = Events.objects.all()
    paginator = Paginator(event, 4)

    page_number = request.GET.get('page')
    page = paginator.get_page(page_number)

    return render(request, 'events/events_list.html', {'page': page})



def AdminHome(request):
    return render(request, 'events/AdminHome.html')
def UserHome(request):
    return render(request, 'events/UserHome.html')
def eventsAvailable(request):
    return render(request, 'events/eventsAvailable.html')

def index(request):
    return render(request, 'events/index.html')
def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account for {username} created Successfully')
            return redirect('events/Homepage')
    else:
        form = UserRegisterForm()
    return render(request, 'events/register.html', {'form': form})
@login_required
def profile(request):
    return render(request, 'events/profile.html')
def createevent(request):
    if request.method == 'POST':

        event_name = request.POST.get('eventName')
        event_date = request.POST.get('eventDate')
        event_time = request.POST.get('eventTime')
        event_description = request.POST.get('eventDescription')


        event = Events( name=event_name, date=event_date, time=event_time, description=event_description)
        event.save()

    return render(request, 'events/createevent.html')


def payment(request):
    return render(request, 'events/payment.html')

def adminlogin(request):
        if request.method == 'POST':
            form = LoginForm(request.POST)
            if form.is_valid():
                username = form.cleaned_data['username']
                password = form.cleaned_data['password']

                # Verify the user's credentials (assuming Admin is your custom model)
                try:
                    admin = Admin.objects.get(username=username)
                    if admin.password == password:  # Replace with your custom password hashing logic
                        # Password matches
                        # Log in the user or set a session variable
                        # Redirect to the admin profile page
                        return redirect('events/AdminHome')
                    else:
                        return render(request, 'events/adminlogin.html',
                                      {'form': form, 'error_message': 'Invalid login credentials'})
                except Admin.DoesNotExist:
                    return render(request, 'events/adminlogin.html',
                                  {'form': form, 'error_message': 'Invalid login credentials'})
        else:
            form = LoginForm()

        return render(request, 'events/adminlogin.html', {'form': form})



def adminlogout(request):
    return render(request, 'events/adminlogout.html')
def ContactUs(request):
    return render(request, 'events/ContactUs.html')


