# Generated by Django 4.1.2 on 2022-10-28 17:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0005_notice_author_notice_bibliography_notice_date_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Newsletter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=90)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
