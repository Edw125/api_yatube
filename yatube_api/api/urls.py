from django.urls import include, path
from rest_framework import routers

from rest_framework.authtoken import views

from api.views import CommentViewSet, GroupViewSet, PostViewSet, UserViewSet


router = routers.DefaultRouter()
router.register(r'posts', PostViewSet)
router.register(r'groups', GroupViewSet, basename='groups')
router.register(r'users', UserViewSet, basename='users')
router.register(
    r'posts/(?P<post_id>\d+)/comments', CommentViewSet, basename='comments'
)

urlpatterns = [
    path('api/v1/api-token-auth/', views.obtain_auth_token),
    path('api/v1/', include(router.urls)),
]
