# pevcp/views.py
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.utils import timezone 
from .models import Event


def homepage(request):
    return render(request, 'homepage.html')

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('dashboard')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # Redirect to the dashboard after successful login
            return redirect('dashboard')
        else:
            # Handle invalid login credentials
            return render(request, 'login.html', {'error': 'Invalid username or password'})
    else:
        return render(request, 'login.html')


@login_required
def dashboard(request):
    # Retrieve user's profile information
    user = request.user

    # Retrieve recent activity (example: last 5 events)
    recent_activity = Event.objects.filter(user=user).order_by('-created_at')[:5]

    # Retrieve upcoming events (example: next 5 events)
    upcoming_events = Event.objects.filter(user=user, date__gte=timezone.now()).order_by('date')[:5]

    context = {
        'user': user,
        'recent_activity': recent_activity,
        'upcoming_events': upcoming_events,
    }
    return render(request, 'dashboard.html', context)
def meeting_room(request):
    return render(request, 'meeting_room.html')

@login_required
def privacy_settings(request):
    return render(request, 'privacy_settings.html')

@login_required
def account_management(request):
    return render(request, 'account_management.html')

def help_support(request):
    return render(request, 'help_support.html')
