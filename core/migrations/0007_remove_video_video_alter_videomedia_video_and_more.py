# Generated by Django 5.1.1 on 2024-11-18 04:22

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_alter_video_author_alter_video_thumbnail_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='video',
            name='video',
        ),
        migrations.AlterField(
            model_name='videomedia',
            name='video',
            field=models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, related_name='video_media', to='core.video', verbose_name='Vídeo'),
        ),
        migrations.AlterField(
            model_name='videomedia',
            name='video_path',
            field=models.CharField(max_length=255, verbose_name='Vídeo'),
        ),
    ]
