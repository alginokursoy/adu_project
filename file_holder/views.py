from django.shortcuts import render

# Create your views here.
from .models import FileBank
from .models import Counter

def home(request):
    k=Counter.objects.get(pk=1)
    k.count=k.count+1
    k.save()
    context={
    'files':FileBank.objects.all(),
    'counter':k
    }
    return render(request, 'file_holder/home.html',context)
