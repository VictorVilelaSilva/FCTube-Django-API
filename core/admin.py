from django.contrib import admin
from django.contrib.auth.admin import csrf_protect_m
from django.http import JsonResponse
from django.shortcuts import render
from django.urls import path, reverse
from django.utils.html import format_html
from django.views.decorators.csrf import csrf_exempt, csrf_protect
from core.form import VideoChunkUploadForm
from core.models import Video, Tags
from core.services import VideoService


class VideoAdmin(admin.ModelAdmin):
    readonly_fields = ("published_at", "num_likes", "num_views", "author")
    list_display = ("title", "is_published", "published_at", "num_likes", "num_views","redirect_to_upload")
    #lookups serve para fazer busca de dados oriundos de relação de tabelas (Ex: tags__name)
    search_fields = ("title", "description", "tags__name")
    #list_filter serve para filtrar dados na tela do admin
    list_filter = ("is_published", "tags")

    def save_model(self, request, obj, form, change):
        if not obj.pk:
            obj.author = request.user
        super().save_model(request, obj, form, change)

    def get_urls(self):
        urls = super().get_urls()
        custom_urls = [
            path(
                '<int:id>/upload-video', 
                self.upload_video, 
                name='core_video_upload'
            ),
            path(
                '<int:id>/upload-video/finish', 
                self.finish_upload_video, 
                name='core_video_upload_finish'
            )
            ]
        return custom_urls + urls
    
    def redirect_to_upload(self, obj: Video):
        url = reverse('admin:core_video_upload', args=[obj.id])
        return format_html(f'<a href="{url}">Upload</a>')
    
    def finish_upload_video(self, request, id):
        pass

    redirect_to_upload.short_description = "Upload"

    @csrf_protect_m
    def upload_video(self, request, id):

        if request.method == 'POST':
            form = VideoChunkUploadForm(request.POST, request.FILES)
            if not form.is_valid():
                return JsonResponse({'error':form.errors}, status=400)
            
            VideoService().process_upload(
            video_id=id,
            chunck_index = form.cleaned_data['chunckIndex'],
            chunck = form.cleaned_data['chunck'].read()
            )
            pass
        context = dict(
            id = id
        )
        return render(request, 'admin/core/upload_video.html', context)
    
# Register your models here.
admin.site.register(Video, VideoAdmin)
admin.site.register(Tags)
