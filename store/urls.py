from django.urls import path, include
from . import views

urlpatterns = [
    path("products/", views.ProductList.as_view(), name="get-products"),
    path("products/<int:id>/", views.ProductDetail.as_view(), name="product-detail"),
    path("collections/", views.CollectionListView.as_view(), name="get-collections"),
    path("collections/<int:id>/", views.CollectionDetailView.as_view(),
         name='collection-detail')
]
