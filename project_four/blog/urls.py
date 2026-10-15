from django.urls import path
from . import views

urlpatterns=[
    path('',views.home,name='home'),
    path('postt/',views.postt,name='postt'), # every function of views must be add here.
]