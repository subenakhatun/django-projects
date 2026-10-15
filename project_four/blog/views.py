from django.shortcuts import render
from datetime import datetime

# Create your views here.
def postt(request):
    a = 1000
    return render(request,'blog/post_list.html',{'a': a})

class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age

def home(request):
    context = {
        "name":"Subena khatun",
        "content":" write anything you want to write in this content. This is a practice project of Django.",
        "age": 32,
        "price":200,
        "skills":["Python","Django","Fest API","Javasciript","React","Machine laerning","Deep learning","Computer Vision"],
        "user":User("Unknown",33),
        "blog":{
            "title": "Django Practices Project",
            "content":"<b>this is bold </b>:",
            "created_at":datetime(2026,10,15,6,23)
        },
        "empty_value": None,
    }

    return render(request,'blog/post_list.html',context)

