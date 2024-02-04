from django.db import models


class Restaurant(models.Model):
    name = models.CharField(max_length=50)
    specialization = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    website = models.URLField()
    phone = models.CharField(max_length=12)


    class Meta:
        app_label = 'apfelschuss.votes'

    def __str__(self):
        return self.user.username