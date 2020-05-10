from django.urls import path

from users.views import *
from django.contrib.auth import views
urlpatterns = [
    path('', LoginFormView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout')
]
