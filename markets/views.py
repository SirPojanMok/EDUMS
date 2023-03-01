from django.shortcuts import render, redirect
from .models import Item, Tag
from django.contrib.auth.models import User
from .forms import AddItemForm
from django.utils import timezone

# Create your views here.
def index(request):

    items = Item.objects.all()

    return render(request, 'markets/index.html', {'items': items})

def detail(request, pk):
    item = Item.objects.get(pk=pk)
    tags = Tag.objects.filter(item=item)

    return render(request, 'markets/detail.html', {'item': item, 'tags': tags})

def category(request, slug):

    tag = Tag.objects.get(slug=slug)

    return render(request, 'markets/category.html', {'tag': tag})

def store(request, item_seller):

    seller = User.objects.get(username=item_seller)
    items = Item.objects.filter(seller=seller)

    return render(request, 'markets/store.html', {'items': items})

def sell(request):

    if request.method == "POST":
        form = AddItemForm(request.POST, request.FILES)

        if form.is_valid():
            formObject = form.save(commit=False)
            formObject.seller = request.user
            formObject.publishedDate = timezone.now()
            formObject.save()

            return redirect('markets:index')
    
    else:
        form = AddItemForm()

    return render(request, 'markets/add.html', {'form': form})





