from django import forms
from .models import Asset, Maintenance, TrackingMovement

class TrackingForm(forms.ModelForm):
    class Meta:
        model = TrackingMovement
        fields = ['asset', 'previous_location', 'new_location', 'tracking_date', 'comments']
        widgets = {
            'asset': forms.Select(attrs={'class': 'form-control'}),
            'previous_location': forms.TextInput(attrs={'class': 'form-control'}),
            'new_location': forms.TextInput(attrs={'class': 'form-control'}),
            'tracking_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'comments': forms.Textarea(attrs={'class': 'form-control'}),
        }

class AssetForm(forms.ModelForm):
    ASSET_CHOICES = [
        ('Laptops', 'Laptops'),
        ('Desktops', 'Desktops'),
        ('Extensions', 'Extensions'),
        ('Banners', 'Banners'),
        ('Screens', 'Screens'),
    ]
    
    asset_type = forms.ChoiceField(
        choices=ASSET_CHOICES,
        required=True,
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    
    class Meta:
        model = Asset
        fields = ['name', 'asset_type', 'description', 'location']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'location': forms.TextInput(attrs={'class': 'form-control'}),
        }
        help_texts = {
            'name': 'Enter the name of the asset.',
            'description': 'Provide a brief description of the asset.',
            'location': 'Specify the location of the asset.',
        }

class MaintenanceForm(forms.ModelForm):
    class Meta:
        model = Maintenance
        fields = ['asset', 'maintenance_date', 'description', 'category']
        widgets = {
            'asset': forms.Select(attrs={'class': 'form-control'}),
            'maintenance_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'category': forms.Select(attrs={'class': 'form-control'}),
        }
        help_texts = {
            'maintenance_date': 'Select the date of maintenance.',
            'description': 'Provide details about the maintenance.',
            'category': 'Select the category of the asset.',
        }
