from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from utils import calculate_similarity, find_similar_profiles, train_recommendation_model
import random

app = Flask(__name__)
CORS(app)

# Configure the database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Importing the UserProfile model
from models import UserProfile

# Route to add a user
@app.route('/add_user', methods=['POST'])
def add_user():
    data = request.json
    new_user = UserProfile(
        name=data.get("name"),
        interests=data.get("interests"),
        affiliations=data.get("affiliations"),
        demographics=data.get("demographics")
    )
    db.session.add(new_user)
    db.session.commit()
    return jsonify({"message": "User added successfully", "user_id": new_user.id})

# Route to like a user
@app.route('/like_user', methods=['POST'])
def like_user():
    data = request.json
    user_id = data.get("user_id")
    liked_user_id = data.get("liked_user_id")

    user = UserProfile.query.get(user_id)
    if not user:
        return jsonify({"error": "User not found"}), 404

    if liked_user_id not in user.likes:
        user.likes.append(liked_user_id)
        db.session.commit()

    return jsonify({"message": "User liked successfully"})

# Route to dislike a user
@app.route('/dislike_user', methods=['POST'])
def dislike_user():
    data = request.json
    user_id = data.get("user_id")
    disliked_user_id = data.get("disliked_user_id")

    user = UserProfile.query.get(user_id)
    if not user:
        return jsonify({"error": "User not found"}), 404

    if disliked_user_id not in user.dislikes:
        user.dislikes.append(disliked_user_id)
        db.session.commit()

    return jsonify({"message": "User disliked successfully"})

# Route to find matches
@app.route('/find_matches', methods=['POST'])
def find_matches():
    data = request.json
    user_id = data.get("user_id")
    top_n = data.get("top_n", 3)

    current_user = UserProfile.query.get(user_id)
    if not current_user:
        return jsonify({"error": "User not found"}), 404

    all_users = UserProfile.query.all()
    matches = find_similar_profiles(current_user, all_users, top_n)
    result = [{
        "user_id": match.id,
        "name": match.name,
        "interests": match.interests,
        "affiliations": match.affiliations,
        "demographics": match.demographics
    } for match in matches]

    return jsonify(result)

if __name__ == '__main__':
    # Initialize the database and create tables
    with app.app_context():
        print("Creating database tables...")
        db.create_all()  # Creates the tables based on the models defined
        print("Tables created successfully.")

        # Train the recommendation model after ensuring the schema is ready
        recommendation_model = train_recommendation_model()

    # Start the application
    app.run(debug=True)
