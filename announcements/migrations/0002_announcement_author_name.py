# Generated by Django 4.0.10 on 2023-04-29 09:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('announcements', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='announcement',
            name='author_name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
