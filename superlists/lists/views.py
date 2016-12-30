from django.shortcuts import render
from django.http import HttpResponse

from lists.models import Item

# Create your views here.
def home_page(request):
    item = Item()
    item.text = request.POST.get('item_text', '')
    item.save()

    context = {
        'new_item_text': request.POST.get('item_text', ''),
    }
    return render(request, 'home.html', context)
