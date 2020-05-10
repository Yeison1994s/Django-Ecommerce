# Your code here!
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from django.forms import model_to_dict


# Create your models here.
class cliente(models.Model):
	       nombre         = models.CharField(max_length=50)
	       apellidos      = models.CharField(max_length=50)
	       status         = models.BooleanField(default=True)

	       def __unicode__(self):
	       	      nombreCompleto = "%s %s"%(self.nombre,self.apellidos)
	       	      return nombreCompleto
	       	      #retorna la concatenacion del nombre y el apellido para mostrar mas la descripcion del cliente en el panel
class Category(models.Model):
	nombre = models.CharField(max_length=50,verbose_name='Nombre', unique=True)
	descripcion = models.TextField(max_length=400,null=True, blank=True, verbose_name='Descripción')
 
	def __str__(self):
	    return self.nombre
 
	def toJSON(self):
	    item = model_to_dict(self)
	    return item
	class Meta:
	    verbose_name = 'Categoria'
	    verbose_name_plural = 'Categorias'
	    ordering = ['id']
     
class Product(models.Model):
    name = models.CharField('Name', max_length=100)
    description = models.TextField(max_length=300)
    status= models.BooleanField(default=True)
    imagen = models.ImageField(upload_to='productos/')
    precio= models.DecimalField(max_digits=6,decimal_places=2)
    stock= models.IntegerField()
    created = models.DateTimeField('Created', auto_now_add=True)
    changed = models.DateTimeField('Changed', auto_now=True)
    categorias = models.ManyToManyField(Category,null=True,blank=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('product_edit', kwargs={'pk': self.pk})

