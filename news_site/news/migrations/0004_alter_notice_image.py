# Generated by Django 4.1.2 on 2022-10-27 01:58

from django.db import migrations, models
import news.models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0003_alter_notice_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notice',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=news.models.upload_image_formater),
        ),
    ]
