from django.db import models
from django.utils import timezone

# Create your models here.# Create database here dah m3ana el models 


class post (models.Model) : # db Table created 
    title = models.CharField ( max_length = 50 ) # Column 
    content = models.TextField ( max_length = 2000 ) # another column
    created_at = models.DateTimeField(default=timezone.now)
    active = models.BooleanField(default=False)
    author_mail= models.EmailField(default='')

    def __str__ (self) : # hena 3lshan a5leha yerga3ly be title fe panel 
        return self.title