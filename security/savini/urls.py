from django.urls import path
from . import views
from . import code
from django.contrib import admin
from .views import contact_form_submit


urlpatterns = [
    path('',views.homepage, name=""),
    path('register',views.register, name="register"),
    path('my-login',views.my_login, name="my-login"),
    path('dashboard',views.dashboard, name="dashboard"),
    path('suggester',views.suggester, name="suggester"),
    path('safe',views.safe, name="safe"),
    path('user-logout',views.user_logout, name="user-logout"),
    path('check-password/', code.check_password_strength, name='check_password_strength'),
    path('save_app_data/', views.save_app_data, name='save_app_data'),  
    path('about', views.about, name='about'),
    path('contact', views.contact_form_submit, name='contact'),
    path('FAQ', views.FAQ, name='FAQ'),
    path('team', views.team, name='team'),
    path('privacy-policy', views.privacy_policy, name='privacy-policy'),

]













