from django.db import models

# Create your models here.
class FileBank(models.Model):
    file=models.FileField(null=False, blank=False)
    course_title=models.CharField(blank=True, null=True, max_length=100)

    def __str__(self):
        return self.file.name
