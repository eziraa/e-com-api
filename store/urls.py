from django.urls import path, include
from . import views

urlpatterns = [
    path("products/", views.ProductList),
    path("products/<int:id>/", views.ProductDetail),
    path("collections/", views.CollectionList),
    path("collections/<int:id>/", views.CollectionDetail, name='collection-detail')
]
