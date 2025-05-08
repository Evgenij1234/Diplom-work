from extensions import db
from datetime import datetime

class Product(db.Model):
    __tablename__ = 'products'

    id = db.Column(db.Integer, primary_key=True)
    user = db.Column(db.String(50), db.ForeignKey('users.username'), nullable=False)
    category = db.Column(db.Text)  
    name = db.Column(db.Text, nullable=False)  
    price = db.Column(db.Numeric(10, 2))
    unit = db.Column(db.Text) 
    characteristics = db.Column(db.JSON)
    link = db.Column(db.Text)
    resource = db.Column(db.Text)
    date_time = db.Column(db.DateTime)
    created_at = db.Column(db.TIMESTAMP, server_default=db.func.current_timestamp())

    def __repr__(self):
        return f'<Product {self.name}>'