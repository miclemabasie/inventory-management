from django.urls import path
from .views import (
    sales,
    sales_point,
    set_sale
)

app_name = 'salse'

urlpatterns = [
    path('', sales, name='sales'),
    path('sales-point/', sales_point, name='sales_point'),
    path('set-sale/', set_sale, name='set_sale')
]
