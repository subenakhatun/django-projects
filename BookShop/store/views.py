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
        serializer = CategorySeiralizers(categories,many=True) # ak sathe onek gula
        return Response(serializer.data, status=status.HTTP_200_OK) # status=status.HTTP_200_OK. na dile o hoy just bujar jonno deya j asole ki hocche
    
    # Create Category
    def post(self,request):
        serializer = CategorySeiralizers(data=request.data) # ১. asha data serializer kore dey
        if serializer.is_valid(): # validation check korbe
            serializer.save() # tik thakhle database a patanu 
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) # na hole errors show korbe

# single single sob category sekahr jonno details a .

class CategoryDetailsAPIView(APIView):
    # category er list 1,2,3,4--- ak ak kore niye ashar jonno method create
    def get_object(self,pk): # request use kora jabe na, kaorn amra unique akta akta kore value chacchi
        return get_object_or_404(Category, pk=pk)

    # read ak ak kore sob category
    def get(self,request,pk):
        category = self.get_object(pk)
        serializer = CategorySeiralizers(category)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    # update korbo specifi ak ak kore category k 
    def put(self,request,pk):
        category = self.get_object(pk)
        serializer = CategorySeiralizers(category, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    # Delete korbo specifi ak ak kore category k 
    def delete(self, request, pk):
        category = self.get_object(pk)
        # delete kore dibo so validation er dorkar ei nai
        category.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    


'''
    # এখানে:
    # request -> HTTP Request অবজেক্ট
    # args    -> ()   (খালি tuple, কারণ পজিশনাল কিছু আসেনি)
    # kwargs  -> {'pk': 2}  (URL থেকে আসা pk=2)

'''

# Author API. applying Genric and Mixins: GenericAPIView + Mixins
from rest_framework import generics,mixins
from .models import Author
from .serializers import AuthorSerializers

# list 
class AuthorListCreateAPIView(mixins.ListModelMixin,mixins.CreateModelMixin,generics.GenericAPIView):
    # Author er data niye asha lagbe
    queryset = Author.objects.all()
    # seralizations class use korte hobe
    serializer_class = AuthorSerializers
    # get
    def get(self,request,*args,**kwargs):
        return self.list(request,*args,**kwargs)
    # post data 
    def post(self,request,*args,**kwargs):
        return self.create(request,*args,**kwargs)


    # Author Detials
class AuthorDetailAPIView(mixins.RetrieveModelMixin,mixins.UpdateModelMixin,mixins.DestroyModelMixin,generics.GenericAPIView,):
    # Author er data niye asha lagbe
    queryset = Author.objects.all()
    # seralizations class use korte hobe
    serializer_class = AuthorSerializers

    # retirive
    def get(self,request,*args,**kwargs):
        return self.retrieve(request,*args,**kwargs)

    # update
    def put(self,request,*args,**kwargs):
        return self.update(request,*args,**kwargs)

    # partial update
    def patch(self,request,*args,**kwargs):
        return self.partial_update(request,*args,**kwargs)

    # Delete or destroy
    def delete(self,request,*args,**kwargs):
        return self.destroy(request,*args,**kwargs)


    # Book API using Concrete Generic Views
from .models import Book
from .serializers import BookSerializers

# read and create
class BookListCreateAPIView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializers

# retirve,update,delete
class BookDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializers


# Book niyei kaj korbo tobe modelviewset use kore ar custom action use kore
from rest_framework import viewsets
from rest_framework.decorators import action


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializers

    @action(detail=False, methods=['get'])

    # total book ar sesh hoye jawa book er number dkeahnur jonno condition set kore deya
    def summary(self, request):
        books = self.get_queryset()
        total_books = books.count()
        out_of_stock = books.filter(stock__lte=0).count()

        return Response(
            {
                'total_books': total_books,
                'out_of_stock_books': out_of_stock,
            },
            status=status.HTTP_200_OK,
        )
