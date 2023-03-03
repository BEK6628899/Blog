from django.db import models

class Maqola(models.Model):
    sarlavha = models.CharField(max_length=50)
    matn = models.CharField(max_length=1000)
    sana = models.DateField()
    rasm = models.FileField(blank=True)
    def __str__(self):
        return self.sarlavha


