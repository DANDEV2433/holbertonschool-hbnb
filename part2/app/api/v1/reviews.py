#!/usr/bin/python3
from flask_restx import Namespace, Resource, fields
from app.services import facade

api = Namespace('reviews', description='Review operations')

# Define the review model for input validation and documentation
review_model = api.model('Review', {
    'text': fields.String(required=True, description='Text of the review'),
    'rating': fields.Integer(required=True, description='Rating of the place (1-5)'),
    'user_id': fields.String(required=True, description='ID of the user'),
    'place_id': fields.String(required=True, description='ID of the place')
})

@api.route('/')
class ReviewList(Resource):
    @api.expect(review_model)
    @api.response(201, 'Review successfully created')
    @api.response(400, 'Invalid input data')
    def post(self):
        """Register a new review"""
        data = request.json
        try:
            new_review = facade.create_review(
                text=data['text'],
                rating=data['rating'],
                user_id=data['user_id'],
                place_id=data['place_id']
            )
            return {"message": "L'avis a ete cree", "avis": new_review.to_dict()}, 201
        except ValueError as e:
            return {"erreur": str(e)}, 400

    @api.response(200, 'List of reviews retrieved successfully')
    def get(self):
        """Retrieve a list of all reviews"""
        reviews = facade.get_all_reviews()
        return [review.to_dict() for review in reviews], 200

@api.route('/<review_id>')
class ReviewResource(Resource):
    @api.response(200, 'Review details retrieved successfully')
    @api.response(404, 'Review not found')
    def get(self, review_id):
        """Get review details by ID"""
        review = facade.get_review_by_id(review_id)
        if review:
            return review.to_dict(), 200
        return {"erreur": "Avis introuvable"}, 404

    @api.expect(review_model)
    @api.response(200, 'Review updated successfully')
    @api.response(404, 'Review not found')
    @api.response(400, 'Invalid input data')
    def put(self, review_id):
        """Update a review's information"""
        data = request.json
        try:
            updated_review = facade.update_review(review_id, **data)
            if updated_review:
                return {"message": "L'avis a ete mis a jour", "avis": updated_review.to_dict()}, 200
            return {"erreur": "Avis introuvable"}, 404
        except ValueError as e:
            return {"erreur": str(e)}, 400

    @api.response(200, 'Review deleted successfully')
    @api.response(404, 'Review not found')
    def delete(self, review_id):
        """Delete a review"""
        deleted = facade.delete_review(review_id)
        if deleted:
            return {"message": "L'avis a ete supprime"}, 200
        return {"erreur": "Avis introuvable"}, 404

@api.route('/places/<place_id>/reviews')
class PlaceReviewList(Resource):
    @api.response(200, 'List of reviews for the place retrieved successfully')
    @api.response(404, 'Place not found')
    def get(self, place_id):
        """Get all reviews for a specific place"""
        reviews = facade.get_reviews_by_place_id(place_id)
        if reviews is not None:
            return [review.to_dict() for review in reviews], 200
        return {"erreur": "Lieu introuvable"}, 404
