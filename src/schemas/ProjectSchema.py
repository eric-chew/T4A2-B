from main import ma
from models.Project import Project
from schemas.UserSchema import UserSchema
from marshmallow.validate import Length, URL


class ProjectSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Project

    name = ma.String(required=True, validate=Length(min=1))
    link = ma.String(required=True, validate=URL())

    user = ma.Nested(UserSchema)


project_schema = ProjectSchema()
projects_schema = ProjectSchema(many=True)
