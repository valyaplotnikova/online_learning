
from rest_framework import viewsets, generics
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework.permissions import AllowAny

from users.models import User, Payments
from users.serializers import UserSerializer, PaymentsSerializer, UserReadOnlySerializer, PaymentsDetailSerializer
from users.services import create_stripe_product, create_stripe_price, create_stripe_sessions, session_retrieve


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
    filter_backends = [DjangoFilterBackend, OrderingFilter, SearchFilter]
    filterset_fields = ('paid_course', 'paid_lesson', 'payment_method',)
    ordering_fields = ('-payment_data',)


class PaymentsCreateAPIView(generics.CreateAPIView):
    serializer_class = PaymentsSerializer
    queryset = Payments.objects.all()

    def perform_create(self, serializer):
        payment = serializer.save(user=self.request.user)
        product_id = create_stripe_product(payment)
        price = create_stripe_price(payment.amount, product_id)
        session_id, payment_link = create_stripe_sessions(price)
        payment.session_id = session_id
        payment.link_to_payment = payment_link
        payment_status = session_retrieve(session_id)
        payment.payment_status = payment_status
        payment.save()


class PaymentsRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = PaymentsDetailSerializer
    queryset = Payments.objects.all()
