from flask import Blueprint, jsonify, session, request
from app.models import User, Menu, Restaurant
from flask_login import current_user, login_user, logout_user, login_required

restaurant_routes = Blueprint('restaurants', __name__)

@restaurant_routes.route('/<int:id>/menus')
def get_all_restaurant_menus(id):
    restaurant = Restaurant.query.get(id)

    if not restaurant:
        return {'error' : 'could not find restaurant with that id'}
    rest_dict = restaurant.to_dict()

    return rest_dict
