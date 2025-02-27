#!/usr/bin/python3
from .base_model import BaseModel


class Review(BaseModel):
    def __init__(self, text, rating, place, user):
        super().__init__()
        self.text = text
        self.rating = rating
        self.place = place  # Référence au lieu associé à l'avis
        self.user = user  # Référence à l'utilisateur ayant rédigé l'avis

    def write_review(self):
        # Validation du texte de l'avis
        if not self.text:
            raise ValueError("Le texte de l'avis est obligatoire.")

        # Validation de la note
        if not (1 <= self.rating <= 5):
            raise ValueError("La note doit être entre 1 et 5.")

        # Validation de l'existence du lieu et de l'utilisateur
        if not self.place:
            raise ValueError("Le lieu de l'avis est invalide.")

        if not self.user:
            raise ValueError("L'utilisateur de l'avis est invalide.")

        # Ajouter l'avis au lieu
        self.place.add_review(self)

        print(
            f"Revue de {self.user.first_name} {self.user.last_name} "
            f" pour {self.place.title}."
        )

    def delete(self):
        # Supprimer l'avis
        if self.place:
            self.place.remove_review(self)

        # Effacer les informations de l'avis
        self.text = None
        self.rating = None
        self.place = None
        self.user = None

        print(f"Avis supprimé.")

    def edit(self, new_text, new_rating):
        # modifier un avis existant
        if new_rating < 1 or new_rating > 5:
            raise ValueError("La note doit être entre 1 et 5.")

        self.text = new_text
        self.rating = new_rating
        self.save()  # Mise à jour de la date de mise à jour

        print(
            f"Avis édité par {self.user.first_name} "
            f"{self.user.last_name}."
        )

    def get_reviews_by_place(self):
        # Retourner tout les avis pour un lieu donné
        return [
            review for review in self.place.reviews
            if review.place == self.place
        ]

    def get_reviews_by_user(self):
        # Retourner tout les avis écrits par un utilisateur donné
        return [
            review for review in self.place.reviews
            if review.user == self.user
        ]

    def get_date_of_review(self):
        # Retourner la date de création de l'avis
        return self.created_at

    def get_date_of_creation(self):
        # Retourner la date de création de l'avise
        return self.created_at
