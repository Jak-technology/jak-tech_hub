from rest_framework import serializers
from users.serializers import UserSerializer
from .models import BlogPost, BlogPostComment

        
class BlogPostCommentSerializer(serializers.ModelSerializer):
    # author = serializers.SerializerMethodField(method_name="get_author")
    author = serializers.CharField()
    
    class Meta:
        model = BlogPostComment
        fields = ['id', 'content', 'author', 'email', 'date_created', 'date_updated']

    def create(self, validated_data):
        try:
            blog_post_id = self.context['request'].parser_context['kwargs']['id']
            author = self.get_author(validated_data)
            blogpost = BlogPost.objects.get(id=blog_post_id)
            validated_data['blogpost'] = blogpost
            validated_data['author'] = author
            return super().create(validated_data)
        except Exception as e:
            print("Error:", e)
            raise e

    # def get_author(self, obj):
    #     request = self.context.get('request')
    #     if request and request.user.is_authenticated:
    #         return request.user.username
    #     elif request and 'author' in request.data:
    #         return request.data['author']
    #     else:
    #         raise serializers.ValidationError("Error! Author is not provided")


class BlogPostSerializer(serializers.ModelSerializer):
    author = UserSerializer(read_only=True)
    comments = BlogPostCommentSerializer(many=True, read_only=True)    
    class Meta:
        model = BlogPost
        fields = ['id', 'author', 'title', 'description', 'content', 'image', 'date_created', 'date_updated', 'comments']