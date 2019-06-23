from django.db import models

# Create your models here.
class PizzaShop(models.Model):
    name = models.CharField(max_length=30, verbose_name='Пиццерия')
    description = models.TextField(verbose_name='Страничка про нас')
    rating = models.FloatField(default = 0, verbose_name='Рэйтинг')
    url = models.URLField(verbose_name='Интернет-адрес')

    class Meta:
        verbose_name='Пиццерия'
        verbose_name_plural='Пиццерия'

    def __str__(self):
        return self.name

class Pizza(models.Model):
    pizzashop = models.ForeignKey(PizzaShop, on_delete=models.CASCADE)
    name = models.CharField(max_length=30, verbose_name='Название пиццы')
    short_description = models.CharField(max_length=30, verbose_name="Рецептура")
    price = models.IntegerField(default=0, verbose_name = 'Цена')
    photo = models.ImageField('Фото', upload_to='firstapp/photos', default='', blank=True)

    class Meta:
        verbose_name='Пиццa'
        verbose_name_plural='Пиццы'
        ordering = ['price']

    def __str__(self):
        return self.name

class Order(models.Model):
    pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE, verbose_name = 'Пицца')
    name = models.CharField(max_length=30, verbose_name='Имя')
    phone = models.CharField(max_length=30, verbose_name='Телефон')
    date = models.DateTimeField(auto_now_add = True, verbose_name='Дата')
