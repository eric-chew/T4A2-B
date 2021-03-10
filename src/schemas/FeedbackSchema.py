from main import ma
from models.Feedback import Feedback
from schemas.ProjectSchema import ProjectSchema

class FeedbackSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Feedback
        
    project =  ma.Nested(ProjectSchema)
    user =  ma.Nested(UserSchema)

feedback_schema = FeedbackSchema()
feedbacks_schema = FeedbackSchema(many=True)