import json
from re import template
from django.shortcuts import redirect, render, get_object_or_404
from django.http import JsonResponse, HttpResponse
from .models import Product, Category, Purchase
from .forms import AddProductForm, EditProductForm, PurchaseProductForm, AddCategoryForm
from django.urls import reverse, reverse_lazy
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.contrib import messages
from django.db.models import Q


@login_required
def product_list_view(request):
    if 'term' in request.GET:
        print('some jquery get request was made')
        qs = Product.objects.filter(name__icontains=request.GET.get('term'))
        titles = list()
        for product in qs:
            titles.appen(product.name)
        
        return JsonResponse(titles, safe=False)
    products = Product.objects.filter(active=True)
    categories = Category.objects.prefetch_related('product')
    template_name = 'products/product_list.html'
    add_product_form = AddProductForm()
    add_category_form = AddCategoryForm()
    purchase_product_form = PurchaseProductForm()

    context = {
        'products': products,
        'categories': categories,
        'add_product_form': add_product_form,
        'purchase_form': purchase_product_form,
        'add_category_form': add_category_form,
        'page_name': 'Products',
        'section': 'products'
    }
    print(context['section'])

    return render(request, template_name, context)

@login_required
def category_list_view(request):
    category_list = Category.objects.all()
    template_name = 'products/category_list.html'
    context = {
        'section': 'products',
        'categories': category_list,
    }

    if 'term' in request.GET:
        qs = Category.objects.filter(category_name__icontains=request.GET.get('term'))
        titles = list()
        for category in qs:
            titles.append(category.category_name)
        print(titles)
        return JsonResponse(titles, safe=False)

    return render(request, template_name, context)


@login_required
def add_category_view(request):
    user = request.user
    if request.method == 'POST':
        form = AddCategoryForm(request.POST)
        data = {}
        if form.is_valid():
            name = request.POST.get('category_name')
            category = Category.objects.create(category_name=name)
            # category.save()
            data['name'] = name
            res = {'data': data}
            print(name)
            return JsonResponse(res, safe=False)
        else:
            print(form.errors)    
           
    else:
        form = AddCategoryForm()
        print('something is not right')

    # return render(request, 'products/add_category.html', {'form': form})


@login_required
def product_add_view(request):
    if request.method == 'POST':
        form = AddProductForm(request.POST)
        data = {}
        if form.is_valid():
            response = request.POST
            print(response)
            user = request.user
            category = response.get('category')
            category_item = get_object_or_404(Category, id=category)
            name = response.get('name')
            image = response.get('image')
            price = response.get('price')
            quantity = response.get('quantity')
            reorder_quantity = response.get("reorderLevel")
            # Check if product with same already exist in the database
            try:
                normalized_product_name = name.lower()
                normalized_category_name = category_item.category_name.lower()
                product_check = Product.objects.get(Q(name__iexact=normalized_product_name) & Q(category__category_name__iexact=normalized_category_name))
                if product_check:
                    print('this product is available')
                    return JsonResponse({'error': "product in database already"})
            except Product.DoesNotExist:
                
                product = Product.objects.create(user=user, category=category_item, name=name, image=image, price=price, quantity=quantity, reorder_quantity=reorder_quantity)
                product.save()

                purchase = Purchase.objects.create(user=request.user, product=product, purchase_quantity=quantity,purchase_created=timezone.now())
                purchase.save()
                

                data['user'] = user.username
                data['name'] = name
                data['category'] = category_item.category_name
                data['image'] = image
                data['price'] = price
                data['quantity'] = quantity
                data['reorder_quantity'] = reorder_quantity
                messages.success(request, 'Product was saved successfully')
                
                return JsonResponse(data, safe=False)
    else:
        form = AddProductForm()

    template_name = 'products/add_product.html'
    context = {
        'form': form,
        'section': 'add_product'
    }

    return render(request, template_name, context)


@login_required
def product_detail_view(request, product_id, product_slug):
    product = get_object_or_404(Product, id=product_id, slug=product_slug)
    
    template_name = 'products/product_detail.html'
    context = {
        'product': product
    }
    return render(request, template_name, context)



@login_required
def product_edit_view(request, product_slug):
    product = get_object_or_404(Product, slug=product_slug)
    if request.method == 'POST':
        form = EditProductForm(instance=product, data=request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            form.save()
            return redirect('products:product_list')
    else:
        form = EditProductForm(instance=product)
    
    template_name = 'products/edit_product.html'
    context = {
        'form': form,
        'product': product,
        'section': 'products'
    }

    return render(request, template_name, context)


def product_delete_view(request, product_slug):
    product = get_object_or_404(Product, slug=product_slug)
    if request.method == 'POST':
        product.delete()
        print(f"got the request to delete product with slug: {product_slug}")
        return redirect('products:product_list')
    else:
        template_name = 'products/delete_product.html'
        return render(request, template_name)


def purchase_product_list(request):
    user = request.user
    purchase_history = Purchase.objects.all()
    weekly_purchases = []
    for purchase in purchase_history:
        if purchase.was_created_this_week():
            weekly_purchases.append(purchase)
    
    monthly_purchases = []
    for purchase in purchase_history:
        if purchase.was_created_this_month():
            monthly_purchases.append(purchase)
            
    yes_purchases = []
    for purchase in purchase_history:
        if purchase.was_created_yesterday():
            yes_purchases.append(purchase)

    template_name = 'products/purchase.html'
    context = {
        'user': user,
        'purchase_form': PurchaseProductForm(),
        'weekly_purchase': weekly_purchases,
        'monthly_purchase': monthly_purchases,
        'purchase_history': purchase_history,
        'title': 'Purchase History',
        'page_name': 'Purchases',
        'section': 'purchases',
        'yes_purchases': yes_purchases,
    }

    return render(request, template_name, context)



def purchase_product(request):
    user = request.user
    if request.method == 'POST':
        form = PurchaseProductForm(request.POST)
        data = {}
        if form.is_valid():
            response = request.POST
            product_id = response.get('product')
            product = Product.objects.get(id=product_id)
            purchase_quantity = response.get('purchase_quantity')
            print(response)
            if response.get('purchase_created') == '':
                purchase_created_date = timezone.now()
            else:
                purchase_created_date = response.get('purchase_created')
            product.quantity += int(purchase_quantity)
            product.save()
            purchase = Purchase.objects.create(user=user, product=product, purchase_quantity=int(purchase_quantity), purchase_created=purchase_created_date)
            purchase.save()
            print('product was saved')
            # send back json data
            data['product_name'] = product.name
            data['purchase_quantity'] = purchase_quantity
            sent_data = {'data': data}
            return JsonResponse(sent_data, safe=False)
        else:
            error_data = {}
            error_data['error'] = form.errors
            return JsonResponse(error_data, safe=False)
    else: 
        form = PurchaseProductForm()

    template_name = 'products/purchase.html'
    context = {
        'form': form,
        'section': 'purchases'
    }
    return render(request, template_name, context)

