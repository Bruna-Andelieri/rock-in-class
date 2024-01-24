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
    ]  # Lista todas as colunas do modelo

    def display_tutor(self, obj):
        return obj.tutor.name if obj.tutor else None  # Substitua pelo campo que deseja exibir

    display_tutor.short_description = "Tutor"  # Define um título para a coluna


admin.site.register(Booking, BookingAdmin)
