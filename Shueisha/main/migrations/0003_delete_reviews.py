# Generated by Django 4.1.1 on 2022-09-15 01:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_reviews'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Reviews',
        ),
    ]