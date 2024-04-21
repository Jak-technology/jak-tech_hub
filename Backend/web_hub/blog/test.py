import json
from django.test import TestCase, Client
from django.urls import reverse
from rest_framework import status
from .models import BlogPost
from .serializers import BlogPostSerializer

class TestBlogViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.blog1 = BlogPost.objects.create(title='Model 1-Test Blog 1', content='This is the content of the first test blog.')
        self.blog2 = BlogPost.objects.create(title='Model 1-Test Blog 2', content='This is the content of the second test blog.')

    # def test_blog_create_view(self):
    #     response = self.client.post(reverse('create-blog'),
    #                                 json.dumps({'title': 'Model-1 New Blog', 'content': 'This is the content of the new blog.'}),
    #                                 content_type='application/json')
    #     self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_blog_list_view(self):
        response = self.client.get(reverse('list-blog'))
        blogs = BlogPost.objects.all()
        serializer = BlogPostSerializer(blogs, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_blog_detail_view(self):
        response = self.client.get(reverse('blog-detail', kwargs={'id': self.blog1.id}))
        serializer = BlogPostSerializer(self.blog1)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    # def test_blog_update_view(self):
    #     response = self.client.put(reverse('blog-detail', kwargs={'id': self.blog1.id}),
    #                                json.dumps({'title': 'Updated Blog', 'content': 'This is the updated content of the first test blog.'}),
    #                                content_type='application/json')
    #     self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
    #
    # def test_blog_delete_view(self):
    #     response = self.client.delete(reverse('blog-detail', kwargs={'id': self.blog1.id}))
    #     self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
