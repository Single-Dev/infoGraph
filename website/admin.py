from django.contrib import admin
from .models import *

admin.site.register(Users)
admin.site.register(Countrys)
admin.site.register(Profile)
admin.site.register(Dashboard)
admin.site.register(Category)

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'body', 'post', 'created_on', 'active')
    list_filter = ('active', 'created_on')
    search_fields = ('name', 'body')
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(active=True)