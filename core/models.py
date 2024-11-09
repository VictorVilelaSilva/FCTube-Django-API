from math import e
from django.apps import AppConfig
from django.db import models
from django.forms import ValidationError
from django.utils import timezone

# Create your models here.
# verbose_name é o nome que será exibido no admin
class Video(models.Model):
    title        = models.CharField(max_length=100,verbose_name='Título')
    description  = models.TextField(verbose_name='Descrição')
    thumbnail    = models.ImageField(upload_to='thumbnails/',null=True,verbose_name='thumbnail')
    slug         = models.SlugField(max_length=100, unique=True)
    published_at = models.DateTimeField(verbose_name='Publicado em', null=True, editable=False)
    is_published = models.BooleanField(default=False,verbose_name='Está publicado?')
    num_likes    = models.IntegerField(default=0, verbose_name='Número de likes', editable=False)
    num_views    = models.IntegerField(default=0,verbose_name='Número de visualizações',editable=False)
    tags         = models.ManyToManyField('Tags',verbose_name='Tags')
    author       = models.ForeignKey('auth.User',on_delete=models.CASCADE,verbose_name='Autor',editable=False)

    # A classe abaixo faz com que o nome da classe seja exibido no plural e singular no admin
    class Meta:
        verbose_name = 'Vídeo' #singular
        verbose_name_plural = 'Vídeos'#plural
    
    def save(self, *args, **kwargs):
        if self.is_published and not self.published_at:
            self.published_at = timezone.now()
        return super().save(*args, **kwargs)

    def clean (self):
        if self.is_published and not self.thumbnail and not self.video:
            raise ValidationError('Para publicar um Vídeo é necessário enviar um thumbnail e um vídeo')
        

    # A classe abaixo faz com que o nome do objeto seja exibido no admin
    def __srt__(self):
        return self.title


class VideoMedia(models.Model):
    
    class Status(models.TextChoices):
        UPLOADED_STARTED = 'UPLOADED_STARTED', 'Upload iniciado'
        PROCESS_STARTED = 'PROCESSING_STARTED', 'Processamento Iniciado'
        PROCESS_FINISHED = 'PROCESSING_FINISHED', 'Processamento finalizado'
        PROCESS_ERROR = 'PROCESSING_ERROR', 'Erro no Processamento'
    
    video_path = models.CharField(max_length=255, verbose_name='Videos')
    status = models.CharField(max_length=20, choices=Status.choices, default=Status.UPLOADED_STARTED, verbose_name='Status')
    video = models.OneToOneField(Video, on_delete=models.CASCADE, verbose_name='Vídeo', related_name='video_media')

    class Media:
        verbose_name = 'Media'
        verbose_name_plural = 'Midias'

class Tags(models.Model):
    name = models.CharField(max_length=50,unique=True,verbose_name='Nome')

    class Meta:
        verbose_name = 'Tag'
        verbose_name_plural = 'Tags'

    def __str__(self):
        return self.name