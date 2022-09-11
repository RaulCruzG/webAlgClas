from django.db import models

# Create your models here.
class Entero(models.Model):
    variableE1 = models.IntegerField(null=True, blank=True)
    variableE2 = models.IntegerField(null=True, blank=True)
    variableE3 = models.IntegerField(null=True, blank=True)
    variableESuma = models.IntegerField(null=True, blank=True)
    
    def suma(self):
        self.variableESuma = self.variableE1 + self.variableE2 + self.variableE3
        return str(self.variableESuma)
    
    def __str__(self):
        return str(self.variableE1) + ', ' + str(self.variableE2) + ', ' + str(self.variableE3)