# Generated by Django 2.1.1 on 2018-10-07 21:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('file_holder', '0002_filebank_course_title'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='filebank',
            name='course_title',
        ),
        migrations.AddField(
            model_name='filebank',
            name='description',
            field=models.TextField(default='none'),
        ),
        migrations.AddField(
            model_name='filebank',
            name='file_name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='filebank',
            name='file',
            field=models.FileField(upload_to=''),
        ),
    ]
