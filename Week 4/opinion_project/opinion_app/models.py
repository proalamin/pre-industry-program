from django.db import models

class Opinion(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    election_area = models.TextField()
    party = models.CharField(max_length=50)

    def __str__(self):
        return self.name
