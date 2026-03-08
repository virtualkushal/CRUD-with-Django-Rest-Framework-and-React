from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),  # Optional: you can remove this line if you don't want admin
    path('api/', include('api.urls')),  # All API URLs will start with /api/
]