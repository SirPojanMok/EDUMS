from django.urls import path
from . import views
app_name = 'stores'

urlpatterns = [
    path('', views.viewStore, name='my-store'),
    path('transaction/', views.transaction, name='transaction'),
    path('create-store/', views.createStore, name='create-store'),
    path('delete-store/', views.deleteStore, name='delete-store'),
    path('add-item/', views.addItem, name='add-item'),
    path('edit-item/<int:pk>/', views.editItem, name='edit-item'),
    path('delete-item/<int:pk>/', views.deleteItem, name='edit-item'),
]