from flask import Blueprint, jsonify
from flask_login import login_required
from app.models import User, Menu
from flask_login import current_user, login_user, logout_user, login_required

menu_routes = Blueprint('menus', __name__)


@menu_routes.route('/<int:id>')
def get_menu(id):
    menu = Menu.query.get(id)

    if not menu:
        return {'error' : 'could not find a menu with that id'}, 404
    menu_dict = menu.to_dict()
    
    return menu_dict
