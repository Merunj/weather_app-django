from django.test import TestCase, Client
from django.urls import reverse


class WeatherViewTest(TestCase):
    def setUp(self):
        self.client = Client()

    def test_weather_view_get(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)  
        self.assertContains(response, 'Введите название города')

    def test_weather_view_post_valid_city(self):
        response = self.client.post(reverse('home'), {'city':'Москва'})
        self.assertEqual(response.status_code, 200)  
        self.assertContains(response, 'Москва')

    def test_weather_view_post_invalid_city(self):
        response = self.client.post(reverse('home'), {'city':'Москваз'})
        self.assertEqual(response.status_code, 200)  
        self.assertContains(response, 'Не удалось получить данные о погоде')
            