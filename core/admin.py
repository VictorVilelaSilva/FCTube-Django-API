from django.contrib import admin
from core.models import Video, Tags


class VideoAdmin(admin.ModelAdmin):
    readonly_fields = ("published_at", "num_likes", "num_views", "author")
    list_display = ("title", "is_published", "published_at", "num_likes", "num_views")
    #lookups serve para fazer busca de dados oriundos de relação de tabelas (Ex: tags__name)
    search_fields = ("title", "description", "tags__name")
    #list_filter serve para filtrar dados na tela do admin
    list_filter = ("is_published", "tags")

    def save_model(self, request, obj, form, change):
        if not obj.author_id:
            obj.author = request.user
        super().save_model(request, obj, form, change)
    

# Register your models here.
admin.site.register(Video, VideoAdmin)
admin.site.register(Tags)
