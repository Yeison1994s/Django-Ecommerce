from django.urls import path
from web.viewsy.dashboard.views import *
from web.viewsy.cliente.views import ClientView
from django.contrib.admin.views.decorators import staff_member_required
from .views import (
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
    UserPostListView,
    pos1
)
from . import views

urlpatterns = [
    path('', views.home, name='web-home'),
    path('user/<str:username>', UserPostListView.as_view(), name='user-posts'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    path('about/', views.about, name='web-about'),
    path('pos/', PostListView.as_view(), name='web-pos'),
    path('block/', views.block, name='web-block'),
    path('contacto/', views.contacto, name='web-contacto'),
    #Dashboard
    path('dashboard/',DashboardView.as_view(), name='dashboard'),
    #Cliente
    path('client/', ClientView.as_view(), name='client'),
    #Gallery Imagenes
    path('index/', views.index, name='index'),
]
