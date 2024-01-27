from django.http import Http404

# Create your tests here.
import unittest
from unittest.mock import patch, MagicMock
from booking.models import Booking

from booking.views import delete_booking


class DeleteBookingViewTest(unittest.TestCase):
    @patch("booking.views.get_object_or_404")
    @patch("booking.views.messages.success")
    def test_delete_booking_view(
        self, mock_messages_success, mock_get_object_or_404
    ):
        user = MagicMock()
        booking_id = 1
        booking = MagicMock()
        booking.pk = booking_id
        user.return_value = booking

        form_data = {"delete": True}
        request = MagicMock()
        request.method = "POST"
        request.POST = form_data

        request.user = user

        mock_get_object_or_404.return_value = booking

        delete_booking(request, booking_id)

        mock_get_object_or_404.assert_called_once_with(
            Booking, pk=booking_id, student=request.user
        )

        booking.delete.assert_called_once()

        mock_messages_success.assert_called_once_with(
            request, "Booking deleted successful"
        )

    @patch("booking.views.get_object_or_404")
    def test_delete_booking_view_not_post(self, mock_get_object_or_404):
        user = MagicMock()
        booking_id = 1
        booking = MagicMock()
        booking.pk = booking_id
        user.return_value = booking

        mock_get_object_or_404.return_value = booking

        request = MagicMock()
        request.method = "GET"
        request.user = user

        response = delete_booking(request, booking_id)

        mock_get_object_or_404.assert_called_once_with(
            Booking, pk=booking_id, student=request.user
        )

        self.assertEqual(response.status_code, 200)

    @patch("booking.views.get_object_or_404", side_effect=Http404)
    def test_delete_booking_view_booking_not_found(
        self, mock_get_object_or_404
    ):
        user = MagicMock()
        booking_id = 1

        mock_get_object_or_404.side_effect = Http404

        request = MagicMock()
        request.method = "GET"
        request.user = user

        with self.assertRaises(Http404):
            delete_booking(request, booking_id)

        mock_get_object_or_404.assert_called_once_with(
            Booking, pk=booking_id, student=request.user
        )
