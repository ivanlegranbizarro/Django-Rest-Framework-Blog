from rest_framework import permissions
from django.contrib import admin
from django.urls import path, include
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from categorias.router import router_categories
from posts.router import router_posts
from comments.router import router_comments

schema_view = get_schema_view(
    openapi.Info(
        title="Blog Api",
        default_version='v1',
        description="Documentación de la Api del Blog de Iván",
        terms_of_service="",
        contact=openapi.Contact(email="ivanlegranbizarro@gmail.com"),
        license=openapi.License(name="MIT"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/users/', include('users.urls', namespace='users')),
    path('api/', include(router_categories.urls)),
    path('api/', include(router_posts.urls)),
    path('api/', include(router_comments.urls)),
    path('docs/', schema_view.with_ui('swagger',
                                      cache_timeout=0), name='schema-swagger-io'),
    path('redocs/', schema_view.with_ui('redoc',
                                        cache_timeout=0), name='schema-redoc')
]
