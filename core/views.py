from django.shortcuts import render

from .models import Phones


# Create your views here.
def index(request):
    phones = Phones.objects.all()
    return render(request, "index.html", {"phones": phones})

