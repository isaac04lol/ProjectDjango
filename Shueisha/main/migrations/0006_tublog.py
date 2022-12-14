# Generated by Django 4.1.1 on 2022-09-21 23:50

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_review_is_active'),
    ]

    operations = [
        migrations.CreateModel(
            name='TuBlog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('author', models.CharField(blank=True, max_length=200, null=True)),
                ('name', models.CharField(blank=True, max_length=200, null=True)),
                ('description', models.CharField(blank=True, max_length=500, null=True)),
                ('body', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('slug', models.SlugField(blank=True, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='tublog')),
                ('is_active', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'tublog',
                'verbose_name_plural': 'Tu Blog',
                'ordering': ['timestamp'],
            },
        ),
    ]
