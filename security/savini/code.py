import os
from django.http import JsonResponse

def is_weak_password(password):
    weak_passwords_directory = 'savini/data'
    for filename in os.listdir(weak_passwords_directory):
        filepath = os.path.join(weak_passwords_directory, filename)
        with open(filepath, 'r', encoding='utf-8') as file:  # Specify encoding here
            if password.strip() in file.read().splitlines():
                return True
    return False

def check_password_strength(request):
    if request.method == 'POST':
        password = request.POST.get('password', '')
        weak = is_weak_password(password)
        return JsonResponse({'weak': weak})
    return JsonResponse({})
