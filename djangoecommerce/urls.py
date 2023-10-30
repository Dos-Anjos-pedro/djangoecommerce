from django.urls import path, include
from django.contrib import admin

from core import views
from catalog import views as views_catalog

urlpatterns = [
    path('', views.index, name='index'),
    path('contato/', views.contact, name='contact'),
  
    path('catalogo/', include(('catalog.urls', 'catalog'), namespace='catalog')),
    path('admin/', admin.site.urls),
]
