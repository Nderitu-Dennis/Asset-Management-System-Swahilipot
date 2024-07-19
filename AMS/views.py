from django.shortcuts import render, redirect, get_object_or_404
from django.utils.timezone import now
from .models import Asset, Maintenance, TrackingMovement
from .forms import AssetForm, MaintenanceForm, TrackingForm

def dashboard(request):
    assets = Asset.objects.all()
    maintenance_records = Maintenance.objects.all()
    return render(request, 'dashboard.html', {'assets': assets, 'maintenance_records': maintenance_records})

def add_asset(request):
    if request.method == 'POST':
        form = AssetForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('existing_assets')
    else:
        form = AssetForm()
    return render(request, 'add_asset.html', {'form': form})

def existing_assets(request):
    assets = Asset.objects.all()
    return render(request, 'existing_assets.html', {'assets': assets})

def maintenance_form(request):
    if request.method == 'POST':
        form = MaintenanceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('maintenance_list')
    else:
        form = MaintenanceForm()
    maintenance_records = Maintenance.objects.all()
    return render(request, 'maintenance.html', {'form': form, 'maintenance_records': maintenance_records})

def maintenance_list(request):
    maintenance_records = Maintenance.objects.all()
    return render(request, 'maintenance_request.html', {'maintenance_records': maintenance_records})

def tracking_form(request):
    today = now().date()
    if request.method == 'POST':
        form = TrackingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('tracking_list')  # Redirect to the tracking list after form submission
    else:
        form = TrackingForm()

    movements = TrackingMovement.objects.all()
    return render(request, 'tracking_form.html', {
        'form': form,
        'movements': movements,
        'today': today,
    })

def tracking_list(request):
    tracked_assets = TrackingMovement.objects.all()  # Correct model used here
    return render(request, 'tracking_list.html', {'tracked_assets': tracked_assets})

def asset_detail(request, asset_id):
    asset = get_object_or_404(Asset, pk=asset_id)
    return render(request, 'asset_detail.html', {'asset': asset})

def add_maintenance(request, asset_id):
    asset = get_object_or_404(Asset, pk=asset_id)
    if request.method == 'POST':
        form = MaintenanceForm(request.POST)
        if form.is_valid():
            maintenance_record = form.save(commit=False)
            maintenance_record.asset = asset
            maintenance_record.save()
            return redirect('asset_detail', asset_id=asset.id)
    else:
        form = MaintenanceForm()
    return render(request, 'maintenance.html', {'form': form, 'asset': asset})

def maintenance_submit(request):
    if request.method == 'POST':
        form = MaintenanceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('maintenance_list')
    else:
        form = MaintenanceForm()
    
    maintenance_records = Maintenance.objects.all()
    return render(request, 'maintenance_request.html', {
        'form': form,
        'maintenance_records': maintenance_records,
    })
