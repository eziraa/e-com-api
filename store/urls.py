from django.urls import path, include
from . import views
from . import models

urlpatterns = [
    path("products/", views.ProductListView.as_view(),
         name="get-products"),
    path("products/<int:id>/", views.ProductDetail().__class__.as_view(),
         name="product-detail"),
    path("collections/", views.CollectionListView.as_view(), name="get-collections"),
    path("collections/<int:id>/", views.CollectionDetailView.as_view(),
         name='collection-detail')
]
