from django.shortcuts import render, get_object_or_404,redirect
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from .models import Product
from django.contrib import messages
from .forms import addProductForm
from django.contrib.messages.views import SuccessMessageMixin
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views import generic
from django.http import JsonResponse
from django.views.generic import (
    CreateView,
    ListView,
    UpdateView,
    DeleteView,
    DetailView
    )
from .decorators import unauthenticated_user, allowed_users, admin_only
from django.contrib.auth.decorators import login_required
"""
def mi_metodo(request):
    if request.method == 'POST':
        form = addProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, f'Usuario creado')
            return redirect('product_list')#redirigue a donde deseas
    else:
        form = addProductForm()

    context = {
        'form': form
    }
    return render(request, 'productos/product_home.html',context)
"""
class ProductCreate(CreateView):
    model = Product
    form_class = addProductForm
    template_name = 'productos/product_home.html'
    success_message = 'Success: Book was created.'
    success_url = reverse_lazy('product_list')
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'add':
                form = self.get_form()
                data = form.save()
            else:
                data['error'] = 'No ha ingresado a ninguna opción'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Creación de un Producto'
        context['entity'] = 'Productos'
        context['list_url'] = reverse_lazy('product_list')
        context['action'] = 'add'
        context['form'] = addProductForm()
        return context

class ProductList(ListView): 

    model = Product
    template_name ='productos/product_list.html'
    context_object_name = 'product'

    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Listado de Productos'
        context['create_url'] = reverse_lazy('product-create')
        context['list_url'] = reverse_lazy('product_list')
        context['entity'] = 'Productos'
        return context

class ProductDetail(DetailView): 
    model = Product
    template_name ='productos/detail_Product.html'

class ProductUpdate( UpdateView): 

    model = Product
    form_class = addProductForm
    template_name = 'productos/modalagregar.html'
    success_url = reverse_lazy('product_list')
    success_message = "Product successfully updated!"

class ProductDelete(DeleteView):

    model = Product
    success_url = reverse_lazy('product_list')
    success_message = "Product successfully deleted!"

class gallery(ListView):
    model = Product
    template_name ='productos/gallery.html'
    context_object_name = 'product'
    paginate_by = 18

class galleryAdmin(ListView):
    model = Product
    template_name ='productos/galleryAdmin.html'
    context_object_name = 'product'
    paginate_by = 18


def productos(request):
    return render(request, 'productos/product_home.html')