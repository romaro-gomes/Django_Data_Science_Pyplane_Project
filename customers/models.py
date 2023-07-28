from django.db import models

class Customer(models.Model):
    company_name = models.CharField(max_length=220)
    budget = models.PositiveIntegerField()
    employment=models.PositiveBigIntegerField()
    joined=models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return str(self.company_name)
        
