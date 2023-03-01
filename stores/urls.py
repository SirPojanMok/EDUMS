from django.urls import path
from . import views
app_name = 'stores'

urlpatterns = [
    path('create-store/', views.createStore, name='create-store'),
    path('my-store/', views.viewStore, name='my-store'),
    path('my-store/delete/', views.deleteStore, name='delete-store'),
    path('my-store/add-item/', views.addItem, name='add-item'),
    path('my-store/edit-item/<int:pk>/', views.editItem, name='edit-item'),
    path('my-store/delete-item/<int:pk>/', views.deleteItem, name='edit-item'),
]