from email.policy import default
from tabnanny import verbose
from django.db import models

# Create your models here.
class Category(models.Model):
    title = models.CharField(max_length=200)

    class Meta:
        verbose_name_plural = 'Categories'      #TO CHANGE THE PLURAL FORMAT IN OUR DB

    def __str__(self):
        return self.title



class Book(models.Model):
    title = models.CharField(max_length=250)
    author = models.CharField(max_length = 40, default ="Mike")
    isbn = models.CharField(max_length=14)
    category =models.ForeignKey(Category, related_name="books", on_delete =models.CASCADE)
    quantity = models.IntegerField()
    price = models.IntegerField()
    description = models.TextField()
    img_url = models.URLField()
    status = models.BooleanField(default=True)
    created_on = models.DateField(auto_now_add = True)

    def __str__(self):
        return self.title

    class Meta:                     #MODE OF ARRANGEMENT(OLDEST TO NEWEST)
        ordering = ['-created_on']    



class Product(models.Model):
    product_tag = models.CharField(max_length = 15)
    name = models.CharField(max_length = 100)
    category = models.ForeignKey(Category, related_name="products", on_delete =models.CASCADE)
    price = models.IntegerField()
    description = models.TextField()
    quantity =models.IntegerField()
    created_on = models.DateField(auto_now_add = True)
    img_url = models.URLField()
    status = models.BooleanField(default=True)

    def __str__(self):
        return '{} {}'.format(self.product_tag, self.name)  #TO IDENTIFY PRODUCT OBJECT BY THE TAG AND NAME AT ONCE

    class Meta:
        ordering = ['-created_on']

