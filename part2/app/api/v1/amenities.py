#!/usr/bin/python3
from flask_restx import Namespace, Resource, fields
from app.services import facade
from flask import request

api = Namespace('amenities', description='Amenity operations')

# Definie le modele de commodite pour la validation et la documentation des entrees
amenity_model = api.model('Amenity', {
    'name': fields.String(required=True, description='Name of the amenity')
})

@api.route('/')
class AmenityList(Resource):
    @api.expect(amenity_model)
    @api.response(201, 'Amenity successfully created')
    @api.response(400, 'Invalid input data')
    def post(self):
        """Register a new amenity"""
        data = request.json
        try:
            new_amenity = facade.create_amenity({"name": data['name']})
            return {"message": "La commodite a ete creee", "commodite":new_amenity.to_dict()}, 201
        except ValueError as e:
            return {"erreur": str(e)}, 400

    @api.response(200, 'List of amenities retrieved successfully')
    def get(self):
        """Retrieve a list of all amenities"""
        amenities = facade.get_all_amenities()
        return [amenity.to_dict() for amenity in amenities], 200

@api.route('/<amenity_id>')
class AmenityResource(Resource):
    @api.response(200, 'Amenity details retrieved successfully')
    @api.response(404, 'Amenity not found')
    def get(self, amenity_id):
        """Get amenity details by ID"""
        amenity = facade.get_amenity_by_id(amenity_id)
        if amenity:
            return amenity.to_dict(), 200
        return {"erreur": "Commodite introuvable"}, 404

    @api.expect(amenity_model)
    @api.response(200, 'Amenity updated successfully')
    @api.response(404, 'Amenity not found')
    @api.response(400, 'Invalid input data')
    def put(self, amenity_id):
        """Update an amenity's information"""
        data = request.json
        try:
            updated_amenity = facade.update_amenity(amenity_id, **data)
            if updated_amenity:
                return {"message": "Commodite mise a jour", "commodite": updated_amenity.to_dict()}, 200
            return {"erreur": "Commodite introuvable"}, 404
        except ValueError as e:
            return {"erreur": str(e)}, 400
