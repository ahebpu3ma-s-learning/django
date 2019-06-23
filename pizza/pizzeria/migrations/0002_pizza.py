# Generated by Django 2.2.2 on 2019-06-21 20:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pizzeria', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pizza',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='Название пиццы')),
                ('short_description', models.CharField(max_length=30, verbose_name='Рецептура')),
                ('price', models.IntegerField(default=0, verbose_name='Цена')),
                ('pizzashop', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pizzeria.PizzaShop')),
            ],
        ),
    ]