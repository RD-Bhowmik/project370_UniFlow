from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from .views import *
urlpatterns = [
    path('', views.mainhome, name="home"),
    path('login/', views.loginPage, name="login"),
    path('after_login/', views.afterLogin, name="after_login"),
    path('register/', views.registerPage, name="register"),
    path('logout/', views.logoutUser, name="logout"),
    
    path('addDonor/', views.add_donor, name='add_donor'),
    path('addedDoner/',views.donor_added, name='donor_added'),

    path('list/', donor_list, name='donor_list'),  # New URL for donor list

    path('reghospital/', views.register_hospital, name='register_hospital'),
    path('hospital_list/', views.hospital_list, name='hospital_list'),

    path('event/add/', views.add_event, name='add_event'),  # Add event
    path('event/<int:event_id>/update/', views.update_event, name='update_event'),  # Update event
    path('event/<int:event_id>/delete/', views.delete_event, name='delete_event'),  # Delete event
    path('events/', views.event_list, name='event_list'),  # Event list

    path('add_blood_request/', views.add_blood_request, name='add_blood_request'),

    path('blood_requests/', views.blood_request_list, name='blood_request_list'),

    path('blood_requests/<int:pk>/update/', views.update_blood_request, name='update_blood_request'),
    path('blood_requests/<int:pk>/delete/', views.delete_blood_request, name='delete_blood_request'),
    path('adminpage/', views.adminPannel, name='admin_panel'),



]