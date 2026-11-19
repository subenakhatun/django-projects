from rest_framework import serializers
from .models import Category,Author,Book,AuthorProfile

# Category Serializers
class CategorySeiralizers(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__' 

# Author Profile Serializers
class AuthorProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = AuthorProfile
        fields = '__all__'

# Author Srializers
class AuthorSerializers(serializers.ModelSerializer):
    profile = AuthorProfileSerializer(read_only=True)
    class Meta:
        model = Author
        fields = '__all__'






# Book Serializers
class BookSerializers(serializers.ModelSerializer):
    category = serializers.PrimaryKeyRelatedField(
        queryset=Category.objects.all()
    )

    authors = serializers.PrimaryKeyRelatedField(
        many=True,
        queryset=Author.objects.all()
    )
    

    class Meta:
        model = Book
        fields = '__all__'
