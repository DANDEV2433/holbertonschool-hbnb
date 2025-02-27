#!/usr/bin/python3
import unittest
from app.models.user import User
from app.models.place import Place
from app.models.review import Review

class TestReview(unittest.TestCase):

    def test_review_creation(self):
        # Création d'un utilisateur
        user = User(first_name="John", last_name="Doe", email="john.doe@example.com", password="password")

        # Création d'un lieu
        place = Place(title="Cozy Apartment", description="A nice place to stay", price=100,
                      latitude=37.7749, longitude=-122.4194, owner=user)

        # Création d'u avis
        review = Review(text="Great stay!", rating=5, place=place, user=user)

        # Ajout de l'avis au lieu
        review.write_review()

        # Vérification des assertions
        assert review.text == "Great stay!"
        assert review.rating == 5
        assert review.place == place
        assert review.user == user

        # Vérification que 'avis a bien été ajouée au lie
        # Vérifie que le nombre d'avs associés au lieu est bien égal à 1
        assert len(place.reviews) == 1
        # Vérifie que le texte u  premer avis associée au lie
        # a bien le même nom.
        assert place.reviews[0].text == "Great stay!"
        print("Review creation test passed!")
