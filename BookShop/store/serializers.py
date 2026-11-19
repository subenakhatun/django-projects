from rest_framework import serializers
from .models import Category,Author,Book

# Category Serializers
class CategorySeiralizers(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__' 

# Author Srializers
class AuthorSerializers(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'

# Book Serializers
class BookSerializers(serializers.ModelSerializer):
    category = serializers.PrimaryKeyRelatedField(
        queryset=Category.objects.all()
    )

    author = serializers.PrimaryKeyRelatedField(
        queryset=Author.objects.all()
    )

    class Meta:
        model = Book
        fields = '__all__'
