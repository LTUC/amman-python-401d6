from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .models import Post
from .permissions import IsAuthorOrReadOnly
from .serializers import PostSerializer


class PostList(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticatedOrReadOnly,)
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthorOrReadOnly,)
    queryset = Post.objects.all()
    serializer_class = PostSerializer
