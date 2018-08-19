from django.conf.urls import url
from django.urls import include, path
from rest_framework import routers
from reauth import views as reauth

router = routers.DefaultRouter()
router.register(r'users', reauth.UsersViewSet, 'auth')

urlpatterns = [
    url(r'^', include(router.urls)),
    # url(r'^users', api_api.user_profiles, name='user_profiles'),
    url(r'^api/', include('rest_framework.urls', namespace='rest_framework')),
    path('register/', reauth.RegisterUsers.as_view(), name="auth-register"),
]
