import random
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import CountVectorizer
from surprise import Dataset, Reader, SVD
from surprise.model_selection import train_test_split
import pandas as pd
from models import UserProfile, db

# Calculate similarity score based on interests
def calculate_similarity(user_interests, other_users):
    vectorizer = CountVectorizer().fit_transform([user_interests] + [user.interests for user in other_users])
    similarity_matrix = cosine_similarity(vectorizer)
    user_similarity_scores = similarity_matrix[0][1:]  # Ignore self-comparison
    return user_similarity_scores

# Train recommendation model
def train_recommendation_model():
    with db.session.begin():
        interactions = [
            (user.id, liked_user_id, 1)
            for user in UserProfile.query.all()
            for liked_user_id in user.likes
        ]
        if not interactions:
            return None  # No data to train on

        reader = Reader(rating_scale=(0, 1))
        data = Dataset.load_from_df(pd.DataFrame(interactions, columns=['user', 'item', 'rating']), reader)

        trainset, testset = train_test_split(data, test_size=0.2)
        model = SVD()
        model.fit(trainset)

        return model

# Find similar profiles
def find_similar_profiles(current_user, all_users, top_n=3):
    other_users = [user for user in all_users if user.id != current_user.id]
    similarity_scores = calculate_similarity(current_user.interests, other_users)

    # Pair users with their scores and sort by similarity
    user_score_pairs = list(zip(other_users, similarity_scores))
    user_score_pairs.sort(key=lambda x: x[1], reverse=True)

    # Select top N similar users
    similar_users = [pair[0] for pair in user_score_pairs[:top_n]]

    # Select random users for diversity
    random_users = random.sample([user for user in other_users if user not in similar_users], top_n)

    # Combine and shuffle similar and random users
    result = similar_users + random_users
    random.shuffle(result)
    return result
