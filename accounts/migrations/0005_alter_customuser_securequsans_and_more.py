# Generated by Django 4.0.10 on 2023-04-29 21:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_alter_customuser_securequsans'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='secureQusAns',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='security_question',
            field=models.CharField(choices=[('what is your favorite color?', 'What is your favorite color?'), ("what is your mother's maiden name?", "What is your mother's maiden name?"), ('what is the name of your first pet?', 'What is the name of your first pet?')], max_length=255),
        ),
    ]
