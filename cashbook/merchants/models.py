from django.db import models


class Merchant(models.Model):
    name = models.CharField(max_length=255)
    website = models.URLField(blank=True)

    def __unicode__(self):
        return self.name
