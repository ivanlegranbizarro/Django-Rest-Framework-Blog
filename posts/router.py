from rest_framework.routers import DefaultRouter
from . import views

router_posts = DefaultRouter()
router_posts.register(prefix='posts', viewset=views.PostViewSet)
