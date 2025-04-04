from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.response import Response
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
# class ItemListCreateView(generics.ListCreateAPIView):
#     queryset = Item.objects.all()
#     serializer_class = ItemSerializer

#     def create(self, request, *args, **kwargs):
#         response = super().create(request, *args, **kwargs)
#         return Response({
#             'message': 'Item created successfully',
#             'data': response.data
#         }, status=status.HTTP_201_CREATED)

class ItemListView(generics.ListAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

    def list(self, request, *args, **kwargs):
        response = super().list(request, *args, **kwargs)
        return Response({
            'message': 'Items retrieved successfully',
            'data': response.data
        }, status=status.HTTP_200_OK)

# Create a new item
class ItemCreateView(generics.CreateAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        return Response({
            'message': 'Item created successfully',
            'data': response.data
        }, status=status.HTTP_201_CREATED)

class GetUserView(generics.RetrieveAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

    def retrieve(self, request, *args, **kwargs):
        response = super().retrieve(request, *args, **kwargs)
        return Response({
            'message': 'Item retrieved successfully',
            'data': response.data
        }, status=status.HTTP_200_OK)

class UpdateUserView(generics.UpdateAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

    def update(self, request, *args, **kwargs):
        response = super().update(request, *args, **kwargs)
        return Response({
            'message': 'Item updated successfully',
            'data': response.data
        }, status=status.HTTP_200_OK)

class DeleteUserView(generics.DestroyAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

    def destroy(self, request, *args, **kwargs):
        super().destroy(request, *args, **kwargs)
        return Response({
            'message': 'Item deleted successfully'
        }, status=status.HTTP_204_NO_CONTENT)


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
