from datetime import datetime

from flask_login import UserMixin
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Dish(db.Model):
    __tablename__ = 'dish'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(128), unique=True, nullable=False)
    description = db.Column(db.String)
    price = db.Column(db.Double)
    quantity = db.Column(db.Integer)

    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'price': self.price,
            'quantity': self.quantity,
        }


class Order(db.Model):
    __tablename__ = 'order'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    status = db.Column(db.String)
    special_requests = db.Column(db.String, nullable=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def serialize(self):
        return {
            'id': self.id,
            'user_id': self.user_id,
            'status': self.status,
            'special_requests': self.special_requests,
            'created_at': self.created_at,
            'updated_at': self.updated_at,
        }


class OrderDish(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    order_id = db.Column(db.Integer, db.ForeignKey('order.id'), nullable=False)
    dish_id = db.Column(db.Integer, db.ForeignKey('dish.id'), nullable=False)
    dish_name = db.Column(db.String)
    price = db.Column(db.Double)
    quantity = db.Column(db.Integer)

    def serialize(self):
        return {
            'id': self.id,
            'order_id': self.order_id,
            'dish_id': self.dish_id,
            'price': self.price,
            'quantity': self.quantity,
            'dish_name': self.dish_name,
        }


class User(db.Model, UserMixin):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(128), unique=True, nullable=False)
    email = db.Column(db.String(256), unique=True, nullable=False)
    phone_number = db.Column(db.String, unique=False, nullable=True)
    password_hash = db.Column(db.String(1024), nullable=False)
    role = db.Column(db.String(256))
    created_at = db.Column(db.DateTime)
    updated_at = db.Column(db.DateTime)

    def serialize(self):
        return {
            'id': self.id,
            'username': self.username,
            'email': self.email,
        }


class Session(db.Model):
    __tablename__ = 'session'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    session_token = db.Column(db.String)
    expires_at = db.Column(db.DateTime)
