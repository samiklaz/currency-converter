from django.db import models


class Currency(models.Model):
    code = models.CharField(max_length=10)
    name = models.CharField(max_length=255)

    class Meta:
        verbose_name_plural = 'Currencies'

    def __str__(self):
        return self.name
