
from rest_framework import viewsets, generics
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter
from rest_framework.permissions import AllowAny

from users.models import User, Payments
from users.serializers import UserSerializer, PaymentsSerializer, UserReadOnlySerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    # serializer_class = UserSerializer
    permission_classes = (AllowAny,)

    def get_serializer_class(self):
        if (self.action == "retrieve" and self.request.user == User.objects.get(pk=self.kwargs.get("pk"))
                or self.request.user.is_superuser):
            return UserSerializer
        return UserReadOnlySerializer

    def perform_create(self, serializer):
        user = serializer.save(is_active=True)
        user.set_password(self.request.data.get('password'))
        user.save()


class PaymentsListAPIView(generics.ListAPIView):
    serializer_class = PaymentsSerializer
    queryset = Payments.objects.all()
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = ('paid_course', 'paid_lesson', 'payment_method',)
    ordering_fields = ['payment_data']
