from rest_framework import routers

from users.apps import UsersConfig
from users.views import UserViewSet, PaymentsViewSet

app_name = UsersConfig.name

router = routers.DefaultRouter()
router.register(r'', UserViewSet, basename='users')
router.register(r'payments', PaymentsViewSet, basename='payments')

urlpatterns = [

] + router.urls
