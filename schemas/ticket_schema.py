from main import ma
from marshmallow import fields, validate, pre_load

VALID_STATUSES = ('incoming', 'open', 'in progress', 'on hold', 'resolved', 'closed')
VALID_PRIORITIES = ('low', 'medium', 'high', 'emergency')

class TicketSchema(ma.Schema):
    class Meta:
        # feilds to expose
        ordered = True
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
                  'assigned_to_user_id', # for loading only
                  'comments')
    # FOR LOADING
    assigned_to_user_id = fields.Int(required=True, 
                                validate=validate.Range(min=1, 
                                error='Cant assign with an empty id'))
    
    # VALIDATION
    title       = fields.String(required=True, 
                                validate=validate.Length(min=1, 
                                error='Title cannot be empty'))
    description = fields.String(required=True, 
                                validate=validate.Length(min=1, 
                                error='Description cannot be empty'))
    priority    = fields.String(required=True, 
                                validate=validate.OneOf(VALID_PRIORITIES, 
                                error='Priority must be one of the following : ' + ', '.join(VALID_PRIORITIES)))
    status      = fields.String(required=True, 
                                validate=validate.OneOf(VALID_STATUSES, 
                                error='Status must be one of the following : ' + ', '.join(VALID_STATUSES)))
    created_at  = fields.DateTime(required=True, 
                                error='Created_at must be a valid datetime')

    # display the relations
    created_by_user  = fields.Nested('UserSchema', 
                                    only=['id','name', 'email', 'user_role'])
    
    assigned_to_user = fields.Nested('UserSchema',
                                    only=['id','name', 'email', 'user_role'])
    
    comments         = fields.List(fields.Nested('CommentSchema', exclude=['ticket', 'ticket_id']))
    
    # lowers the case on incoming priority and status
    @pre_load
    def lower_priority_and_status(self, data, **kwargs):
        if 'priority' in data:
            data['priority'] = data['priority'].lower()
        if 'status' in data:
            data['status'] = data['status'].lower()
        return data
    
    # for hiding feilds contextualy 
    # @post_dump(pass_many=True)


ticket_schema = TicketSchema()
tickets_schema = TicketSchema(many=True)