from flask import Blueprint, jsonify
from flask_login import login_required
from app.models import User, Menu
from flask_login import current_user, login_user, logout_user, login_required

menu_routes = Blueprint('menus', __name__)


