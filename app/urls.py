from django.contrib import admin
from django.urls import path, include
import genres

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('genres.urls'))
]
