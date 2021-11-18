from . models import *
from django.test import TestCase

'''
    Helps to test products
'''
class ProductTest(TestCase):
    @classmethod
    def test_create_product(cls):
        # create user
        test_user = User.objects.create(username='testuser',password='test123')
        test_user.save()

        #create product
        test_product = Product.objects.create(seller=test_user,name='product test 1',price='2000',
        description='a test product',is_sold=False)
        test_product.save()

    def test_product_content(self):
        product = Product.objects.get(id=1)
        seller = f'{product.seller}'
        name = f'{product.name}'
        price = f'{product.price}'
        description =f'{product.description}'
        self.assertEqual(seller, 'test_user')
        self.assertEqual(name, 'product test 1')
        self.assertEqual(price, '2000')
        self.assertEqual(description, 'a test product')
