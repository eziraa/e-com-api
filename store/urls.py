from django.urls import path, include
from . import views

urlpatterns = [
    path("products/", views.ProductList),
    path("products/<int:id>/", views.ProductDetail)
]
