from main import db
from datetime import datetime

class Feedback(db.Model):
    __tablename__ = 'feedbacks'

    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(), nullable=False)
    last_updated = db.Column(db.DateTime, default=datetime.now, onupdate=datetime.now)
    project_id = db.Column(db.Integer, db.ForeignKey('projects.id'), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)