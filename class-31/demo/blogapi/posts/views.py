from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import Post
from .serializers import PostSerializer

class PostsList(ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class PostsDetail(RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
