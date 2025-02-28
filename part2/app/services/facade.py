#!/usr/bin/python3
from app.persistence.repository import InMemoryRepository
from app.models import user, place, amenity, review

class HBnBFacade:
    def __init__(self):
        self.user_repo = InMemoryRepository()
        self.place_repo = InMemoryRepository()
        self.review_repo = InMemoryRepository()
        self.amenity_repo = InMemoryRepository()

    # Placeholder method for creating a user
    def create_user(self, user_data):
        user = user(**user_data)
        self.user_repo.add(user)
        return user

    def get_user(self, user_id):
        return self.user_repo.get(user_id)

    def get_user_by_email(self, email):
        return self.user_repo.get_by_attribute('email', email)

    def create_place(self, place_data):
        place = place(**place_data)
        self.place_repo.add(place)
        return place

    def get_place(self, place_id):
        return self.place_repo.get(place_id)

    def get_all_places(self):
        return self.place_repo.get_all(self)

    def update_place(self, place_id, place_data):
         # Récupére la place existante
        place = self.get_place(place_id)
        place.update(**place_data)  # Maj la place
        self.place_repo.update(place)  # Sauvegarde
        return place
    
    def create_amenity(self, amenity_data):
        amenity = amenity(**amenity_data)
        self.amenity_repo.add(amenity)
        return amenity

    def get_amenity(self, amenity_id):
        return self.amenity_repo.get(amenity_id)

    def get_all_amenities(self):
        return self.amenity_repo.get_all()
    
    def update_amenity(self, amenity_id, amenity_data):
        # Récupére la commodité existante
        amenity = self.get_amenity(amenity_id)
        amenity.update(**amenity_data)  # Maj la commodité
        self.amenity_repo.update(amenity)  # Sauvegarde
        return amenity

    def create_review(self, review_data):
        review = review(**review_data)
        self.review_repo.add(review)
        return review

    def get_review(self, review_id):
        return self.review_repo.get(review_id)

    def get_all_reviews(self):
        return self.review_repo.get_all(self)

    def get_reviews_by_place(self, place_id):
        # Récupérer les avis du lieu
        reviews = self.review_repo.get_reviews_for_place(place_id)
        return reviews

    def update_review(self, review_id, review_data):
         # Récupére l'avis existant
        review = self.get_review(review_id)
        review.update(**review_data)  # Maj l'avis
        self.review_repo.update(review)  # Sauvegarde
        return review

    def delete_review(self, review_id):
        review = self.review_repo.get(review_id)
        self.review_repo.delete(review)
