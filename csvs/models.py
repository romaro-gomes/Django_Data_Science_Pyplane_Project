from django.db import models

class Csv(models.Model):
    file_name = models.FileField(upload_to='csvs/', max_length=100)
    uploaded= models.DateTimeField(auto_now_add=True)
    activated = models.BooleanField(default=False)
    
    def __str__(self):
        return f'File Id:{self.id} | Uploaded: {self.uploaded} | Activate: {self.activated}'