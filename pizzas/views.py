from django.shortcuts import render

from .models import Pizza

# Create your views here.
def index(request):
    """The home page for Pizzeria."""
    return render(request, 'pizzas/index.html')


def pizza_choices(request):
    pizza_choices = Pizza.objects.order_by('name') # alphabetical order
    context = {'pizza_choices':pizza_choices}
    return render(request, 'pizzas/pizza_choices.html', context)

def pizza_choice(request, pizza_id):
    pizza_choice = Pizza.objects.get(id=pizza_id)
    toppings = pizza_choice.topping_set.order_by('name')
    reviews = pizza_choice.review_set.order_by("-date_added")
    context = {'pizza_choice':pizza_choice, 'toppings':toppings, 'reviews':reviews}

    return render(request, 'pizzas/pizza_choice.html', context)


