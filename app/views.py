from django.shortcuts import get_object_or_404, render

from app.models import Product

def home(request):
    return render(request, 'home.html')

def product_details(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    context = {'product': product}
    return render(request, 'product_details.html', context)