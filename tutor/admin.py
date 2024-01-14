from django.contrib import admin
from tutor.models import Instrument, MusicStyle, Tutor

# Register your models here.
admin.site.register(Tutor)
admin.site.register(Instrument)
admin.site.register(MusicStyle)
