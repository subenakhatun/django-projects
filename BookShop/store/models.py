from django.db import models

# Create your models here.
# Category Model Create
class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name

# Author Model
class Author(models.Model):
    name=models.CharField(max_length=100)
    country = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return self.name

# BOOK list Model
class Book(models.Model):
    title = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    stock= models.PositiveBigIntegerField(default=0)
    is_available = models.BooleanField(default=True)
    category = models.ForeignKey(Category,on_delete=models.CASCADE, related_name='books')
    author = models.ForeignKey(Author,on_delete=models.CASCADE, related_name='books')

    def __str__(self):
        return self.title
