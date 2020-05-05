# The next 4 lines are required word-for-word in the new Django
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Pizzeria.settings")

import django
django.setup()

from pizzas.models import Pizza, Review

pizzas = Pizza.objects.all()

for pizza in pizzas:
    print(pizza.id, pizza)

# If we know the ID of an object we can use the get() method to
# examine any attributes the object has.

t = Pizza.objects.get(id=1) # Pizza has ID of 1 (seen by executing the above for-loop)
print(t.name)
print(t.date_added)

# We can also look at the entries related to a certain topic.
# Since we defined topic as a foreignkey attribute in the Entry model,
# Django can use this relationship to access the entries for any topic.
# To get data through a foreign key relationship, you use the lowercase name
# of the related model followed by an underscore and the word set.

toppings = t.topping_set.all() # t represents Chess cause we set it as id 1

for topping in toppings:
    print(topping)

r = Review.objects.get(id=2) # Pizza has ID of 1 (seen by executing the above for-loop)
print(r.review)
print(r.date_added)