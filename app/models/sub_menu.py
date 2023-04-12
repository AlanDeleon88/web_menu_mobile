from .db import db
from datetime import datetime

class SubMenu(db.Model):
    __tablename__='sub_menus'

    id = db.Column(db.Integer, primary_key= True)
    name = db.Column(db.String(40), nullable= False)
    description = db.Column(db.String(255), nullable = True)
    menu_id = db.Column(db.Integer, db.ForeignKey('menus.id'), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.now)
    updated_at = db.Column(db.DateTime, default=datetime.now, onupdate=datetime.now)

    menus = db.relationship('Menu', back_populates='sub_menus', single_parent = True)

    def to_dict(self):
        return{
            "id" : self.id,
            "name" : self.name,
            "description" : self.description,
            "menu_id" : self.menu_id
        }
