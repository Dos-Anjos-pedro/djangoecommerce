from django.urls import path, include
from django.contrib import admin
from django.conf import settings
from core import views
from catalog import views as views_catalog
from django.contrib.auth.views import LoginView, LogoutView
from accounts.views import RegisterView

urlpatterns = [
    path('', views.index, name='index'),
    path('contato/', views.contact, name='contact'),
    path('entrar/', LoginView.as_view(template_name='login.html'), name='login'),
    path('sair/', LogoutView.as_view(next_page='index'), name='logout'), 
    path('catalogo/', include(('catalog.urls', 'catalog'), namespace='catalog')),
    path('conta/', include(('accounts.urls', 'catalog'), namespace='accounts')),
    path('compras/', include(('checkout.urls', 'checkout'), namespace='checkout')),
    path('admin/', admin.site.urls),
]
