from main import ma
from marshmallow import fields


class UserSchema(ma.Schema):
    created_comments = fields.List(fields.Nested('CommentSchema', exclude=['user']))
    class Meta: 
        ordered = True
        fields = ('id', 'name', 'email', 'password_hash','role_id', 'tickets', 'created_comments', )

user_schema  = UserSchema(exclude=['password_hash'])
users_schema = UserSchema(many=True, exclude=['password_hash'])


    # tickets  = fields.List(fields.Nested('TicketSchema',  exclude=['user']))
    # comments = fields.List(fields.Nested('CommentSchema', exclude=['user']))
    
    # created_tickets  = fields.Nested('TicketSchema', exclude=['user'])
    # assigned_tickets = fields.List(fields.Nested('TicketSchema', exclude=['user']))
    # created_comments    = fields.List(fields.Nested('CommentSchema'))
    