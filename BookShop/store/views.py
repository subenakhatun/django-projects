# For HTML page rendaring
from django.shortcuts import render

# Error Handlaing 
from django.shortcuts import get_object_or_404
# Status pass 
from rest_framework import status
# return response
from rest_framework.response import Response
# APIView create
from rest_framework.views import APIView
# Which Model
from .models import Category
# Which Serializer
from .serializers import CategorySeiralizers

# Create your views here.

# CategorySeiralizers View function Create

class CategoryListCreateAPIVIew(APIView):
    # Read Category
    def get(self,request):
        categories = Category.objects.all()
        # convert Jeson File , call serializers
        serializer = CategorySeiralizers(categories,many=True) # ak sateh onek gula
        return Response(serializer.data, status=status.HTTP_200_OK)
