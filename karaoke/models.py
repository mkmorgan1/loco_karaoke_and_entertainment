from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Event(models.Model):
    EVENT_TYPE_CHOICES = [
        ('karaoke', 'Karaoke Night'),
        ('live_music', 'Live Music'),
        ('comedy', 'Comedy Night'),
        ('dance', 'Dance Party'),
        ('special', 'Special Event'),
    ]
    
    title = models.CharField(max_length=200)
    description = models.TextField()
    event_type = models.CharField(max_length=20, choices=EVENT_TYPE_CHOICES, default='karaoke')
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    location = models.CharField(max_length=200, default='Main Stage')
    capacity = models.PositiveIntegerField(blank=True, null=True)
    is_featured = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.title} - {self.date}"
    
    class Meta:
        ordering = ['date', 'start_time']
