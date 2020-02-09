import base64
import requests
from app import db, login
from datetime import datetime
from flask_login import UserMixin

@login.user_loader
def load_user(id):
    return User.query.get(int(id))

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    password_hash = db.Column(db.String(128))

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return self.password_hash == base64.b64encode(password.encode('utf-8'))

    # def __repr__(self):
    #     return '<User {}>'.format(self.name)

class Debtor(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True, unique=True)
    ship = db.Column(db.String(120))
    legality = db.Column(db.String(120))
    address = db.Column(db.String)
    phone_number = db.Column(db.String(120))
    key_person = db.Column(db.String(120))
    contact_person = db.Column(db.String(120))
    credit_aggreement = db.Column(db.String(120))
    total_credits = db.Column(db.Integer)
    tenor = db.Column(db.Integer)
    start_date = db.Column(db.DateTime, index=True)
    end_date = db.Column(db.DateTime, index=True)

    def to_dict(self):
        data = {
            'id': self.id,
            'name': self.name,
            'ship': self.ship,
            'legality': self.legality,
            'address': self.address,
            'phone_number': self.phone_number,
            'key_person': self.key_person,
            'contact_person': self.contact_person,
            'credit_aggreement': self.credit_aggreement,
            'total_credits': self.total_credits,
            'tenor': self.tenor,
            'fancy_start_date': datetime.strftime(self.start_date, '%d %B %Y'),
            'fancy_end_date': datetime.strftime(self.end_date, '%d %B %Y'),
            'start_date': datetime.strftime(self.start_date, '%Y-%m-%d'),
            'end_date': datetime.strftime(self.end_date, '%Y-%m-%d'),
        }

        return data

    # def __repr__(self):
    #     return '<Debtor {}>'.format(self.name)

class Payment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    main = db.Column(db.Integer)
    interest = db.Column(db.Integer)
    payment_date = db.Column(db.DateTime, index=True)
    notes = db.Column(db.String(150))
    debtor_id = db.Column(db.Integer, db.ForeignKey('debtor.id'))

    def to_dict(self):
        data = {
            'id': self.id,
            'main': self.main,
            'interest': self.interest,
            'notes': self.notes,
            'fancy_payment_date': datetime.strftime(self.payment_date, '%d %B %Y'),
            'payment_date': datetime.strftime(self.payment_date, '%Y-%m-%d'),
        }

        return data

    # def __repr__(self):
    #     return '<Payment {}>'.format(self.name)
