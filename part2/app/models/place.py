#!/usr/bin/python3
from .base_model import BaseModel
from datetime import datetime
from app.models.user import User
from flask_restx import Api

api = Api()

class Place(BaseModel):
    def __init__(self, title, description, price, latitude, longitude, owner):
        super().__init__()
        self.title = self.validate_title(title)
        self.description = self.validate_description(description)
        self.price = self.validate_price(price)
        self.latitude = self.validate_latitude(latitude)
        self.longitude = self.validate_longitude(longitude)
        self.owner = self.validate_owner(owner)
        self.reviews = []  # List to store related reviews
        self.amenities = []  # List to store related amenities

    def add_review(self, review):
        """ajoute un avis au lieu"""
        if review not in self.reviews:
            self.reviews.append(review)
            print(
                f"ajoute par {review.user.first_name}{review.user.last_name}"
                )
        else:
            print("Cet avis a deja ete ajoute")

    def get_reviews(self):
        """retourne tout les avis associes au lieu"""
        return self.reviews

    def add_amenity(self, amenity):
        """ajoute une commodite dans la liste des commodites du lieu"""
        if amenity not in self.amenities:
            self.amenities.append(amenity)

    def remove_amenity(self, amenity):
        """retire une commodite de la liste des commodites du lieu"""
        if amenity in self.amenities:
            self.amenities.remove(amenity)

    def get_amenities(self):
        """retourne la liste de commodites du lieu"""
        return self.amenities

    @staticmethod
    def validate_title(title):
        if not title or len(title) > 100:
            raise
        ValueError
        ("Un titre est requis et ne doit pas depasser 100 caracteres.")
        return title

    @staticmethod
    def validate_description(description):
        if description and len(description) > 500:
            raise ValueError("La description ne doit depasser 500 caracteres.")
        return description

    @staticmethod
    def validate_price(price):
        if price < 0:
            raise ValueError("Le prix doit avoir une valeur positive.")
        return price

    @staticmethod
    def validate_latitude(latitude):
        if not (-90.0 <= latitude <= 90.0):
            raise ValueError("La latitude doit etre entre -90.0 et 90.0.")
        return latitude

    @staticmethod
    def validate_longitude(longitude):
        if not (-180.0 <= longitude <= 180.0):
            raise ValueError("La longitude doit etre entre -180.0 et 180.0.")
        return longitude

    @staticmethod
    def validate_owner(owner):
        if not isinstance(owner, User):
            raise
        ValueError("Le proprietaire doit etre une instance valide de User.")
        return owner

    def update(self, **kwargs):
        # maj les attributs et modifie la date de mise a jour (updated_at)
        for key, value in kwargs.items():
            if hasattr(self, key) and key != "id":
                setattr(self, key, value)
        self.updated_at = datetime()

    def __repr__(self):
        return (f"Place(id={self.id}, title={self.title}, price={self.price},"
                f"latitude={self.latitude}, longitude={self.longitude},"
                f"owner={self.owner.first_name} {self.owner.last_name})")
