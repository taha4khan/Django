# myproject/urls.py

from django.contrib import admin
from django.urls import path, include
from events.views import home  # Import the home view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),  # Route for the root URL
    path('api/', include('events.urls')),  # Assuming your API URLs are defined here
]
