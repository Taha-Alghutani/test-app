from django.shortcuts import render
import socket
from .models import Item

# Create your views here.
def index(request):
    hostname = socket.gethostname()
    return render(request, 'app/index.html', {
        'container_id': hostname
    })
def items(request):
    items = Item.objects.all()
    return render(request, 'app/item_list.html', {
        'items': items
    })
