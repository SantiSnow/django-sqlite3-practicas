from django.db import models

# Create your models here.


class Articulo(models.Model):

    nombre = models.CharField(max_length=80)
    precio = models.FloatField()
    stock = models.IntegerField()
    seccion = models.CharField(max_length=50)

    def __init__(self, nombre, precio, stock, seccion):
        self.nombre = nombre
        self.precio = precio
        self.stock = stock
        self.seccion = seccion


class Cliente(models.Model):

    nombre = models.CharField(max_length=80)
    direccion = models.CharField(max_length=80)
    email = models.EmailField()
    telefono = models.IntegerField()
    compras = models.IntegerField()
    comentarios = models.CharField(max_length=120)

    def __init__(self, nombre, direccion, email, telefono, compras, comentarios):
        self.nombre = nombre
        self.direccion = direccion
        self.email = email
        self.telefono = telefono
        self.compras = compras
        self.comentarios = comentarios


class Pedido(models.Model):

    cantidad = models.IntegerField()
    fecha = models.DateField()
    entregado = models.BooleanField()
    pagado = models.BooleanField()

    def __init__(self, cantidad, fecha, entregado, pagado):
        self.cantidad = cantidad
        self.fecha = fecha
        self.entregado = entregado
        self.pagado = pagado



