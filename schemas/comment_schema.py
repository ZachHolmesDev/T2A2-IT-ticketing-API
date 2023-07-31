from main import ma
from marshmallow import fields


class CommentSchema(ma.Schema):
    user   = fields.Nested('UserSchema', only=['name', 'email'])
    ticket = fields.Nested('TicketSchema', only=['title', 'description'])
    
    class Meta: 
        ordered = True
        fields  = ('id', 'content', 'created_at', 'user', 'ticket')
    
    
comment_schema = CommentSchema()
comments_schema = CommentSchema(many=True)
