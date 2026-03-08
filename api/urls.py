from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import GroceryItemViewSet

# Create a router and register our viewset
router = DefaultRouter()
router.register(r'items', GroceryItemViewSet, basename='groceryitem')


urlpatterns = [
    path('', include(router.urls)),
]