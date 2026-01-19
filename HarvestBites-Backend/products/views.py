from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Product

@api_view(['GET'])
def product_list(request):
    products = Product.objects.all()
    data = [{
        'id': p.id,
        'name': p.name,
        'price': float(p.price),
        'image': p.image or '',
        'stock': p.stock,
        'description': p.description or ''
    } for p in products]
    return Response(data)
