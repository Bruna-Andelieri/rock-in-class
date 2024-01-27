from django.contrib import admin
from booking.models import Booking

# Register your models here.


class BookingAdmin(admin.ModelAdmin):
    list_display = [
        "student",
        "display_tutor",
        "booking_date",
        "booking_time",
        "message",
    ]

    def display_tutor(self, obj):
        """
        Displays the name of the tutor associated with the given object.
        """
        return obj.tutor.name if obj.tutor else None

    display_tutor.short_description = "Tutor"


admin.site.register(Booking, BookingAdmin)
