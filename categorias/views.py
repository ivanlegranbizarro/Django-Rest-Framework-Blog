from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from .models import Category
from .serializers import CategorySerializer
from .permissions import IsAdminOrReadOnly


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    # queryset = Category.objects.filter(published=True)
    serializer_class = CategorySerializer
    permission_classes = (IsAdminOrReadOnly)
    lookup_field = 'slug'
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['published']
