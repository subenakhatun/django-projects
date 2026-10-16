from django.shortcuts import render
import datetime

from project_four import blog, shop

# Create your views here.
def product_list(request):
    spost = [
        {"title":"Dhango Basics","is_featured":True, "author":"Mohit Kumar"},
        {"title":"Django Advanced","is_featured":False, "author":""},
        {"title":"Django REST Framework","is_featured":False, "author":"Anu Choudhary"},
    ]

    context = {
        "shops": shop,
        "today": datetime.now(),
        "html_code":"<b>Welcome to My Blog</b>"

    }

    return render(request,'shop/product_list.html', context)