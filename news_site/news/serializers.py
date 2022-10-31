from rest_framework.serializers import ModelSerializer

from .models import Comment, Notice

class NoticeSerializer(ModelSerializer):
    
    def to_representation(self, instance):
        representation = super(NoticeSerializer, self).to_representation(instance)
        representation['date'] = instance.date.strftime('%d/%m/%Y')
        representation['updated_at'] = instance.updated_at.strftime('%d/%m/%Y')
        return representation
    
    class Meta:
        model = Notice
        fields = ["id", "image", "title", "subtitle", "date", "description", "highlighted", "photo", "author", "bibliography", "updated_at"]
        
class CommentSerializer(ModelSerializer):
    
    def to_representation(self, instance):
        representation = super(CommentSerializer, self).to_representation(instance)
        representation['created-at'] = instance.updated_at.strftime('%d/%m/%Y')
        return representation
    
    class Meta:
        model = Comment
        fields = ["id", "photo", "name", "surname", "comment", "active", "created_at"]
    