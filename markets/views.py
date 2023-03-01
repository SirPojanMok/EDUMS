from django.shortcuts import render, redirect
from .models import Item, Tag, Transaction
from django.contrib.auth.models import User
from .forms import  BuyItemForm

from stores.models import Seller


# Create your views here.
def index(request):

    if not request.user.is_authenticated:
        return redirect('accounts:signin')

    items = Item.objects.all()

    return render(request, 'markets/index.html', {'items': items})

def detail(request, pk):

    item = Item.objects.get(pk=pk)
    tags = Tag.objects.filter(item=item)

    return render(request, 'markets/detail.html', {'item': item, 'tags': tags})

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
        transaction = Transaction(item = item, buyer = request.user)

        if form.is_valid():

            quantity = form.cleaned_data['quantity']

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





