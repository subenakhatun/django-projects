from django.shortcuts import render,redirect,get_object_or_404
# render: html file a send kora, redirect: ei url ei niye asha, get_object: j object ta kora hoise seta k call kore niye asha na hole error dkehabe
from django.urls import reverse # পাইথন লজিক বা ভিউ ফাইল থেকে নির্দিষ্ট কোনো ইউআরএল-এর সঠিক ঠিকানা বা পাথ বের করার জন্যই মূলত reverse ব্যবহার করা হয়।
# reverse: url e extact path
# Create your views here.

from .models import Task

# tasks er ak ak kore sob list ei jaygay hobe
# Task ক্লাসটিকে সরাসরি ডেটাবেজের টেবিলের রেকর্ডগুলোর সাথে কথা বলানোর বা ডেটা কুয়েরি করার কাজটি করে দেয় এই objects।
def task_list(request):
    tasks = Task.objects.all().order_by('created')
    return render(request,'todo/tasklist.html',{'tasks':task_list})

# create tasks
# def create_task(request):
def task_create(request):
    if request.method == 'POST':
        title = request.POST.get('title', '').strip()
        description = request.POST.get('description','').strip()
        if title:
            Task.objects.create(title=title,description=description)
            return redirect(reverse('todo:task_list'))
        error = 'Ttile can not be empty.'
        return render(request,'todo/task_form.html',{'error': error})
    return render(request, 'todo/task_form.html')


# update ba Edit function
def task_update(request, pk):
    task = get_object_or_404(Task, pk=pk)
    
    if request.method == 'POST':
        title = request.POST.get('title', '').strip()
        description = request.POST.get('description', '').strip()
        
        if title:
            task.title = title
            task.description = description
            task.save()
            return redirect(reverse('todo:task_list'))
            
        error = 'Title can not be empty.'
        return render(request, 'todo/task_form.html', {'task': task, 'error': error})
        
    return render(request, 'todo/task_form.html', {'task': task})

# task list update
'''
question: ami ki update korte chai?
answer: jokon browser a title description dibo seTa ami chaile edit korte parbo
er jonno amak ki kora lage?
1. def task_update(request,pk) nam a akta function create kora lagbe
2. oi function a first er task er akta logic set korte hobe already j task ase seta
task = Task.object(Task,pk)

3. er pore amak post method er jonno logic korte hobe
if request.method=='POSt':
    title = title
    descrption = descitpion
    if title and description already ase tokon save korbo
    er pore 
'''

def task_update(request, pk):
    # পুরনো টাস্কটি খুঁজে বের করা ( ২ নম্বর স্টেপ)
    task = get_object_or_404(Task, pk=pk)
    
    # POST মেথডের লজিক ( ৩ নম্বর স্টেপ)
    if request.method == 'POST':
        title = request.POST.get('title', '').strip()
        description = request.POST.get('description', '').strip()
        
        # যদি টাইটেল খালি না থাকে, তবে আপডেট করে সেভ করব
        if title:
            task.title = title
            task.description = description
            task.save()
            return redirect(reverse('todo:task_list'))
            
    return render(request, 'todo/task_form.html', {'task': task})

# task list delete
def task_delete(request, pk):
    task = get_object_or_404(Task, pk=pk)
    
    if request.method == 'POST':
        task.delete()
        return redirect(reverse('todo:task_list'))
        
    return render(request, 'todo/task_confirm_delete.html', {'task': task})

def task_complete(request, pk):
    task = get_object_or_404(Task, pk=pk)
    
    # স্ট্যাটাসটি উল্টে দেওয়া (কমপ্লিট থাকলে আন-কমপ্লিট, আর না থাকলে কমপ্লিট)
    task.completed = not task.completed
    task.save()
    
    return redirect(reverse('todo:task_list'))