from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='productHome'),
    path('detail/<int:p_id>', views.detailProduct, name='detailProduct'),
    path('deleteProduct/<int:p_id>', views.deleteProduct, name='deleteProduct'),
    path('createProduct', views.createProduct, name='createProduct')
]
