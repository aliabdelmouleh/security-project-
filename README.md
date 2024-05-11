"# Savini: a trusted website that generates, checks and stores passwords in a safe way " 
Problem: 
Nowadays protecting our online identity is crucial because hackers are constantly evolving their techniques, and weak passwords are a major vulnerability.
Many people today become victims of cyber-attacks because their passwords aren't strong enough. And even when they try to make them strong , they often forget them.
Our solution:
In fact, we will propose three key services as part of the solution:
1. Password Generation: Offering a service to generate strong passwords that meet security standards OWASP, ensuring users have access to reliable password options.
2. Password Strength Testing and Feedback:Providing users with a tool to assess the strength of their passwords and receive real-time feedback on potential weaknesses.
3. Secure Password Management: Introducing an account-based platform where users can securely store and manage passwords for different online platforms using strong hashing algorithm ensuring easy access while maintaining the highest levels of security.
**   Usage:**
open CMD first .
to run the server : http://127.0.0.1:8000
to run the server as admin : http://127.0.0.1:8000/admin
then : python manage.py runserver
python manage.py createsuperuser
to open the website for the first time 
python manage.py startapp savini
for data base encreption :
pip install cryptography
from cryptography.fernet import fernet
key = fernet.generate_key()
print(key)   --this command will print the encrepted key to settings.py 
