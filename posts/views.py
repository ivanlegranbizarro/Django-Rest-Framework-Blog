from rest_framework import viewsets
from .models import Post
from .serializers import PostSerializer
from .permissions import IsAdminOrAuthorOrReadOnly
from django_filters.rest_framework import DjangoFilterBackend


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAdminOrAuthorOrReadOnly]
    lookup_field = 'slug'
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['category__slug']

