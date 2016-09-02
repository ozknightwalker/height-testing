from __future__ import unicode_literals

from django.db import models


class Height(models.Model):
    cushion = models.CharField(max_length=255)
    faucet = models.CharField(max_length=255)
    date_time = models.DateTimeField('date published', auto_now_add=True)

    def __unicode__(self):
        return self.name
