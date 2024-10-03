from rest_framework import serializers

from materials.serializers import LessonSerializer, CourseSerializer
from users.models import User, Payments
from users.services import session_retrieve


class PaymentsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Payments
        fields = '__all__'


class PaymentsDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = Payments
        fields = ('user', 'payment_data', 'amount', 'paid_course', 'paid_lesson', 'payment_status',)


class UserSerializer(serializers.ModelSerializer):
    payments = PaymentsSerializer(source='payments_set', many=True, read_only=True)

    class Meta:
        model = User
        fields = ('payments', 'email', )


class UserReadOnlySerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ("id", "email", "phone", "city", "avatar",)
