from models.User import User
from main import ma
from marshmallow.validate import Length, Email


class UserSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = User
        load_only = ['password']

    username = ma.String(required=True, validate=Length(min=1))
    email = ma.String(
        required=True,
        validate=[Length(min=4, max=254), Email()]
    )
    password = ma.String(required=True, validate=Length(min=8))


user_schema = UserSchema()
users_schema = UserSchema(many=True)
