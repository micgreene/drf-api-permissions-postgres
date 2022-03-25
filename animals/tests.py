from django.test import TestCase
from django.contrib.auth import get_user_model

from .models import Animal

class AnimalTests(TestCase):

    @classmethod
    def setUpTestData(cls):
        test = get_user_model().objects.create_user(username='test', password='password')
        test.save()

        test_animal = Animal.objects.create(name='Rattlesnake', owner=test, description='Long, venomous reptile native to the arid regions of SW North America. Makes a distinct warning sound to would-be predators with a delicate formation on its tail which gives the snake its namesake.')
        test_animal.save()

    def test_animals_model(self):
        animal = animal.objects.get(id=1)
        actual_user = str(animal.owner)
        actual_name = str(animal.name)
        actual_descr = str(animal.description)
        self.assertEqual(actual_user,'test')
        self.assertEqual(actual_name, 'Rattlesnake')
        self.assertEqual(actual_descr,'Long, venomous reptile native to the arid regions of SW North America. Makes a distinct warning sound to would-be predators with a delicate formation on its tail which gives the snake its namesake.')