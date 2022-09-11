from tkinter import Variable
from django.db import models

# Create your models here.
class Flotante(models.Model):
    variableF1 = models.FloatField(null=True, blank=True)
    variableF2 = models.FloatField(null=True, blank=True)
    variableF3 = models.FloatField(null=True, blank=True)
    variableFSuma = models.FloatField(null=True, blank=True)
    
    def suma(self):
        self.variableFSuma = self.variableF1 + self.variableF2 + self.variableF3
        self.variableFSuma = round(self.variableFSuma, 2)
        return str(self.variableFSuma)
    
    def __str__(self):
        return str(self.variableF1) + ' -- ' + str(self.variableF2) + ' -- ' + str(self.variableF3)