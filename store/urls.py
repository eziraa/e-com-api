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
         name='collection-detail'),
    path("categories/", views.CategoryListView.as_view(), name="get-categories"),
    path("categories/<int:id>/", views.CategoryDetailView.as_view(),
         name='category-detail'),
    path("promotions/", views.PromotionListView.as_view(), name="get-promotions"),
    path("promotions/<int:id>/", views.PromotionDetailView.as_view(),
         name='promotion-detail'),
    path("customers/", views.CustomerListView.as_view(), name="get-customers"),
    path("customers/<int:id>/", views.CustomerDetailView.as_view(),
         name='promotion-detail'),
    path("orders/", views.OrderListView.as_view(), name="get-orders"),
    path("orders/<int:id>/", views.OrderDetailView.as_view(),
         name='order-detail'),
    path("orderItems/", views.OrderItemListView.as_view(), name="get-orderItems"),
    path("orderItems/<int:id>/", views.OrderItemDetailView.as_view(),
         name='order-item-detail'),

]
