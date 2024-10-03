from django.urls import path
from rest_framework import routers
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from users.apps import UsersConfig
from users.views import UserViewSet, PaymentsListAPIView, PaymentsCreateAPIView, PaymentsRetrieveAPIView

app_name = UsersConfig.name

router = routers.DefaultRouter()
router.register(r'', UserViewSet, basename='users')


urlpatterns = [
    path('payments/', PaymentsListAPIView.as_view(), name='payments-list'),
    path('token/', TokenObtainPairView.as_view(permission_classes=(AllowAny,)), name='token'),
    path('token/refresh/', TokenRefreshView.as_view(permission_classes=(AllowAny,)), name='token_refresh'),
    path('payment/', PaymentsCreateAPIView.as_view(), name='payment'),
    path('payment/<int:pk>/', PaymentsRetrieveAPIView.as_view(), name='payment-detail')
] + router.urls
