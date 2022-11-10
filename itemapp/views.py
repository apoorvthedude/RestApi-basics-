from django.shortcuts import render,HttpResponseRedirect,Http404
from .serializers import ItemSerializer
from .models import ItemModel
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse,JsonResponse
from rest_framework.parsers import JSONParser

# Create your views here.

# Function to Get/POST All Items
@csrf_exempt
def ItemsView(request):
	if request.method == "GET":
		items = ItemModel.objects.all()
		serializer = ItemSerializer(items,many = True)
		return JsonResponse(serializer.data,safe=False)

	elif request.method == "POST":
		data = JSONParser().parse(request)
		serializer = ItemSerializer(data = data)
	
		if serializer.is_valid():
			serializer.save()
			return JsonResponse(serializer.data,status = 201)
		return JsonResponse(serializer.errors,status=400)

# function to add specific Item
@csrf_exempt
def ItemView(request,id):
	try:
		item = ItemModel.objects.get(id=id)
	except ItemModel.DoesNotExist:
		raise Http404('Not Found')
	
	if request.method == 'GET':
		serializer = ItemSerializer(item)
		return JsonResponse(serializer.data)

	if request.method == "PUT":
		data = JSONParser().parse(request)
		serializer = ItemSerializer(item,data = data)

		if serializer.is_valid():
			serializer.save()
			return JsonResponse(serializer.data,status = 201)
		return JsonResponse(serializer.errors,status=400)

	if request.method == "DELETE":
		item.delete()
		return HttpResponse(status=204)
