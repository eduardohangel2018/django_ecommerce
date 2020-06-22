from django.contrib import admin
from django.urls import path
# Importa do arquivo .views a home_page
from .views import home_page
urlpatterns = [
        path('', home_page),
        path('about/', about_page),
        path('contact/', contact_page),
        path('admin/', admin.site.urls),
]
