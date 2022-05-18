from django.contrib import admin
from .models import TopicVideo, Video


@admin.register(TopicVideo)
class TopicVideodAdmin(admin.ModelAdmin):
    """Тематика"""
    list_display = ("name", 'id', "url",)
    list_display_links = ("name",)


@admin.register(Video)
class VideoAdmin(admin.ModelAdmin):
    list_display = ("title", "id", "videoid", "url", "topic", "draft")
    list_filter = ('topic',)
    search_fields = ["title", "topic__name"]
    save_on_top = True
    save_as = True
    list_editable = ("draft",)
    actions = ["publish", "unpublish"]

    def unpublish(self, request, queryset):
        """Снять с публикации"""
        row_update = queryset.update(draft=True)
        if row_update == 1:
            message_bit = "1 запись была обновлена"
        else:
            message_bit = f"{row_update} записей были обновлены"
        self.message_user(request, f"{message_bit}")

    def publish(self, request, queryset):
        """Опубликовать"""
        row_update = queryset.update(draft=False)
        if row_update == 1:
            message_bit = "1 запись была обновлена"
        else:
            message_bit = f"{row_update} записей были обновлены"
        self.message_user(request, f"{message_bit}")

    publish.short_description = "Опубликовать"
    publish.allowed_permissions = ('change', )

    unpublish.short_description = "Снять с публикации"
    unpublish.allowed_permissions = ('change',)


admin.site.site_title = "Language Portal"
admin.site.site_header = "Language Portal"
