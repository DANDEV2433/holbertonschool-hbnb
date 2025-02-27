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
        
        # Création d'une revue
        review = Review(text="Great stay!", rating=5, place=place, user=user)
        
        # Ajout de la revue au lieu
        review.write_review()
        
        # Vérification des assertions
        assert review.text == "Great stay!"
        assert review.rating == 5
        assert review.place == place
        assert review.user == user
        
        # Vérification que la revue a bien été ajoutée au lieu
        # Vérifie que le nombre d'avis associés au lieu est bien égal à 1
        assert len(place.reviews) == 1
        # Vérifie que le texte de la première revue associée au lieu
        # a bien le même nom.
        assert place.reviews[0].text == "Great stay!"
        print("Review creation test passed!")

if __name__ == "__main__":
    unittest.main()
