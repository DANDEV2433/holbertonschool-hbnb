from .base_model import BaseModel
import re


class User(BaseModel):
    #  liste partagée par tous les instances de la classe User
    email_list = []

    def __init__(self, first_name, last_name, email, password, is_admin=False):
        super().__init__()
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.is_admin = is_admin
        self.password = password
        self.reviews = []
        self.places = [] # Liste des lieux possédés par l'utilisateur

    def add_place(self, place):
        # Ajoute un lieu à l'utilisateur.
        if place not in self.places:
            self.places.append(place)
            print(f"Lieu ajouté à {self.first_name} {self.last_name}")
        else:
            print("Ce lieu a déjà été ajouté.")

    def add_review(self, review):
        # Ajoute une revue à la liste des revues de l'utilisateur
        if review not in self.reviews:
            self.reviews.append(review)
            print(f"Revue ajoutée par {self.first_name} {self.last_name}")
        else:
            print("Cette revue a déjà été ajoutée.")

    def get_reviews(self):
        # Retourne toutes les revues écrites par cet utilisateur
        return self.reviews

    def register(self):
        # enregistrement de l'utilisateur
        # Validation pour le prénom
        if len(self.first_name) > 50:
            raise ValueError("Le prénom dépasse 50 caractères.")
    # Validation pour le nom de famille
        if len(self.last_name) > 50:
            raise ValueError("Le nom de famille dépasse 50 caractères.")

    # Validation pour l'email
        if not self.is_valid_email(self.email):
            raise ValueError("L'email n'est pas valide.")

    # Vérifier si l'email est unique
        if not self.is_unique_email(self.email):
            raise ValueError("L'email est déjà utilisé.")

    # Ajouter l'email à la liste après la validation
        self.__class__.email_list.append(self.email)

        print(f"{self.first_name} {self.last_name} enregistré avec succès.")

    def is_valid_email(self, email):
        # Valide le format de l'email avec une expression régulière
        email_regex = r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)"
        # tente de faire correspondre la chaîne email
        # avec l'expression régulière
        return re.match(email_regex, email) is not None

    def is_unique_email(self, email):
        """Vérifie si l'email est unique"""
        # retourne True si unique sinon false
        return email not in self.__class__.email_list

    def login(self):
        """Simuler la connexion."""
        print(f"{self.first_name} {self.last_name} est maintenant connecté.")

    def logout(self):
        """Simuler la déconnexion."""
        print(f"{self.first_name} {self.last_name} est maintenant déconnecté.")

    def delete(self):
        """suppression de l'utilisateur."""
        if self.email in self.__class__.email_list:
            self.__class__.email_list.remove(self.email)

        self.first_name = None
        self.last_name = None
        self.email = None
        print
        (f"Utilisateur supprimé. Les informations sont maintenant effacées.")

    def get_date_of_creation(self):
        """Retourner la date de création de l'utilisateur."""
        return self.created_at

    def get_date_of_update(self):
        """Retourner la date de mise à jour de l'utilisateur."""
        return self.updated_at
