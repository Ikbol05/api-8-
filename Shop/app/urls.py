from django.urls import path
from . views import CategoryCreateView, CategoryDetailView, ProductCreateView, ProductDetailView, login

urlpatterns = [
    path('api/category/list/', CategoryCreateView.as_view()),
    path('api/category/detail/<int:pk>', CategoryDetailView.as_view()),
    path('api/product/list/', ProductCreateView.as_view()),
    path('api/product/detail/<int:pk>', ProductDetailView.as_view()),
    path('api/login/', login)
]