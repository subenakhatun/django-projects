from django.shortcuts import render,redirect,get_object_or_404
from django.urls import reverse # পাইথন লজিক বা ভিউ ফাইল থেকে নির্দিষ্ট কোনো ইউআরএল-এর সঠিক ঠিকানা বা পাথ বের করার জন্যই মূলত reverse ব্যবহার করা হয়।
# Create your views here.

from .models import Task

# tasks er ak ak kore sob list ei jaygay hobe
# Task ক্লাসটিকে সরাসরি ডেটাবেজের টেবিলের রেকর্ডগুলোর সাথে কথা বলানোর বা ডেটা কুয়েরি করার কাজটি করে দেয় এই objects।
def task_list(request):
    tasks = Task.Objects.all().order_by('_created')
    return render(request,'todo/tasklist.html',{'tasks':task_list})

# create tasks
def create_task(request):
    