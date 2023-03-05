from django.shortcuts import render, redirect
from .models import Item, Tag, Transaction
from django.contrib.auth.models import User
from .forms import  BuyItemForm
from django.utils import timezone
from stores.models import Seller


# Create your views here.
def index(request):

    if not request.user.is_authenticated:
        return redirect('accounts:signin')

    items = Item.objects.all()
    today = Item.objects.filter(publishedDate__day = timezone.now().day)

    return render(request, 'markets/index.html', {'items': items, 'today': today})

def detail(request, pk):

    item = Item.objects.get(pk=pk)
    user = User.objects.get(username=item.seller)
    seller = Seller.objects.get(user=user)
    items = Item.objects.filter(seller=seller).exclude(pk=pk)[:5]
    tags = Tag.objects.filter(item=item)

    return render(request, 'markets/detail.html', {'item': item, 'tags': tags, 'items':items})

def category(request, slug):

    tags = Tag.objects.filter(slug=slug)

    return render(request, 'markets/category.html', {'tags': tags })

def store(request, item_seller):
    
    user = User.objects.get(username=item_seller)
    seller = Seller.objects.get(user=user)
    items = Item.objects.filter(seller=seller)

    return render(request, 'markets/store.html', {'items': items})

def buy(request, pk):
    item = Item.objects.get(pk=pk)

    if request.method == "POST":
        form = BuyItemForm(request.POST)

        if form.is_valid():
            quantity = form.cleaned_data['quantity']
            total = quantity * item.price
            transaction = Transaction(item=item.name, quantity=quantity, total=total, boughtDate=timezone.now(), buyer=request.user, seller=item.seller)
            item.quantity -= quantity

            item.save()
            transaction.save()
            
            if item.quantity < 1:
                item.delete()

            return redirect('markets:index')
            
    else:
        form = BuyItemForm()
    
    return render(request, 'markets/buy.html', {'form': form})


def transaction(request):

    transactions = Transaction.objects.filter(buyer=request.user)

    return render(request, 'markets/transaction.html', {'transactions': transactions})





