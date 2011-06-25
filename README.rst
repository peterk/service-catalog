========================
A simple service catalog
========================

The service catalog can be used to display information about available API:s in
an organization.


Installation
------------

1. Install Python 2.7 for you OS

2. Install pip:

   $ curl -O https://raw.github.com/pypa/pip/master/contrib/get-pip.py
   
   $ python get-pip.py

3. Install Django 1.3:
   
   $ pip install django

4. Get the source:
   
   $ git clone https://peterk@github.com/peterk/service-catalog.git

5. Edit katana/settings.py and enter your database settings.

6. Create database tables and indexes:
   
   $ python manage.py syncdb
   
   (create superuser when asked)


7. Start the application:

   $ cd katana

   $ python manage.py runserver

   Now you can open the admin interface in your browser: http://127.0.0.1:8000/admin

License
-------
BSD


