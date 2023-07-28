from main import ma
from marshmallow import fields


from marshmallow import fields

class TicketSchema(ma.Schema):
    comments = fields.List(fields.Nested('CommentSchema', exclude=['ticket']))

    class Meta:
        fields = ('id', 'title', 'description', 'priority', 'status', 'created_at', 'updated_at', 'user_id', 'assigned_to', 'comments')

ticket_schema = TicketSchema()
tickets_schema = TicketSchema(many=True)