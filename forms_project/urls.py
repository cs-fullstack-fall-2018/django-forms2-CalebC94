from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('', include('forms_app.urls')),
    path('create/', ''),
    path('admin/', admin.site.urls),
]