from django.db import models

# Create your models here.
class Flor(models.Model):
    nombre=models.CharField(max_length=100,primary_key=True)
    valor=models.IntegerField()
    descripcion=models.TextField()
    estado=models.CharField(max_length=1)
    stock=models.IntegerField(default=0)
    #creamos un campo de tipo Imagen que se carga en el directorio
    # pelis ubicado en "media"
    fotografia=models.ImageField(upload_to="flores",null=True)  #aqui decia pelis

    def __str__(self):
        return self.nombre
    
    class Meta:
        verbose_name='Flor'
        verbose_name_plural='Flores'

class Ticket(models.Model):
    usuario=models.CharField(max_length=100)
    nombreflor=models.CharField(max_length=100)
    precio=models.IntegerField()
    cantidad=models.IntegerField()
    total=models.IntegerField()
   

    def __str__(self):
        return str(self.usuario)+' '+str(self.titulo)