from main import ma
from marshmallow import fields


class UserSchema(ma.Schema):
    tickets  = fields.List(fields.Nested('TicketSchema',  exclude=['user']))
    comments = fields.List(fields.Nested('CommentSchema', exclude=['user']))

    class Meta: 
        fields = ('id', 
                  'name', 
                  'email', 
                  'role_id',
                  'password_hash', 
                  'tickets', 
                  'comments')

user_schema  = UserSchema(exclude=['password_hash'])
users_schema = UserSchema(many=True, exclude=['password_hash'])