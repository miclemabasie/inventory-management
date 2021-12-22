from django import http
import os
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Customer
from .forms import CustomerCreateForm
from django.contrib.auth.decorators import login_required
from PIL import Image
from django.conf import settings
from django.core.files.storage import FileSystemStorage






def customer_list_view(request):
    customers = Customer.objects.all()
    customers_owing = Customer.objects.filter(is_owing=True)
    template_name = 'customers/customer-list.html'
    form = CustomerCreateForm()
    context = {
        'customers': customers,
        'customers_owing': customers_owing,
        'customer_add_form': form,
    }

    return render(request, template_name, context)



@login_required
def add_customer_view(request):
    PATH = f"{settings.BASE_DIR}/media/"
    if request.method == 'POST':
        form = CustomerCreateForm(data=request.POST,files=request.FILES )
        if form.is_valid():
            data = {}
            print('#####################################')
            req = request.POST
            name = req.get('name')
            phone = req.get('phone')
            photo = request.FILES.get('photo')
            about = req.get('about')
            print(request.FILES)
          
            file_storage_system = FileSystemStorage()
            print(file_storage_system)
            filename = file_storage_system.save(photo.name, photo)
            file_url = file_storage_system.url(filename)
            save_url = file_url.split('/')[-1]
            Customer.objects.create(name=name, photo=save_url, phone=phone,about=about)
            data['name'] = name,
            data['about'] = about,
            

            response = {'data': data}
            return JsonResponse(response, safe=False)
        else:
            print(form.errors)

    else:
        form = CustomerCreateForm()

    template_name = 'customers/add_customer.html'
    context = {
        'form': form,

    }
    return render(request, template_name, context)
