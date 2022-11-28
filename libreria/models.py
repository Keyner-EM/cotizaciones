from django.db import models

# Create your models here.
class cotizacines(models.Model):
    id= models.AutoField(primary_key=True)
    Nombre = models.CharField(max_length=100, verbose_name='Nombre')
    Telefono = models.CharField(max_length=15, null=True, verbose_name='Telefono')
    Correo = models.EmailField(unique=True, null=True, blank=True)
    Dirección = models.CharField(max_length=50, null=True, verbose_name='Direcciòn')
    Producto = models.CharField(max_length=100, null=True, verbose_name='Producto')
    imgproducto = models.ImageField(upload_to='imagenes/', verbose_name="imagen", null=True)
    precio = models.TextField(verbose_name="Precio", null=True)
    Medio_de_pago = models.CharField(max_length=100, null=True, verbose_name='Medio de pago')
    Precio_Total = models.TextField(verbose_name="Total", null=True)
    