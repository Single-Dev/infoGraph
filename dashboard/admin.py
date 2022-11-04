from django.contrib import admin
from .models import *

admin.site.register(MyUser)
admin.site.register(Dashboard)


@admin.register(Element)
class CommentAdmin(admin.ModelAdmin):
    # list_display = ('name', 'body', 'post', 'created_on', 'active')
    list_filter = ('active',)
    search_fields = ('title',)
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(active=True)