from django import forms
from django.forms import fields
from .models import Product, Purchase, Category
import logging

logging.basicConfig(level=logging.DEBUG)

logger = logging.getLogger(__name__)
# logger.setLevel(logging.DEBUG)

class AddProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['category', 'name', 'image', 'price', 'quantity', 'reorder_quantity']

    # logger.info('Cleaning form fields')
    # def clean_name(self):
    #     name = self.cleaned_data['name']
    #     category = self.cleaned_data['category']
    #     # check the database for product with same name and category
    #     try:
    #         logger.info('Checking if product with this name already exists.')
    #         qs = Product.objects.filter(name=name, category=category).first()
    #     except:
    #         pass
    #     if qs is not None:
    #         logger.warning('Failed to resolve product name, this product already exists in the database')
    #         raise forms.ValidationError('This product with name and category already exists')
    #     else:
    #         logger.info('Product name resolved successfully')
    #         return name
        
class EditProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['category', 'name', 'price', 'reorder_quantity', ]


class AddCategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['category_name']

    logger.info('Cleaning category fields')
    def clean_name(self):
        name = self.cleaned_data.get('category_name')
        # check if category already exist
        try:
            logger.info('Checking category existends in the database')
            qs = Category.objects.filter(category_name=name).first()
        except:
            pass
        if qs is not None:
            logger.error("Category already exists in the database")
            raise forms.ValidationError('This category already exists!')
        else:
            logger.info("Category name check passed.")
            return name

class PurchaseProductForm(forms.ModelForm):
    class Meta:
        model = Purchase
        fields = ['product', 'purchase_quantity', 'purchase_created']


    def clean_purchase_quantity(self):
        purchase_quantity = self.cleaned_data.get('purchase_quantity')
        if purchase_quantity < 1:
            raise forms.ValidationError('quantity can not be less that 1')
        return purchase_quantity