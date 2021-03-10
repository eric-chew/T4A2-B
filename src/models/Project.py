from main import db

class Project(db.Model):
    __tablename__="projects"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String())
    link = db.Column(db.String())
    description = db.Column(db.String())
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    feedbacks = db.relationship(
        "Feedback",
        backref="project",
        cascade="all, delete"
    )