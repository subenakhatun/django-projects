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
        categories = Category.objects.all() # sob data show korar jonno
        # convert Jeson File , call serializers
        serializer = CategorySeiralizers(categories,many=True) # ak sateh onek gula
        return Response(serializer.data, status=status.HTTP_200_OK) # status=status.HTTP_200_OK. na dile o hoy just bujar jonno deya j asole ki hocche
    
    # Create Category
    def post(self,request):
        serializer = CategorySeiralizers(data=request.data) # ১. asha data serializer kore dey
        if serializer.is_valid(): # validation check korbe
            serializer.save() # tik thakhle database a patanu 
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) # na hole errors show korbe
