from django.db import models

# Create your models here.
class Dato(models.Model):
    var1 = models.IntegerField(null=True, blank=True)
    var2 = models.CharField(max_length = 1)
    var3 = models.IntegerField(null=True, blank=True)
    var4 = models.IntegerField(null=True, blank=True)
    
    def __str__(self):
        return str(self.var1) + ' -- ' + str(self.var2) + ' -- ' + str(self.var3) + ' -- ' + str(self.var4)