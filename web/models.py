from django.db import models
from django.db import models
from tinymce.models import HTMLField # is for text larger than textfield
# from versatileimagefield.fields import VersatileImageField #is for set image size as much as we need 



class Gallery(models.Model):
    photo = models.FileField(upload_to='gallery/', null=True, blank=True)
    content =models.CharField(max_length=500)
    description = HTMLField()


    
    def __str__(self):
        return str(self.content)

class Update(models.Model):
    images = models.FileField(upload_to='gallery/', null=True, blank=True)
    heading = models.CharField(max_length=200)
    subdescription = models.CharField(max_length=400)
    description = HTMLField()

    def __str__(self):
        return str(self.heading)

    