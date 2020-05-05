from django.shortcuts import render, redirect

from .models import Pizza, Review

from .forms import ReviewForm

from .forms import ReviewForm

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

def new_review(request, pizza_id):
    pizza_choice = Pizza.objects.get(id=pizza_id)
    if request.method != 'POST':
        form = ReviewForm()
    else:
        form= ReviewForm(data=request.POST)

        if form.is_valid():
            new_review = form.save(commit=False)
            new_review.pizza_choice = pizza_choice
            new_review.save()
            form.save()
            return redirect('pizzas:pizza_choice', pizza_id=pizza_id)

    context = {'form': form, 'pizza_choice':pizza_choice}
    return render(request, 'pizzas/new_review.html', context)
