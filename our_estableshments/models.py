from django.db import models


class Branch(models.Model):
    title = models.CharField(max_length=25, verbose_name='Name of branch')
    address = models.CharField(max_length=20, verbose_name='Address of branch')
    image = models.ImageField(upload_to='branch/%y/%m')

    class Meta:
        verbose_name_plural = 'branch'



# Create your models here.
