from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('authtokens.urls'), name='auth-tokens'),
    path('api/', include('products.urls'), name='products'),
    path('users/', include('user.urls'), name='users'),
]
