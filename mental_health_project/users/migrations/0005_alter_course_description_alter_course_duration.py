# Generated by Django 4.0.10 on 2024-04-24 18:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_alter_course_duration'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='description',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='course',
            name='duration',
            field=models.FloatField(help_text='Duration in years'),
        ),
    ]