from rest_framework import viewsets
from .models import GroceryItem
from .serializers import GroceryItemSerializer

class GroceryItemViewSet(viewsets.ModelViewSet):
    """
    A viewset that provides CRUD operations for GroceryItem
    """
    queryset = GroceryItem.objects.all().order_by('-created_at')  # Get all items, newest first
    serializer_class = GroceryItemSerializer