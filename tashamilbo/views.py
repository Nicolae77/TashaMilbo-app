from django.shortcuts import render
from store.models import Product, ReviewRating

def home(request):
    products = Product.objects.all().filter(is_available=True).order_by('created_date')
    
    reviews = ReviewRating.objects.none()

    for product in products:
        reviews = ReviewRating.objects.filter(product_id=product.id, status=True)
       

    context = {
        'products': products,
        'reviews': reviews,
    }
    return render (request, 'home.html', context)


def about(request):
    return render(request, 'about.html')
