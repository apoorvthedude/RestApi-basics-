from rest_framework import serializers
from .models import ItemModel

class ItemSerializer(serializers.ModelSerializer):
	class Meta:
		model = ItemModel
		fields = ['name','price'] # "__all__"
