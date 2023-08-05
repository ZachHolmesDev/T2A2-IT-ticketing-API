from main import ma
from marshmallow import fields, validate, post_dump, pre_dump


class UserSchema(ma.Schema):
    class Meta: 
        # feilds to expose
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
                  'created_comments' ,
                  'created_comments_count')
        load_only = ('password', 'role')
    
    # LOADING FEILDS
    # only for loading name of role so it can be searched for by name
                # TODO should be changed to oneof ???
                # might requrire rework of other things 
                # by this point but will probably simplify the logic 
    role     = fields.String(required=True, 
                             validate=validate.Length(min=1, 
                             error='Role cannot be empty'))
    # only for loading passwords into the schema to then be hashed and stored in the db
    password  = fields.String()
    
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
   
    # relations
    user_role = fields.Nested('RoleSchema', only=['role_name'])

    created_tickets  = fields.List(fields.Nested('TicketSchema', 
                                                 exclude=['created_by_user', 'comments'] ))
    
    assigned_tickets = fields.List(fields.Nested('TicketSchema', 
                                                 exclude=['assigned_to_user', 'comments']))
    
    created_comments = fields.List(fields.Nested('CommentSchema', 
                                                 exclude=['user']))
    
    # experiment afer finished 
    
    # # for hiding feilds contextualy 
    # # @post_dump(pass_many=True)
    # # def show_or_hide_feilds(self, data, many):
    # #     pass
    # # @post_dump(pass_original=True)
    # # def add_ticket_counts(self, data, original_data, **kwargs):
    # #     data['created_tickets_count']  = len(original_data.created_tickets)
    # #     data['assigned_tickets_count'] = len(original_data.assigned_tickets)
    # #     data['created_comments_count'] = len(original_data.created_comments)
    # #     return data
    # created_tickets_count = fields.Integer(dump_only=True)
    # assigned_tickets_count = fields.Integer(dump_only=True)
    # created_comments_count = fields.Integer(dump_only=True)

    # @pre_dump(pass_many=True)
    # def calculate_ticket_counts(self, data, many, **kwargs):
    #     if many:
    #         for user in data:
    #             user.created_tickets_count = len(user.created_tickets)
    #             user.assigned_tickets_count = len(user.assigned_tickets)
    #             user.created_comments_count = len(user.created_comments)
    #     else:
    #         data.created_tickets_count = len(data.created_tickets)
    #         data.assigned_tickets_count = len(data.assigned_tickets)
    #         data.created_comments_count = len(data.created_comments)
    #     return data 
    

user_schema  = UserSchema(exclude=['password_hash'])
users_schema = UserSchema(many=True, exclude=['password_hash', 'created_tickets', 'assigned_tickets', 'created_comments'])

    