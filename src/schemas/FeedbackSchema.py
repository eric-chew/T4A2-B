from main import ma
from models.Feedback import Feedback
from schemas.ProjectSchema import ProjectSchema
from schemas.UserSchema import UserSchema
from marshmallow.validate import Length

class FeedbackSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Feedback

    name = ma.String(required=True, validate=Length(min=1))

    project =  ma.Nested(ProjectSchema)

feedback_schema = FeedbackSchema()
feedbacks_schema = FeedbackSchema(many=True)