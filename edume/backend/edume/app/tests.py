from django.test import TestCase

# Create your tests here.
from edume.app.models import User


def test_user_creation():
    user = User.objects.create(name="Berat",
                               surname="Postalcioglu",
                               email="bpostalci@gmail.com",
                               password="123",
                               bio="")
    assert user is not None
