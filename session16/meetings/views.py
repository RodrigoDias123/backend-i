from django.shortcuts import render

from meetings.models import Meeting

def index(request):
    meetings = list(Meeting.objects.all())
    return render(request, "meetings/index.html",{"meetings": meetings})