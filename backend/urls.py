from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse

def welcome_view(request):
    return HttpResponse("<h1>Welcome to the Room Reservation API</h1><p>Visit <a href='/api/'>API</a></p>")

urlpatterns = [
    path('', welcome_view),  # Home page
    path('admin/', admin.site.urls),
    path('api/', include('rooms.urls')),
]
