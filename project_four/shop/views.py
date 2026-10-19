from django.shortcuts import render
from datetime import datetime



# Create your views here.
def products(request):
    spost = [
        {"title":"Dhango Basics","is_featured":True, "author":"Mohit Kumar"},
        {"title":"Django Advanced","is_featured":False, "author":""},
        {"title":"Django REST Framework","is_featured":False, "author":"Anu Choudhary"},
    ]

    context = {
        "shops": 'ok',
        "today": datetime.now(),
        "html_code":"<b>Welcome to My Blog</b>"

    }

    return render(request,'shop/product_list.html', context)