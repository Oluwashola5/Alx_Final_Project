from django.shortcuts import render
from rest_framework import generics
from .models import Item
from .serializers import ItemSerializer
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from django.views import View
import json
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
# from .views import CreateItemView


# Create and List Items
class ItemListCreateView(generics.ListCreateAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

# Retrieve, Update, and Delete a Single Item
class ItemRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    # permission_classes = [IsAuthenticated] 
# oik-

# Create Item
class CreateItemView(View):
    def post(self, request):
        data = json.loads(request.body)
        item = Item.objects.create(
            name=data.get('name'),
            description=data.get('description'),
            price=data.get('price')
        )
        return JsonResponse({'id': item.id, 'message': 'Item created successfully'})

# Retrieve Item
class RetrieveItemView(View):
    def get(self, request, item_id):
        item = get_object_or_404(Item, id=item_id)
        return JsonResponse({
            'id': item.id,
            'name': item.name,
            'description': item.description,
            'price': str(item.price),
            'created_at': item.created_at.strftime('%Y-%m-%d %H:%M:%S'),
            'updated_at': item.updated_at.strftime('%Y-%m-%d %H:%M:%S')
        })

# Update Item
class UpdateItemView(View):
    def put(self, request, item_id):
        item = get_object_or_404(Item, id=item_id)
        data = json.loads(request.body)
        item.name = data.get('name', item.name)
        item.description = data.get('description', item.description)
        item.price = data.get('price', item.price)
        item.save()
        return JsonResponse({'message': 'Item updated successfully'})

# Delete Item
class DeleteItemView(View):
    def delete(self, request, item_id):
        item = get_object_or_404(Item, id=item_id)
        item.delete()
        return JsonResponse({'message': 'Item deleted successfully'})

def index(request):
    return HttpResponse("Welcome to the homepage!")

# Create your views here.
