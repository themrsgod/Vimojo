import os
import random
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "app.settings")
django.setup()

from app.models import Product

def seed_products(count):
    for _ in range(count):
        name = f'Product {random.randint(1, 100)}'
        price = round(random.uniform(10, 1000), 2)
        description = f'This is a description for {name}'
        image_path = './images/image-4.jpg'  # Replace with actual image path
        Product.objects.create(name=name, price=price, description=description, image=image_path)


if __name__ == '__main__':
    product_count = 20  # Number of products to create
    seed_products(product_count)
    print(f'Successfully seeded {product_count} products')
