from main import ma
from marshmallow import fields

class CategoriesSchema(ma.Schema):
    class Meta:
        fields = ('id', 'categorie_name')

categories_schema = CategoriesSchema()
categories_schemas = CategoriesSchema(many=True)
