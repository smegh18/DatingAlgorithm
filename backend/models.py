from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class UserProfile(db.Model):
    __tablename__ = 'user_profile'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    interests = db.Column(db.Text, nullable=False)
    affiliations = db.Column(db.Text, nullable=False)
    demographics = db.Column(db.JSON, nullable=False)
    likes = db.Column(db.PickleType, default=[])
    dislikes = db.Column(db.PickleType, default=[])

    def __repr__(self):
        return f"<UserProfile {self.name}>"
