# Create your tests here.
import unittest
from unittest.mock import patch, Mock
from django.test import RequestFactory
from django.http import HttpResponse
from tutor.views import tutor_list, tutor_detail
from tutor.models import Tutor


class TutorListViewTest(unittest.TestCase):
    def setUp(self):
        """
        Set up the test environment by initializing common resources.
        """
        self.request_factory = RequestFactory()
        self.mocked_tutors = [
            {
                "id": 1,
                "name": "Tutor 1",
                "email": "tutor1@email.com",
                "description": "loren ipsun",
            },
            {
                "id": 2,
                "name": "Tutor 2",
                "email": "tutor1@email.com",
                "description": "loren ipsun",
            },
        ]

    @patch("tutor.views.Tutor.objects.all")
    def test_tutor_list_view(self, mock_tutors):
        """
        Test case for the tutor_list view.
        """
        mock_tutors.return_value = [
            Tutor(**data) for data in self.mocked_tutors
        ]
        request = self.request_factory.get("/tutor")

        response = tutor_list(request)

        self.assertEqual(response.status_code, 200)

    def test_tutor_detail_view(self):
        """
        Test case for the tutor_detail view.
        """
        mock_tutor = Mock()
        mock_tutor.id = 1
        mock_tutor.name = "Mock Tutor"
        mock_tutor.description = "Mock Description"

        with patch("tutor.views.get_object_or_404") as mock_get_object_or_404:
            mock_get_object_or_404.return_value = mock_tutor

            request = self.request_factory.get("/tutor/1/")

            response = tutor_detail(request, tutor_id=1)

        mock_get_object_or_404.assert_called_once_with(Tutor, id=1)

        self.assertIsInstance(response, HttpResponse)

        self.assertEqual(response.status_code, 200)
