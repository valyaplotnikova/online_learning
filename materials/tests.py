from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from materials.models import Course, Lesson, Subscription
from users.models import User


class LessonTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create(email="test@test.ru")
        self.course = Course.objects.create(course_name='Test_course')
        self.lesson = Lesson.objects.create(lesson_name="Test_lesson", course=self.course, owner=self.user)
        self.client.force_authenticate(user=self.user)

    def test_lesson_retrieve(self):
        """ Тестируем просмотр урока. """
        url = reverse('materials:lesson-get', args=(self.lesson.pk,))
        response = self.client.get(url)
        data = response.json()
        self.assertEqual(
            response.status_code, status.HTTP_200_OK
        )
        self.assertEqual(
            data.get("lesson_name"), self.lesson.lesson_name
        )

    def test_lesson_create(self):
        """ Тестируем создание урока. """
        url = reverse('materials:lesson-create')
        data = {
            "lesson_name": "New_lesson"
        }
        response = self.client.post(url, data)
        self.assertEqual(
            response.status_code, status.HTTP_201_CREATED
        )
        self.assertEqual(
            Lesson.objects.all().count(), 2
        )

    def test_lesson_update(self):
        """ Тестируем редактирование урока. """
        url = reverse('materials:lesson-update', args=(self.lesson.pk,))
        data = {
            "lesson_name": "Lesson_update"
        }
        response = self.client.patch(url, data)
        data = response.json()
        self.assertEqual(
            response.status_code, status.HTTP_200_OK
        )
        self.assertEqual(
            data.get("lesson_name"), "Lesson_update"
        )

    def test_lesson_delete(self):
        """ Тестируем удаление урока. """
        url = reverse('materials:lesson-delete', args=(self.lesson.pk,))
        response = self.client.delete(url)
        self.assertEqual(
            response.status_code, status.HTTP_204_NO_CONTENT
        )
        self.assertEqual(
            Lesson.objects.all().count(), 0
        )

    def test_lesson_list(self):
        """ Тестируем просмотр списка уроков. """
        url = reverse('materials:lesson-list')
        response = self.client.get(url)
        data = response.json()
        result = {
            "count": 1,
            "next": None,
            "previous": None,
            "results":
                [
                    {
                        "id": self.lesson.pk,
                        "lesson_name": self.lesson.lesson_name,
                        "description": None,
                        "preview": None,
                        "url_video": None,
                        "course": self.lesson.course.pk,
                        "owner": self.user.pk
                    }
                ]
        }

        self.assertEqual(
            response.status_code, status.HTTP_200_OK
        )
        self.assertEqual(
            result, data
        )


class SubscriptionTestCase(APITestCase):

    def setUp(self):
        self.user = User.objects.create(email="test@test.com")
        self.course = Course.objects.create(course_name="Test Course", description="Test Course description")
        self.subscription = Subscription.objects.create(user=self.user, course=self.course)
        self.client.force_authenticate(user=self.user)

    def test_subscription_create(self):
        """Тест функционала работы подписки на обновления курса"""
        url = reverse("materials:subscription")
        data = {
            "user": self.user.pk,
            "course": self.course.pk,
        }
        response = self.client.post(url, data)
        response.json()
        self.assertEqual(
            response.status_code, status.HTTP_200_OK
        )
        self.assertEqual(
            response.json(), {"message": "подписка удалена"}
        )


class CourseTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create(email="test@test.ru")
        self.course = Course.objects.create(course_name='Test_course', owner=self.user)
        self.lesson = Lesson.objects.create(lesson_name="Test_lesson", course=self.course, owner=self.user)
        self.client.force_authenticate(user=self.user)

    def test_course_retrieve(self):
        """ Тестируем просмотр курса. """
        url = reverse('materials:course-detail', args=(self.course.pk,))
        response = self.client.get(url)
        data = response.json()
        self.assertEqual(
            response.status_code, status.HTTP_200_OK
        )
        self.assertEqual(
            data.get("course_name"), self.course.course_name
        )

    def test_course_create(self):
        """ Тестируем создание курса. """
        url = reverse('materials:course-list')
        data = {
            "course_name": "New_course"
        }
        response = self.client.post(url, data)
        self.assertEqual(
            response.status_code, status.HTTP_201_CREATED
        )
        self.assertEqual(
            Course.objects.all().count(), 2
        )

    def test_course_update(self):
        """ Тестируем редактирование курса. """
        url = reverse('materials:course-list', args=(self.course.pk,))
        data = {
            "course_name": "course_update"
        }
        response = self.client.patch(url, data)
        data = response.json()
        self.assertEqual(
            response.status_code, status.HTTP_200_OK
        )
        self.assertEqual(
            data.get("course_name"), "course_update"
        )
    #
    # def test_lesson_delete(self):
    #     """ Тестируем удаление урока. """
    #     url = reverse('materials:lesson-delete', args=(self.lesson.pk,))
    #     response = self.client.delete(url)
    #     self.assertEqual(
    #         response.status_code, status.HTTP_204_NO_CONTENT
    #     )
    #     self.assertEqual(
    #         Lesson.objects.all().count(), 0
    #     )
    #
    # def test_lesson_list(self):
    #     """ Тестируем просмотр списка уроков. """
    #     url = reverse('materials:lesson-list')
    #     response = self.client.get(url)
    #     data = response.json()
    #     result = {
    #         "count": 1,
    #         "next": None,
    #         "previous": None,
    #         "results":
    #             [
    #                 {
    #                     "id": self.lesson.pk,
    #                     "lesson_name": self.lesson.lesson_name,
    #                     "description": None,
    #                     "preview": None,
    #                     "url_video": None,
    #                     "course": self.lesson.course.pk,
    #                     "owner": self.user.pk
    #                 }
    #             ]
    #     }
    #
    #     self.assertEqual(
    #         response.status_code, status.HTTP_200_OK
    #     )
    #     self.assertEqual(
    #         result, data
    #     )
    #
