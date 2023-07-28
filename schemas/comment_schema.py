from main import ma
from marshmallow import fields


class CommentSchema(ma.Schema):
    class Meta:
        fields = ('id', 'content', 'created_at', 'user_id', 'ticket_id')

comment_schema = CommentSchema()
comments_schema = CommentSchema(many=True)