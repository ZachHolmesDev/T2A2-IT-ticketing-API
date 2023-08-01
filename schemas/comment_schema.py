from main import ma
from marshmallow import fields


class CommentSchema(ma.Schema):
    user   = fields.Nested('UserSchema', only=['name', 'email'])
    ticket = fields.Nested('TicketSchema', only=['title', 'description'])
    
    class Meta: 
        ordered = True
        fields  = ('id', 
                   'content', 
                   'user',
                   'user_id',
                   'ticket_id', 
                   'created_at', 
                   'ticket')
    
    
comment_schema = CommentSchema()
comments_schema = CommentSchema(many=True)
