from django.urls import path
from . views import DetailBook, DetailUser, ListBook, ListCategory, DetailCategory, ListProduct, DetailProduct, ListUser, DetailUser

urlpatterns = [
    path('categories', ListCategory.as_view(),name ='categories'),
    path('category/<int:pk>', DetailCategory.as_view(), name='detailcategory'),

    path('books', ListBook.as_view(), name='books'),
    path('books/<int:pk>', DetailBook.as_view(), name='detailbook'),
    
    path('products', ListProduct.as_view(),name='products'),
    path('products/<int:pk>', DetailProduct.as_view(), name='datailproducts'),

    path('user', ListUser.as_view(), name = 'user'),
    path('user/<int:pk>', DetailUser.as_view(), name='detailuser'),
]