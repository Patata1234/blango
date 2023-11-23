from django.db import models
from django.conf import settings
                                              #Permite a un modelo tener una relacion con cualquier otro modelo de la aplicaicon
from django.contrib.contenttypes.fields import GenericForeignKey, GenericRelation #Relaciones polimorficas entre modelos
                                              #Almacena unformacion sobre los modelos en la aplicacion
from django.contrib.contenttypes.models import ContentType #Relaciones polimorficas entre modelos 


# Create your models here.
class Tag(models.Model):
    value = models.TextField(max_length=100)
    
    def __str___(self):
        return self.value
      
class Comment(models.Model):
    
    creator = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    content = models.TextField()
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE, default=None)
    object_id = models.PositiveIntegerField(default=None,null=True)
    content_object = GenericForeignKey("content_type", "object_id")
    created_at = models.DateField(auto_now_add=True)
    modified_at = models.DateField(auto_now=True)
 
class Post(models.Model):
    #Especificar modelo de usuario personalizado 
    #Protege la integridad de los datos asegurandose de que no se eliminen instancias relacionadas sin cosideracion  
    author = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.PROTECT)
    created_at = models.DateField(auto_now_add=True)
    modified_at = models.DateField(auto_now=True)
    published_at = models.DateField(blank=True, null=True)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    title = models.TextField(max_length=100)
    slug = models.SlugField()#Campos slug asosiado al articulo
    summary = models.TextField(max_length=500)
    content = models.TextField()
    tags = models.ManyToManyField(Tag, related_name='posts')
    comments = GenericRelation(Comment)  
    
    def __str__(self):
        return self.title
