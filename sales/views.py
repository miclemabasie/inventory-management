from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from .models import Position, Sale, DailySale, CSV
from .forms import AddPositionForm, SaleConfirmForm
from django.utils import timezone
from products.models import Product
from django.http import JsonResponse
from django.urls import reverse
import json

def sales(request):
    sales = Sale.objects.all()

    template_name = 'sales/all_sales.html'

    context = {
        'sales': sales,
        'user': request.user,
        'section': 'sales',
        'page_name': 'Sales'
    }

    return render(request, template_name, context)


def sales_point(request):
    
    user = request.user
    set_sale_form = SaleConfirmForm()
    if request.method == 'POST':
        form = AddPositionForm(request.POST)
        if form.is_valid():
            data = {}
            error_response = {}
            post_data = request.POST
            product_id = post_data.get('product')
            product_id = int(product_id)
            product = Product.objects.get(id=product_id)
            product_name = product.name
            product_quantity = post_data.get('quantity')
            price = post_data.get('price')
            created = post_data.get('created')
            print('###################',created)
            if created == '':
                created = timezone.now()
            print(created)
            data['product'] = product_name
            data['quantity'] = product_quantity
            data['price'] = price
            data['created'] = created
            
            if product.quantity >= int(product_quantity):
                position = Position.objects.create(product=product, quantity=product_quantity, price=price, created=created)
                position.save()
                print(position.position_id)
                data['position_id'] = position.position_id
                return JsonResponse(data, safe=False)
            else:
                errors = {}
                errors['product_quantity_error'] = 'Not enough products to perform this transaction'
            
                error_response['error'] = errors
                return JsonResponse(error_response, safe=False)

        else:
            print(form.errors)
    else:
        form = AddPositionForm()
     
    
    template_name = 'sales/sales_point.html'
    context = {
        'sales_form': form,
        'page_name': 'Add Sale',
        'section': 'sales',
        'form_set_sale': 'set_sale_form'
    }
    return render(request, template_name, context)


def set_sale(request):

    if request.method == 'POST':
        print(request.POST)
        reqData = request.POST
        ids = reqData.get('IDs')
     
        js = json.loads(ids)
       
        # get all positions with ids
        positions_list = []
        for i in js:
            position = Position.objects.get(position_id=i)
            positions_list.append(position)
        print(positions_list)

        sale = Sale.objects.create(sales_man=request.user)
        for pos in positions_list:
            sale.positions.add(pos)
        sale.save
        print(sale.transaction_id)
        position.product.quantity -= position.quantity
        position.product.save()
        return redirect('sales:sales_point')     
    
    template_name = 'sales/set_sale.html'
    return render(request, template_name, {})