from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', HomeViews.as_view(), name='home'),
    path('team_products/<pk>', TeamProductsListViews.as_view(), name='team_products'),
    path('product_details/<pk>/', ProductDetailVeiw.as_view(), name='product_detail'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)