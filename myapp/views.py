from django.http import JsonResponse
from .models import Product
from django.shortcuts import render

def product_list(request):
    products = Product.objects.all()
    data = [{'name': product.name, 'description': product.description, 'price': str(product.price)} for product in products]
    return JsonResponse(data, safe=False)


def product_list_page(request):
    return render(request, 'myapp/product_list.html')
