from rest_framework.routers import DefaultRouter

from .views import TaskViewSet

router = DefaultRouter()

router.register(r'task', TaskViewSet, basename= 'task')

urlpatterns = router.urls