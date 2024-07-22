from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('add_asset/', views.add_asset, name='add_asset'),
    path('existing_assets/', views.existing_assets, name='existing_assets'),
    path('maintenance/', views.maintenance_form, name='maintenance_form'),
    path('maintenance_list/', views.maintenance_list, name='maintenance_list'),
    path('tracking_form/', views.tracking_form, name='tracking_form'),
    path('tracking_list/', views.tracking_list, name='tracking_list'),
    path('asset/<int:asset_id>/', views.asset_detail, name='asset_detail'),
    path('asset/<int:asset_id>/add_maintenance/', views.add_maintenance, name='add_maintenance'),
    path('maintenance/submit/', views.maintenance_submit, name='maintenance_submit'),
]
