from django.db import models


class WeatherCity(models.Model):
    city = models.CharField(max_length=30, verbose_name='Введите название города')

    def __str__(self):
        return self.city
    
    class Meta:
        verbose_name_plural = "cities"