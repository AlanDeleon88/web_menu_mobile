from .db import db
from datetime import datetime

class Menu(db.Model):
    __tablename__ = 'menus'

    id= db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(40), nullable=False)
    description = db.Column(db.String(255), nullable=True)
    restaurant_id = db.Column(db.Integer, db.ForeignKey('restaurants.id'), nullable=False)

    created_at = db.Column(db.DateTime, default=datetime.now)
    updated_at = db.Column(db.DateTime, default=datetime.now, onupdate=datetime.now)


    restaurants = db.relationship('Restaurant', back_populates='menus', single_parent=True)

    sub_menus = db.relationship('SubMenu', back_populates='menus', cascade='all, delete-orphan')

    def to_dict(self):
        return{
            'id' : self.id,
            'name' : self.name,
            'user_id' : self.user_id
        }
