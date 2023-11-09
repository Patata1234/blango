from django.db import models
from django.conf import settings

# Create your models here.
class Tag(models.Model):
    value = models.TextField(max_length=100)
    
    def __str___(self):
        return self.value
    
class Post(models.Model):
    #Especificar modelo de usuario personalizado 
    #Protege la integridad de los datos asegurandose de que no se eliminen instancias relacionadas sin cosideracion
    author = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.PROTECT)
    created_at = models.DateField(auto_now_add=True)
    modified_at = models.DateField(auto_now=True)
    published_at = models.DateField(blank=True, null=True)
    title = models.TextField(max_length=100)
    slug = models.SlugField()#Campos slug asosiado al articulo
    summary = models.TextField(max_length=500)
    content = models.TextField()
    tags = models.ManyToManyField(Tag, related_name='posts')
    
    def __str__(self):
        return self.title