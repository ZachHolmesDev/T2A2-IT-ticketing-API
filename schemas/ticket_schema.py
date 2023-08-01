from main import ma
from marshmallow import fields

# VALID_STATUSES = ()
# VALID_PRIORITIES = ('Low', 'Medium', 'High', 'EMERGANCY')

class TicketSchema(ma.Schema):
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
    # display the relations
    comments        = fields.List(fields.Nested(
                                        'CommentSchema', 
                                        exclude=['ticket']))
    created_by_user = fields.Nested(
                            'UserSchema', 
                            exclude=['created_tickets', 
                                     'created_comments'])
    # for hiding feilds when many hards are viewed
    # @post_dump(pass_many=True)


ticket_schema = TicketSchema()
tickets_schema = TicketSchema(many=True)