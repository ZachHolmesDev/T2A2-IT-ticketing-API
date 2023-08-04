from main import ma
from marshmallow import fields, validate


class UserSchema(ma.Schema):
    # feilds to expose
    class Meta: 
        ordered = True
        fields = ('id', 
                  'name', 
                  'email', 
                  'password', # for loading incoming passwords only
                  'password_hash',
                  'role', # for loading incoming role names only
                  'user_role',
                  'created_tickets',
                  'assigned_tickets', 
                  'created_comments' )
        load_only = ('password', 'role')
    
    # validation
    name     = fields.String(required=True, 
                             validate=validate.Length(min=1, 
                             error='Name cannot be empty'))
    email    = fields.Email (required=True, 
                             validate=validate.Length(min=1, 
                             error='Email cannot be empty & must be a valid email address'))
    # email    = fields.String(required=True, validate=validate.Regexp(
    #                             r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'))
    password = fields.String(required=True, 
                             validate=validate.Length(min=1, 
                             error='Password cannot be empty'))
    role     = fields.String(required=True, 
                             validate=validate.Length(min=1, 
                             error='Role cannot be empty'))
    # only for loading passwords into the schema to then be hashed and stored in the db
    password  = fields.String()
    # relations
    
    user_role = fields.Nested('RoleSchema', only=['role_name'])

    created_tickets  = fields.List(fields.Nested('TicketSchema', 
                                                 exclude=['created_by_user'] ))
    
    assigned_tickets = fields.List(fields.Nested('TicketSchema', 
                                                 exclude=['assigned_to_user']))
    
    created_comments = fields.List(fields.Nested('CommentSchema', 
                                                 exclude=['user']))
    # for hiding feilds contextualy 
    # @post_dump(pass_many=True)

user_schema  = UserSchema(exclude=['password_hash'])
users_schema = UserSchema(many=True, exclude=['password_hash'   ])


    