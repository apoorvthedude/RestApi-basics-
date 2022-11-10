from django.contrib import admin
from django.urls import path,include
from .views import ItemsView,ItemView

urlpatterns = [
path('items/',ItemsView,name = "ItemsView"),
path('item/<int:id>/',ItemView,name = "ItemView"),
]
