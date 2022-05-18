from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import TopicWord, Word


@admin.register(TopicWord)
class TopicWordAdmin(admin.ModelAdmin):
    """Тематика"""
    list_display = ("name", 'translation', 'id', "url", "get_image")
    readonly_fields = ("get_image",)
    list_display_links = ("name",)

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.image.url} width="100" height="110"')
    get_image.short_description = "Изображение"


@admin.register(Word)
class WordAdmin(admin.ModelAdmin):
    list_display = ("word", "id", "transcription",
                    "translation", 'topic', 'draft')
    list_filter = ('topic',)
    search_fields = ["word", 'topic__name']
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
