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