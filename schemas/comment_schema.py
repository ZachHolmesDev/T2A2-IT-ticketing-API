from main import ma
from marshmallow import fields, validate


class CommentSchema(ma.Schema): 
    class Meta: 
        ordered = True
        fields  = ('id', 
                   'content', 
                   'user',
                   'user_id',
                   'ticket_id', 
                   'created_at', 
                   'ticket')
    
    # validation
    content    = fields.String(required=True, 
                                validate=validate.Length(min=1, 
                                error='Content cannot be empty'))
    created_at = fields.DateTime(required=True, 
                                error='Created_at must be a valid datetime')
    user_id    = fields.Integer(required=True, 
                                error='User ID is required')
    ticket_id  = fields.Integer(required=True, 
                                error='Ticket ID is required')
    
    # relationships
    user   = fields.Nested('UserSchema',
                            only=['name', 'email'])
    ticket = fields.Nested('TicketSchema', 
                           only=['title', 'description'])

comment_schema  = CommentSchema()
comments_schema = CommentSchema(many=True)
