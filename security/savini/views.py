from django.shortcuts import render, redirect
from . forms import CreateUserForm, loginForm
from django.contrib.auth.models import auth
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import JsonResponse
import os
import re
from .models import UserData
from django.http import HttpResponse
from django.contrib.auth.hashers import make_password
from django.shortcuts import get_object_or_404
from .forms import ContactForm

from django.conf import settings
from cryptography.fernet import Fernet

f = Fernet(settings.ENCRYPT_KEY)


def homepage(request):
    
    return render(request,'savini/index.html')


def register(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    else:

        form = CreateUserForm()

        if request.method == "POST":

            form = CreateUserForm(request.POST)

            if form.is_valid():

                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request, 'Account was created for ' + user)


                return redirect("my-login")
            
        context = {'form': form}

        return render(request,'savini/register.html', context)


def my_login(request):
    if request.user.is_authenticated:
        return redirect('safe')
    else:
        form = loginForm()

        if request.method == 'POST':
            form = loginForm(data=request.POST)
            if form.is_valid():
                username = form.cleaned_data.get('username')
                password = form.cleaned_data.get('password')
                user = authenticate(request, username=username, password=password)

                if user is not None:
                    auth.login(request, user)
                    return redirect("safe")
            else:
                context = {'form': form, 'login_failure_message': 'Invalid username or password.'}
                return render(request, 'savini/my-login.html', context)
            

        context = {'form': form}

        return render(request, 'savini/my-login.html', context)


def user_logout(request):
    if request.user.is_authenticated:
        auth.logout(request)
        messages.success(request, 'You have logged out.')
    return redirect("")

def body_decrypted(password):
    f = Fernet(settings.ENCRYPT_KEY)
    message_decrypted = f.decrypt(password)
    message_decoded = message_decrypted.decode('utf-8')
    return message_decoded

def dashboard(request):

    return render(request,'savini/dashboard.html')


def suggester(request):

    return render(request,'savini/suggester.html')

@login_required(login_url="my-login")

def safe(request):
        user_data = UserData.objects.filter(user=request.user).first()
        if request.method == 'POST':
            app_name = request.POST.get('app_name')
            password = request.POST.get('password')
            action = request.POST.get('action')  

            if action == "update" :        
                def replace_word(first_string, second_string, specific_word, new_word):
                    first_string_list = first_string.split(' ')
                    second_string_list = second_string.split(' ')
                    try:
                        index = first_string_list.index(specific_word)
                    except ValueError:
                        return second_string

                        
                    message_original= password
                    message_bytes=message_original.encode('utf-8')
                    message_encrypted=f.encrypt(message_bytes)
                    message_decoded=message_encrypted.decode('utf-8')

                    new_word=message_decoded

                    second_string_list[index] = new_word
                    new_second_string = ' '.join(second_string_list)

                    return new_second_string
                
                user_data.password=replace_word(user_data.app_name,user_data.password,app_name,password)
                user_data.save()

            elif action == "delete":

                def remove_word_from_strings(input_string,input_string2,word_to_remove):
                    
                    input_string_list = input_string.split(' ')
                    input_string_list2 = input_string2.split(' ')
                    try:
                        index = input_string_list.index(word_to_remove)
                    except ValueError:
                        return input_string
                    input_string_list.pop(index)
                    input_string_list2.pop(index)

                    new_string = ' '.join(input_string_list)
                    new_string2 = ' '.join(input_string_list2)

                    return new_string,new_string2

                user_data.app_name,user_data.password = remove_word_from_strings(user_data.app_name,user_data.password, app_name)
                user_data.save()


            else :
                if user_data:
                    user_data.app_name = app_name
                    user_data.password = password
                    user_data.save()

                else:
                    UserData.objects.create(user=request.user, app_name=app_name, password=password)
            
        else:

            if (user_data) : 
                ll=user_data.password.split()
                for oo in range(len(ll)) : 
                    ll[oo]=body_decrypted(ll[oo])
                initial_data = {'app_name': user_data.app_name if user_data else '', 'password': (' '.join(ll)) if user_data else ''}
            else : 
                initial_data = {'app_name': user_data.app_name if user_data else '', 'password': (user_data.password) if user_data else ''}

            return render(request, 'savini/safe.html', {'initial_data': initial_data})
        return redirect('safe')



def save_app_data(request):
    if request.method == 'POST' :
        app_name = request.POST.get('app_name')
        password = request.POST.get('password')
        action = request.POST.get('action')  

        if action!="update" and action!="delete" : 
            # Assuming you have a UserData model to store app name and password
            user_data, created = UserData.objects.get_or_create(user=request.user)


            message_original= password
            message_bytes=message_original.encode('utf-8')
            message_encrypted=f.encrypt(message_bytes)
            message_decoded=message_encrypted.decode('utf-8')

            password=message_decoded        

            message_decrypted=f.decrypt(message_decoded)
            message_decoded=message_decrypted.decode('utf-8')

            # Update existing data or create new if it doesn't exist
            if user_data.app_name and user_data.password:
                # If data already exists, append new data with a separator
                user_data.app_name += " " + app_name
                user_data.password += " " + password
            else:
                # If no existing data, just save the new data
                user_data.app_name = app_name
                user_data.password = password

            user_data.save()

            return JsonResponse({'success': True})
    else:
        return JsonResponse({'success': False, 'error': 'Invalid request method'})
    


def contact(request):

    return render(request,'savini/contact.html')

def team(request):

    return render(request,'savini/team.html')

def about(request):

    return render(request,'savini/about.html')

def FAQ(request):

    return render(request,'savini/FAQ.html')

def privacy_policy(request):

    return render(request,'savini/privacy-policy.html')


def contact_form_submit(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('contact')  
    else:
        form = ContactForm()
    return render(request, 'savini/contact.html', {'form': form})