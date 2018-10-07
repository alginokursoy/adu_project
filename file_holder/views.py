from django.shortcuts import render

# Create your views here.
from .models import FileBank

def home(request):
    context={
    'files':FileBank.objects.all()
    }
    return render(request, 'file_holder/home.html',context)
