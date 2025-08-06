from django.shortcuts import render
from django.utils import timezone
from datetime import timedelta
from .models import Event

# Create your views here.

def home(request):
    """Home page view with welcome message and upcoming events calendar"""
    today = timezone.now().date()
    upcoming_events = Event.objects.filter(
        date__gte=today
    ).order_by('date', 'start_time')[:10]  # Show next 10 events
    
    featured_events = Event.objects.filter(
        is_featured=True,
        date__gte=today
    ).order_by('date', 'start_time')[:5]  # Show 5 featured events
    
    context = {
        'upcoming_events': upcoming_events,
        'featured_events': featured_events,
        'today': today,
    }
    
    return render(request, 'karaoke/home.html', context)
