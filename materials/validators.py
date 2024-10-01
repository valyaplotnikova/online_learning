from rest_framework import serializers


class LessonUrlValidator:
    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        video_url = value.get(self.field)
        if video_url and not video_url.startswith('https://www.youtube.com/'):
            raise serializers.ValidationError("Вы не можете использовать видео с данного источника")
