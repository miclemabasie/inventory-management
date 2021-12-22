from django.test import TestCase
from django.urls import reverse
from accounts.models import CustomUser
from django.conf import settings
from decimal import Decimal
from products.models import Product, Category

class TestViewAndTemplates(TestCase):
    
    def setUp(self):
        user = CustomUser.objects.create(username='miclem', email='miclem@mail.com')
        password = 'Test123#'
        user.set_password(password)
        user.save()
        self.user = user
        self.password = password
        self.username = self.user.username

        # create categroy
        category = Category.objects.create(
            category_name='Printers',
        )
        category2 = Category.objects.create(
            category_name='Laptops',
        )
        self.category = category
        self.category2 = category2

        product = Product.objects.create(
            user=self.user,
            category=self.category,
            name='Test product',
            price=Decimal('2.00')
        )  
        product2 = Product.objects.create(
            user=self.user,
            category=self.category,
            name='Test product2',
            price=Decimal('2.00')
        )  
        product.save()
        product2.save()
        self.product = product
        self.product2 = product2

    def test_products_add_page_works(self):
        print('Testing the home page')
        login_url = settings.LOGIN_URL
        ty = self.client.login(username=self.user.username, password=self.password)
        print(ty)
        response = self.client.get(reverse('dashboard'))
        self.assertEqual(response.status_code, 200)

    def test_user_can_not_access_dashboad_without_login(self):
        print('Testing for possible unauthorize access to dashboard')
        response = self.client.get(reverse('dashboard'))
        self.assertEqual(response.status_code, 302)

    def test_product_lsit_view_works(self):
        print("Testing the product list view")
        response = self.client.get(reverse('products:product_list'))
        self.assertEqual(response.status_code, 302)
        self.client.login(username='miclem', password='Test123#')
        response_login = self.client.get(reverse('products:product_list'))
        self.assertEqual(response_login.status_code, 200)
        
        self.assertTemplateUsed(response_login, 'products/product_list.html')
        self.assertContains(response_login, 'Stock Grid')
        self.assertEqual(len(response_login.context['products']), 2)
        product_list = Product.objects.all()
        print(product_list)
        self.assertEqual(list(response_login.context['products']), list(product_list))


    def test_category_list_view_works(self):
        print("Test that category list view works")
        self.client.login(username='miclem', password='Test123#')
        response = self.client.get(reverse('products:category_list'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.context['categories']), 2)
        self.assertContains(response, 'Stock Grid')
        self.assertTemplateUsed(response, 'products/category_list.html')
        category_list = Category.objects.all()
        self.assertEqual(list(response.context['categories']), list(category_list))
    
    def test_add_category_view_works(self):
        Category.objects.create(
            category_name = 'cat'
        )
        self.client.login(username=self.username, password=self.password)
        response = self.client.post(reverse('products:add_category'), {'category_name':'newcate'})
        print(response)
        print(Category.objects.all())