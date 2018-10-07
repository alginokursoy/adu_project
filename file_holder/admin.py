from django.contrib import admin

# Register your models here.
from .models import FileBank
admin.site.register(FileBank)

from .models import Counter
admin.site.register(Counter)
