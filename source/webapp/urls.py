from django.urls import path
from .views import IndexView, ProductView, ProductCreateView, ProductUpdateView, ProductDeleteView, ReviewCreateView

app_name = 'webapp'

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('products/<int:pk>/', ProductView.as_view(), name='product_detail'),
    path('products/create/', ProductCreateView.as_view(), name='product_create'),
    path('products/<int:pk>/edit/', ProductUpdateView.as_view(), name='product_update'),
    path('products/<int:pk>/delete/', ProductDeleteView.as_view(), name='delete'),
    path('products/<int:pk>/create/review', ReviewCreateView.as_view(), name='review_create'),

]
