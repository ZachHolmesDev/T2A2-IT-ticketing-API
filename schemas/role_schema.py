from main import ma
# from marshmallow import Schema, fields


class RoleSchema(ma.Schema): 
    class Meta                 : 
        fields = ('id', 
                  'role_name', 
                  'can_view_all', 
                  'can_manage', 
                  'can_action')

role_schema  = RoleSchema()
roles_schema = RoleSchema(many=True)
