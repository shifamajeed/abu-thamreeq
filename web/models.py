from django.db import models
from django.db import models
# from tinymce.models import HTMLField # is for text larger than textfield
# from versatileimagefield.fields import VersatileImageField #is for set image size as much as we need 



class Gallery(models.Model):
    photo = models.FileField(upload_to='gallery/', null=True, blank=True)
    content =models.CharField(max_length=500)


    
    def __str__(self):
        return str(self.content)