from main import ma

class RoleSchema(ma.Schema): 
    class Meta:
        fields = ('id', 
                  'role_name', 
                  'can_view_all', 
                  'can_delete_all', 
                  'can_edit_all', 
                  'can_manage_users', 
                  'can_manage_tickets', 
                  'can_assign_tickets')

role_schema  = RoleSchema()
roles_schema = RoleSchema(many=True)
