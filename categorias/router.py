from rest_framework.routers import DefaultRouter
from . import views

router_categories = DefaultRouter()
router_categories.register(prefix='categories', viewset=views.CategoryViewSet)
