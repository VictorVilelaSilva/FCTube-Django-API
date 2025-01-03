# Generated by Django 5.1.1 on 2024-11-06 03:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_alter_tags_name_alter_video_num_likes_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='thumbnail',
            field=models.ImageField(null=True, upload_to='thumbnails/', verbose_name='thumbnail'),
        ),
        migrations.AlterField(
            model_name='video',
            name='video',
            field=models.FileField(null=True, upload_to='videos/', verbose_name='Vídeo'),
        ),
    ]
