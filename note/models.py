from django.db import models

class Note(models.Model):
    body = models.CharField('Nota', max_length=75, null=False)

    
    def __str__(self):
        return self.body
    
    
    