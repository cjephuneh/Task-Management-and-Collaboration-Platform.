from .views import UserViewSet, UserLoginViewSet
from rest_framework import routers

app_name = 'authentication'

router = routers.DefaultRouter()
router.register('users', UserViewSet, 'register')
router.register('login', UserLoginViewSet, 'login')



urlpatterns = router.urls
