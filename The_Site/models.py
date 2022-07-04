from django.db import models


class BlackList(models.Model):
    ip = models.CharField(max_length=45)
    time_for = models.DateTimeField('data published')

    def __str__(self):
        return f"ip: {self.ip} \ntime_for: {self.time_for}"
