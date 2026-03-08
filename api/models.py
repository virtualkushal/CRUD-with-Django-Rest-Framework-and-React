from django.db import models

class GroceryItem(models.Model):
    name = models.CharField(max_length=100)
    quantity = models.CharField(max_length=50)
    purchased = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name