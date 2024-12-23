from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Configure the database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Import models
from models import UserProfile

# Initialize the database
with app.app_context():
    print("Creating database tables...")
    db.create_all()  # This will create the tables as defined in models.py
    print("Tables created successfully.")
