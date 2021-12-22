from django.urls import path
from .views import (
    product_list_view,
    product_edit_view,
    product_add_view,
    product_delete_view,
    purchase_product,
    purchase_product_list,
    product_detail_view,
    category_list_view,
    add_category_view
)


app_name = 'products'


urlpatterns = [
    path('list', product_list_view, name='product_list'),
    path('product-add/', product_add_view, name='product_add'),
    path('product-edit/<slug:product_slug>/', product_edit_view, name='product_edit'),
    path('delete-product/<slug:product_slug>/', product_delete_view, name='delete_product'),
    path('purchase-product/', purchase_product, name='product_purchase'),
    path('purchase-history/', purchase_product_list, name='purchase_list'),
    path('product-detail/<int:product_id>/<slug:product_slug>/', product_detail_view, name='product_detail'),
    path('category-list/', category_list_view, name='category_list'),
    path('add-category/', add_category_view, name='add_category')
]

