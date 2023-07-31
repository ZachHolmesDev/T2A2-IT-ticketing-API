from main import ma
from marshmallow import fields

# VALID_STATUSES = ()
# VALID_PRIORITIES = ('Low', 'Medium', 'High', 'EMERGANCY')

class TicketSchema(ma.Schema):
    comments        = fields.List(fields.Nested(
                                        'CommentSchema', 
                                        exclude=['ticket']))
    created_by_user = fields.Nested(
                            'UserSchema', 
                            exclude=['created_tickets', 
                                     'created_comments'])
    class Meta:
        fields = ('id', 
                  'title', 
                  'description', 
                  'priority', 
                  'status', 
                  'created_at', 
                  'updated_at', 
                  'user_id', 
                  'created_by_user', 
                  'comments')

ticket_schema = TicketSchema()
tickets_schema = TicketSchema(many=True)