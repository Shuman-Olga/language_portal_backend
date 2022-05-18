from django.contrib import admin

from .models import Phrase, TopicPhrase


@admin.register(TopicPhrase)
class TopicPhraseAdmin(admin.ModelAdmin):
    """Тематика"""
    list_display = ("name", 'translation', 'id', "url")
    list_display_links = ("name",)


@admin.register(Phrase)
class WordAdmin(admin.ModelAdmin):
    list_display = ("text", "id", "translation", 'topic', 'draft')
    list_filter = ('topic',)
    search_fields = ['topic__name']
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
