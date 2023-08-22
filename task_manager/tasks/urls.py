from .views import TaskViewSet
from rest_framework import routers



app_name = 'tasks'

router = routers.DefaultRouter()
router.register('tasks', TaskViewSet, 'tasks')


urlpatterns = router.urls