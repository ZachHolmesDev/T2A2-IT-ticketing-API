from main import ma
from marshmallow import fields

class TicketCategoriesSchema(ma.Schema):
    class Meta:
        fields = ('ticket_id', 'category_id')

ticket_categories_schema = TicketCategoriesSchema()
ticket_categories_schemas = TicketCategoriesSchema(many=True)