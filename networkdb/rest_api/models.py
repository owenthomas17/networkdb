from django.db import models

class Sites(models.Model):
    '''
    '''
    site_code = models.CharField(max_length=100, primary_key=True)
    site_short_code = models.CharField(max_length=100, blank=True, default='')

class Devices(models.Model):
    '''
    '''
    hostname = models.CharField(max_length=100, primary_key=True)
    make = models.CharField(max_length=100, blank=True, default='')
    model = models.CharField(max_length=100, blank=True, default='')
    site = models.ForeignKey(Sites, on_delete=models.CASCADE, blank=True, default='')

    class Meta:
        ordering = ('hostname',)

