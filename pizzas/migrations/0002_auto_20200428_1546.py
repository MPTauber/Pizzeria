# Generated by Django 3.0.5 on 2020-04-28 20:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pizzas', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='topping',
            name='name',
            field=models.TextField(max_length=50),
        ),
    ]