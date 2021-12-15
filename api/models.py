from django.db import models

class Measurement(models.Model):
    sensor_data = models.FloatField()

    def __str__(self):
        return f'{self.sensor_data}'

