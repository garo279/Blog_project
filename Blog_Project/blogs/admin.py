from django.contrib import admin
from django.utils.html import format_html
from .models import BlogPost


@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ['title_display', 'owner_display', 'date_added_display', 'preview_content']
    list_filter = ['date_added', 'owner']
    search_fields = ['title', 'text', 'owner__username']
    date_hierarchy = 'date_added'
    ordering = ['-date_added']
    readonly_fields = ['date_added']
    fieldsets = (
        ('基本信息', {
            'fields': ('title', 'owner', 'date_added')
        }),
        ('内容', {
            'fields': ('text',),
            'classes': ('wide',),
        }),
    )

    def title_display(self, obj):
        return obj.title[:50] + "..." if len(obj.title) > 50 else obj.title

    title_display.short_description = '标题'

    def owner_display(self, obj):
        return obj.owner.username

    owner_display.short_description = '作者'

    def date_added_display(self, obj):
        return obj.date_added.strftime('%Y-%m-%d %H:%M')

    date_added_display.short_description = '发布时间'

    def preview_content(self, obj):
        preview = obj.text[:100] + "..." if len(obj.text) > 100 else obj.text
        return format_html('<div style="max-width: 300px;">{}</div>', preview)

    preview_content.short_description = '内容预览'