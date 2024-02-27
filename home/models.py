from django.db import models

class Entry(models.Model):
    ID= models.CharField( max_length=10, primary_key=True)
    NAME= models.CharField( max_length=51, blank=False)
    EMAIL= models.CharField( max_length=51,unique=True, blank=False)

    def __str__(self):
        return self.NAME
    
