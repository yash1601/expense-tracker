from django.db import models


# Create your models here.

class Expense(models.Model):
    title = models.CharField(max_length=200)
    amount = models.IntegerField()
    detail = models.TextField(null=True, max_length=500, default=None, blank=True)

    def __str__(self):
        return f"{self.title} - {self.amount}"
