from django.contrib import admin
from tutor.models import Instrument, MusicStyle, Tutor


# Register your models here.
class TutorAdmin(admin.ModelAdmin):
    list_display = ["name", "email", "description", "avatar_image", "display_instrument", "display_music_styles", "updated_on", "created_on"] 

    def display_instrument(self, obj):
        return obj.instrument.name if obj.instrument else None  
    display_instrument.short_description = 'Instrument' 

    def display_music_styles(self, obj):
        return obj.music_styles.name if obj.music_styles else None 
    display_music_styles.short_description = 'Music Styles' 

admin.site.register(Tutor, TutorAdmin)
admin.site.register(MusicStyle)
admin.site.register(Instrument)
