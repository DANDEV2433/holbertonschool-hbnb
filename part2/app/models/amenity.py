#!/usr/bin/python3
from .base_model import BaseModel
from datetime import datetime
from flask_restx import Api

api = Api()

class Amenity(BaseModel):
    def __init__(self, name):
        super().__init__()
        self.name = self.validate_name(name)

    @staticmethod
    def validate_name(name):
        """Valide le nom de la commodite."""
        if not name or len(name) > 50:
            raise ValueError("Nom de commodite requise, 50 caracteres max")
        return name

    def update(self, name=None):
        """met a  jour le nom de la commodite et la date de modification."""
        if name:
            self.name = self.validate_name(name)
        self.updated_at = datetime.now()

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "created_at": self.created_at.isoformat(),
            "updated_at": self.updated_at.isoformat()}

    def __repr__(self):
        return f"Amenity(id={self.id}, name={self.name})"
