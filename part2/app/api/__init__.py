#!/usr/bin/python3
from flask import Blueprint
from flask_restx import Api
from app.models.amenity import api as amenity_ns
from app.models.place import api as place_ns
from app.models.user import api as user_ns

blueprint = Blueprint("api", __name__, url_prefix="/api")

api = Api(
    blueprint,
    title="My API",
    version="1.0",
    description="API documentation for the project",
)

api.add_namespace(amenity_ns, path="/amenities")
api.add_namespace(place_ns, path="/places")
api.add_namespace(user_ns, path="/user")
