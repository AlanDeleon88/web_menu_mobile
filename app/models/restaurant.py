from .db import db
from datetime import datetime



class Restaurant(db.Model):
    __tablename__ = 'restaurants'

    id= db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(40), nullable=False)
    description = db.Column(db.String(255), nullable=True)
    owner_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.now)
    updated_at = db.Column(db.DateTime, default=datetime.now, onupdate=datetime.now)

    users = db.relationship('User', back_populates='restaurants', single_parent=True)

    menus = db.relationship('Menu', back_populates='restaurants', cascade='all, delete-orphan')

    def to_dict(self):
         return{
            "id" : self.id,
            "name" : self.name,
            "owner_id" : self.owner_id,
            "menus" : [{'menu_id' : menu.id, "name" : menu.name, "description" : menu.description} for menu in self.menus]
        }
