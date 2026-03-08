from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from django.shortcuts import get_object_or_404
from .models import GroceryItem
from .serializers import GroceryItemSerializer

class GroceryItemViewSet(viewsets.ModelViewSet):
    """
    A viewset that provides CRUD operations for GroceryItem
    """
    queryset = GroceryItem.objects.all().order_by('-created_at')
    serializer_class = GroceryItemSerializer

    # Override create method for custom response
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            self.perform_create(serializer)
            return Response({
                'message': 'Grocery item created successfully',
                'data': serializer.data
            }, status=status.HTTP_201_CREATED)
        return Response({
            'message': 'Failed to create grocery item',
            'errors': serializer.errors
        }, status=status.HTTP_400_BAD_REQUEST)

    # Override update method for custom response
    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        
        if serializer.is_valid():
            self.perform_update(serializer)
            return Response({
                'message': 'Grocery item updated successfully',
                'data': serializer.data
            })
        return Response({
            'message': 'Failed to update grocery item',
            'errors': serializer.errors
        }, status=status.HTTP_400_BAD_REQUEST)

    # Override destroy method for custom response
    def destroy(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
            self.perform_destroy(instance)
            return Response({
                'message': 'Grocery item deleted successfully'
            }, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({
                'message': 'Failed to delete grocery item',
                'error': str(e)
            }, status=status.HTTP_400_BAD_REQUEST)

    # Custom action to mark multiple items as purchased
    @action(detail=False, methods=['post'])
    def mark_purchased(self, request):
        """
        Custom endpoint to mark multiple items as purchased
        POST /api/items/mark_purchased/ with {"ids": [1,2,3]}
        """
        item_ids = request.data.get('ids', [])
        if not item_ids:
            return Response({
                'message': 'No item IDs provided'
            }, status=status.HTTP_400_BAD_REQUEST)
        
        updated = GroceryItem.objects.filter(id__in=item_ids).update(purchased=True)
        return Response({
            'message': f'{updated} items marked as purchased'
        })

    # Custom action to get statistics
    @action(detail=False, methods=['get'])
    def stats(self, request):
        """
        Get grocery list statistics
        GET /api/items/stats/
        """
        total = GroceryItem.objects.count()
        purchased = GroceryItem.objects.filter(purchased=True).count()
        pending = total - purchased
        
        return Response({
            'total_items': total,
            'purchased_items': purchased,
            'pending_items': pending
        })