from django.db import models
class Entry(models.Model):
    ID = models.CharField(max_length=10, unique=True)
    data1 = models.CharField(max_length=100)
    data2 = models.CharField(max_length=100)

    def __str__(self):
        return f"ID: {self.ID}, Data1: {self.data1}, Data2: {self.data2}"
