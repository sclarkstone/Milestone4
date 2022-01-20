## setup
'pip3 install Django==3.2' to install Django
'django-admin startproject milestone4 .' to set up basic folder structure and files for Django
'touch .gitignore' to create ignore file and then add to file *.sqlite3, *.pyc

python3 manage.py runserver to check it is runner as expected. a Django screen will appear on the browser with the message 'The install worked successfully! Congratulations!
You are seeing this page because DEBUG=True is in your settings file and you have not configured any URLs.'

stop the server then 'python3 manage.py migrate'
'python3 manage.py createsuperuser', input a username (sclarkstone7153), email (samclarkstone@hotmail.com) and password (Unicorn2001)