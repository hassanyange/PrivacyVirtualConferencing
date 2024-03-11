from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.login_view, name='login'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('meeting-room/', views.meeting_room, name='meeting_room'),
    path('privacy-settings/', views.privacy_settings, name='privacy_settings'),
    path('account-management/', views.account_management, name='account_management'),
    path('help-support/', views.help_support, name='help_support'),
    # Add URLs for other features here
]
