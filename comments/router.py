from rest_framework.routers import DefaultRouter
from . import views

router_comments = DefaultRouter()
router_comments.register(prefix='comments', viewset=views.CommentViewSet)
