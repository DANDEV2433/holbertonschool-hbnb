#!/usr/bin/python3
from uuid import uuid4
from datetime import datetime

class BaseModel:
    def __init__(self):
        self.id = str(uuid4())  # Identifiant unique
        self.created_at = datetime.now()  # Horodatage de la création
        self.updated_at = datetime.now()  # Horodatage de la dernière mise à jour

    def save(self):
        """Met à jour le timestamp `updated_at`."""
        self.updated_at = datetime.now()

    def update(self, data):
        """Met à jour les attributs à partir d'un dictionnaire de nouvelles valeurs."""
        for key, value in data.items():
            if hasattr(self, key):
                setattr(self, key, value)
        self.save()
