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

class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'date_posted', 'image_tag')
    search_fields = ('title', 'content')
    list_filter = ('date_posted',)

    def image_tag(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="60" style="object-fit:cover;" />', obj.image.url)
        return '-'
    image_tag.short_description = 'Image'

class ResumeAdmin(admin.ModelAdmin):
    list_display = ('user', 'resume_file')
    search_fields = ('user__username',)

admin.site.unregister(Resume)
admin.site.register(BlogPost, BlogPostAdmin)
admin.site.register(Resume, ResumeAdmin)

admin.site.register(Comment)

admin.site.register(Testimonial)