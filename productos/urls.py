from django.urls import path
#from rolepermissions.decorators import has_role_decorator
#from rolepermissions.decorators import has_permission_decorator
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.decorators import login_required
#from productos import views as ProductUpdate
from productos.viewsy.category.views import *
from .views import (
    ProductList,
    ProductDetail,
    ProductUpdate,
    ProductDelete,
    gallery,
    ProductCreate,
    galleryAdmin
)
from . import views 
urlpatterns = [
    # category
    path('category/list/', CategoryListView.as_view(), name='category_list'),
    path('category/add/', CategoryCreateView.as_view(), name='category_create'),
    path('category/update/<int:pk>/', CategoryUpdateView.as_view(), name='category_update'),
    path('category/delete/<int:pk>/', CategoryDeleteView.as_view(), name='category_delete'),
    path('category/form/', CategoryFormView.as_view(), name='category_form'),
    #Terminacion Category
    path('listado_productos/', ProductList.as_view(), name='product_list'),
    path('create/', views.ProductCreate.as_view(), name='product-create'),
    path('view/<int:pk>/', views.ProductDetail.as_view(), name='product_view'),
    #path('new', staff_member_required(views.ProductCreate.as_view()), name='product_new'),
    #path('new', views.ProductCreate.as_view(), name='product_new'),
    #path('edit/<int:pk>',views.ProductUpdate.as_view(), name='product_edit'),
    path('edit/<int:pk>',ProductUpdate.as_view(), name='product_edit'),
    path('delete/<int:pk>', ProductDelete.as_view(), name='product_delete'),
    path('productos/', views.productos, name='productos'),
    #path('gallery/', gallery.as_view(), name='gallery'),
    path('gallery/', gallery.as_view(), name='gallery'),
    path('galleryAdmin/', galleryAdmin.as_view(), name='galleryadmin'),

]



