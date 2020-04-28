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


#learning_log = Pizzeria
# learning_logs = pizzas

#Topic = Pizza
#Entry = Topping