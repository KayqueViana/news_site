# Generated by Django 4.1.2 on 2022-10-28 02:03

from django.db import migrations, models
import django.utils.timezone
import news.models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0004_alter_notice_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='notice',
            name='author',
            field=models.CharField(blank=True, max_length=60, null=True),
        ),
        migrations.AddField(
            model_name='notice',
            name='bibliography',
            field=models.TextField(blank=True, max_length=300, null=True),
        ),
        migrations.AddField(
            model_name='notice',
            name='date',
            field=models.DateField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='notice',
            name='highlighted',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='notice',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to=news.models.upload_image_formater),
        ),
        migrations.AddField(
            model_name='notice',
            name='subtitle',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='notice',
            name='title',
            field=models.CharField(max_length=60),
        ),
    ]
