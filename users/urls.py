from django.urls import path
from rest_framework import routers

from users.apps import UsersConfig
from users.views import UserViewSet, PaymentsListAPIView

app_name = UsersConfig.name

router = routers.DefaultRouter()
router.register(r'', UserViewSet, basename='users')


urlpatterns = [
    path('payments/', PaymentsListAPIView.as_view(), name='payments-list'),
] + router.urls
