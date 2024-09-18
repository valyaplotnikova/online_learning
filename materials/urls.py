from materials.apps import MaterialsConfig
from rest_framework import routers

from materials.views import CourseViewSet

app_name = MaterialsConfig.name

router = routers.DefaultRouter()
router.register(r'course', CourseViewSet, basename='course')

urlpatterns = [

] + router.urls
