from django.db import models

# Create your models here.
class FileBank(models.Model):
    file=models.FileField(null=False, blank=False)
    file_name=models.CharField(blank=True, null=True, max_length=100)
    description=models.TextField(default='none')

    def __str__(self):
        return self.file.name

class Counter(models.Model):
    count=models.PositiveSmallIntegerField(default=0)
