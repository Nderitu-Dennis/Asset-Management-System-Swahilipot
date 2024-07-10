# AMS/views.py

from django.shortcuts import render
from django.http import HttpResponse
from .models import MaintenanceRequest

def maintenance(request):
    if request.method == 'POST':
        category = request.POST['category']
        asset_id = request.POST['id']
        comments = request.POST['comments']
        
        # Save the data to the database
        MaintenanceRequest.objects.create(category=category, asset_id=asset_id, comments=comments)
        
        return HttpResponse('Form submitted successfully!')
    
    return render(request, 'maintenance.html')
