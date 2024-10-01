from rest_framework import serializers

from materials.models import Course, Lesson, Subscription
from materials.validators import LessonUrlValidator


class LessonSerializer(serializers.ModelSerializer):

    class Meta:
        model = Lesson
        fields = "__all__"
        validators = [LessonUrlValidator(field='url_video')]


class CourseSerializer(serializers.ModelSerializer):
    lesson_count = serializers.SerializerMethodField()
    lessons = LessonSerializer(source='lesson_set', many=True, read_only=True)
    is_subs = serializers.SerializerMethodField()

    def get_lesson_count(self, obj):
        return obj.lesson_set.count()

    def get_is_subs(self, obj):
        request = self.context.get('request')
        return Subscription.objects.filter(course=obj, user=request.user).exists()

    class Meta:
        model = Course
        fields = ['course_name', 'description', 'lesson_count', 'lessons', 'is_subs']


class SubscriptionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Subscription
        fields = '__all__'
