from main import ma
from models.Project import Project
from schemas.UserSchema import UserSchema

class ProjectSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Project

    user =  ma.Nested(UserSchema)

project_schema = ProjectSchema()
projects_schema = ProjectSchema(many=True)