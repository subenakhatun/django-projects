from django.shortcuts import render

def home(request):
    user_name = "Subena Khatun"  # এটি ব্যাকএন্ড বা ডাটাবেসের ডেটা
    
    # render ৩টি জিনিসকে এক জায়গায় মেলায়
    return render(request, 'home.html', {'name': user_name})