from django.contrib import admin
from .models import *
from django.utils.html import format_html
# Register your models here.

admin.site.register(User)
admin.site.register(Project)
class AboutAdmin(admin.ModelAdmin):
    list_display = ('user', 'bio', 'profile_image_preview')

    def profile_image_preview(self, obj):
        if obj.profile_image:
            return format_html('<img src="{}" width="50" height="50" style="border-radius:50%;" />', obj.profile_image.url)
        return "No Image"

    profile_image_preview.short_description = 'Profile Image'

admin.site.register(About, AboutAdmin)
admin.site.register(TechStack)
admin.site.register(Resume)