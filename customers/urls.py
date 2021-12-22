from django.urls import path
from .views import (
    customer_list_view,
    add_customer_view,
)

app_name = 'customers'

urlpatterns = [
    path('customer-list/', customer_list_view, name='customers_list'),
    path('add-customer/', add_customer_view, name='add_customer')
]
