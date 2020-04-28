############ SET-UP
## py -3 -m venv pizza_venv
## pizza_venv/scripts/activate
## pip install django

############ BHOJWANI INSTRUCTIONS:
#Start a new project called Pizzeria with an app called pizzas.

#Define a model Pizza with a field called name, which will hold name values, such as Hawaiian and Meat Lovers.

#Define a model called Topping with fields called pizza and name. The pizza field should be a foreign key to Pizza, 
# and name should be able to hold values such as pineapple, Canadian bacon, and sausage.

#Register both models with the admin site, and use the site to enter some pizza names and toppings.

#Pizzeria Home Page: Add a creative home page to your project to replace the Django default home page

#Add a page to the project that shows the names of available pizzas. Then link each pizza name to
# a page displaying the pizza and its pizza’s toppings (add pictures if you can!)

#Create a form that allows users to post comments on any particular pizza page

############ CREATE THE DJANGO PROJECT
# Create a new project called Pizzeria:
### django-admin startproject Pizzeria .
# Dot is important!! Creates it with a directory structure.

############ CREATE THE DATABASE
### py manage.py migrate

############ VIEW THE PROJECT
# Verify that everything is set up correctly:
### py manage.py runserver
# Click http://127.0.0.1:8000/ to check
# Press CTRL+C in terminal window to quit

############ CREATE A DEBUGGER LAUNCH PROFILE
## Switch to Run view to create launch.json.
## Just choose Django in the drop-down and save.

############ STARTING AN APP
### py manage.py startapp pizzas

############ DEFINING THE MODEL
# Use models.py in pizzas to define the data we want to manage in our app

############ ACTIVATING THE MODEL
# Open settings.py in Pizzeria to add the app we created:
''' 
INSTALLED_APPS = [
    #my_apps
    'pizzas',
    etc. 
'''

############ STORING THE INFORMATION
### py manage.py makemigrations pizzas
# This command creates a migration file that instructs the database to store any
# data associated with any new models.
### py manage.py migrate
# This command applies the changes in the migration file previously created.


############ CRWATING DJANGO ADMIN SITE
### py manage.py createsuperuser
# username: PizzaMonster
# password: p1zzaislife

############  REGISTER MODEL WITH THE ADMIN SITE
# To use the Topic model, we have to register it with the admin site.
# The dot in front of models tells Django to look for models.py in the
# same directory as admin.py
# The code admin.site.register() tells Django to manage our model through the admin site.
### Go to admin.py in pizzas and type code.
'''
from .models import Pizza

admin.site.register(Pizza)
'''
# To check if it worked run server again and click link:
### py manage.py runserver
# Add /admin behind link in browser address
# http://127.0.0.1:8000/admin

############ MIGRATE AND REGISTER THE TOPPING MODEL
# In terminal: 
###py manage.py makemigrations pizzas
### py manage.py migrate
# In admin.py
'''
from .models import Topping

admin.site.register(Topping)
'''

############ DJANGO SHELL
# To examine data programmatically (manually not with server) through an interactive terminal session:
# Create the Django Shell --> MyShell.py
# Add code and run. 
# Can be found in MyShell.py

############ MAPPING THE URL
# Map the home page URL to something other than the default Django site (With the rocket)
# Edit the default urls.py file in the Pizzeria folder to look like this:
'''
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include("pizzas.urls")),
]
'''
# This says that we create another pathway in our app (pizzas - not in our project Pizzeria)
# That command makes it know where to go

# Make a new file, urls.py, in the pizzas folder (the app)
#### Go into urls.py (in pizzas) to find instructions there.


############## FOLLOW POWERPOINTS FOR REST!

#learning_log = Pizzeria
# learning_logs = pizzas
#Topic = Pizza
#Entry = Topping