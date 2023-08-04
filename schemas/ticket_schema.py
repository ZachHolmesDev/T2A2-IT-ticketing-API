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
                  'assigned_to_user',
                  'comments')
    # display the relations
    created_by_user = fields.Nested('UserSchema', 
                                    only=['id','name', 'email', 'user_role'])
    
    assigned_to_user = fields.Nested('UserSchema',
                                    only=['id','name', 'email', 'user_role'])
    
    comments        = fields.List(fields.Nested('CommentSchema', exclude=['ticket', 'ticket_id']))
    # for hiding feilds contextualy 
    # @post_dump(pass_many=True)


ticket_schema = TicketSchema()
tickets_schema = TicketSchema(many=True)