from django.test import TestCase

from products.models import Category
from ..forms import AddProductForm, AddCategoryForm
from ..models import Category
from django.contrib.auth import get_user_model


User = get_user_model()


class TestForms(TestCase):

    def setUp(self):
        category = Category.objects.create(
            category_name='new cat'
        )
        category.save()
        self.category = category

        user_a = User.objects.create(
            username = 'miclem',
            email = 'miclem@mail.com'
        )
        user_a.save()
        self.user = user_a


        # create a product
      

    def test_cat_and_user_creation(self):
        count = Category.objects.all().count()
        self.assertEqual(count, 1)
        user_count = User.objects.all().count()
        self.assertEqual(user_count, 1)

    
    def test_add_product_form(self):
        form = AddProductForm({
            'user': self.user,
            'category': self.category,
            
        })

        form2 = AddProductForm({
            'name': 'miclem',
        
        })
        self.assertTrue(form.is_valid())
        self.assertFalse(form2.is_valid())
    

    

        