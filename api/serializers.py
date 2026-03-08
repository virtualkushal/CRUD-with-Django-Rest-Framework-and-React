from rest_framework import serializers
from .models import GroceryItem

class GroceryItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = GroceryItem
        fields = ['id', 'name', 'quantity', 'purchased', 'created_at']
        read_only_fields = ['id', 'created_at']  # These can't be modified via API

    # Custom validation for name field
    def validate_name(self, value):
        if not value or value.strip() == '':
            raise serializers.ValidationError("Item name cannot be empty")
        if len(value) < 2:
            raise serializers.ValidationError("Item name must be at least 2 characters long")
        if len(value) > 100:
            raise serializers.ValidationError("Item name cannot exceed 100 characters")
        return value.strip()

    # Custom validation for quantity field
    def validate_quantity(self, value):
        if not value or value.strip() == '':
            raise serializers.ValidationError("Quantity cannot be empty")
        return value.strip()

    
    def validate(self, data):
      
        if data.get('name') and data.get('quantity'):
            # You can add cross-field validation here if needed
            pass
        return data