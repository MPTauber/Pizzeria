from django.db import models

# Create your models here.

#Define a model Pizza with a field called name, 
# which will hold name values, such as Hawaiian and Meat Lovers.

class Pizza(models.Model):
    name= models.CharField(max_length=200)
    # auto_no_add=True - set this attribute to the current date and time
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


#Define a model called Topping with fields called 
# pizza and name. The pizza field should be a 
# foreign key to Pizza, and name should be able to 
# hold values such as pineapple, Canadian bacon, and sausage.

class Topping(models.Model):
    pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE)
    name = models.CharField(max_length=50) # Toppings shouldn't be longer than 50 characters
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        # it allows us to set a special attribute telling Django to use "Entries"
        # when it needs to refer to more than one entry. Without this, Django
        # would refer to multiple entries as "Entrys".
        verbose_name_plural = 'toppings'

    def __str__(self):
        return f"{self.name[:50]}..."

class Review(models.Model):
    pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE)
    review = models.TextField() 
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'reviews'

    def __str__(self):
        return f"{self.review[:50]}..."