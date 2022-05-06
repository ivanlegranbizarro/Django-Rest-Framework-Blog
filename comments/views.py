from rest_framework import viewsets
from rest_framework.filters import OrderingFilter
from .models import Comment
from .serializers import CommentSerializer
from django_filters.rest_framework import DjangoFilterBackend
from .permissions import IsAdminOrAuthorOrReadOnly


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    lookup_field = 'slug'
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    ordering = ['-created']
    filterset_fields = ['post__slug']
    permission_classes = [IsAdminOrAuthorOrReadOnly]
