from django.db import models


class Subscriber(models.Model):
    email = models.EmailField()
    active = models.BooleanField(default=0)

    def __repr__(self):
        return f"{self.email}"

    def __str__(self):
        return f"{self.email}"