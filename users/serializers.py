from rest_framework import serializers

from materials.serializers import LessonSerializer, CourseSerializer
from users.models import User, Payments


class PaymentsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Payments
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    payments = PaymentsSerializer(source='payments_set', many=True)

    class Meta:
        model = User
        fields = ('payments', 'email', )
