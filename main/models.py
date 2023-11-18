from django.db import models

class PersonInfo(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    department = models.CharField(max_length=20)
    course = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

