# Generated by Django 2.1.1 on 2018-10-07 17:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('file_holder', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='filebank',
            name='course_title',
            field=models.CharField(max_length=15, null=True),
        ),
    ]