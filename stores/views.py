from django.shortcuts import render, redirect
from django.contrib.auth import authenticate

from .forms import CreateStoreForm, DeleteStoreForm, AddItemForm
from .models import Seller
from markets.models import Item, Transaction
from django.utils import timezone

# Create your views here.
def createStore(request):

    if request.method == "POST":
        form = CreateStoreForm(request.POST)

        if form.is_valid():
            formObject = form.save(commit=False)
            formObject.user = request.user
            formObject.save()

            return redirect('stores:my-store')
    else:
        form = CreateStoreForm()

    return render(request, 'stores/create-store.html', {'form': form})

def viewStore(request):

    try:
        seller = Seller.objects.get(user=request.user)
        items = Item.objects.filter(seller=seller)

    except Seller.DoesNotExist:
        return redirect('markets:index')

    return render(request, 'stores/view-store.html', {'items': items})

def deleteStore(request):

    seller = Seller.objects.get(user=request.user)
    
    if request.method == "POST":
        form = DeleteStoreForm(request.POST)

        if form.is_valid():

            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            user = authenticate(username=username, password=password)

            if seller.user == user:
                seller.delete()

                return redirect('markets:index')
            
    else:
        form = DeleteStoreForm()

    return render(request, 'stores/delete-store.html', {'form': form})

def addItem(request):
    seller = Seller.objects.get(user=request.user)

    if request.method == "POST":
        form = AddItemForm(request.POST, request.FILES)

        if form.is_valid():
            formObject = form.save(commit=False)
            formObject.seller = seller
            formObject.publishedDate = timezone.now()
            formObject.save()

            return redirect('stores:my-store')
    
    else:
        form = AddItemForm()

    return render(request, 'stores/add-item.html', {'form': form})

def editItem(request, pk):

    item = Item.objects.get(pk=pk)

    if request.method == "POST":
        form = AddItemForm(request.POST, request.FILES, instance=item)

        if form.is_valid():
            form.save()

            return redirect('stores:my-store')
    
    else:
        form = AddItemForm(instance=item)

    return render(request, 'stores/edit-item.html', {'form': form})

def deleteItem(request, pk):

    item = Item.objects.get(pk=pk)

    if request.method == "POST":
        item.delete()

        return redirect('stores:my-store')

    return render(request, 'stores/delete-item.html', {'item': item})

def transaction(request):

    seller = Seller.objects.get(user=request.user)
    transactions = Transaction.objects.filter(seller=seller)

    return render(request, 'stores/transaction.html', {'transactions': transactions})