from rest_framework import viewsets
from rest_framework.filters import SearchFilter, OrderingFilter
from users.models import User, Payments
from users.serializers import UserSerializer, PaymentsSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class PaymentsViewSet(viewsets.ModelViewSet):
    queryset = Payments.objects.all()
    serializer_class = PaymentsSerializer
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['paid_course', 'paid_lesson', 'payment_method']
    ordering_fields = ['payment_data']
