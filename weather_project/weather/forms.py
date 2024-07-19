from django import forms
from .models import WeatherCity
from django.forms import ModelForm

class WeatherForm(ModelForm):
    class Meta:
        model = WeatherCity
        fields = ['city']
        widgets = {
            'city': forms.TextInput(attrs={'class':'input', 'placeholder': 'Введите ваш город'})
        }
        # city = forms.CharField(label='Введите название города:', widget=forms.TextInput(attrs={'class':'input', 'placeholder': 'Введите ваш город'}), max_length=50)

    def __str__(self):
        return self.city
