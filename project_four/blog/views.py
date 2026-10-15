from django.shortcuts import render

# Create your views here.
def post_list(reguest):
    return render(request,'blog/post_list.html')