from django.db import models


class Cat(models.Model):
    name = models.CharField(max_length=120)
    weight = models.DecimalField(max_digits=4, decimal_places=1)
    age = models.IntegerField(default=0)
    meal = models.ForeignKey('Meal', on_delete=models.PROTECT)
    status = models.ForeignKey('CatStatus', on_delete=models.PROTECT)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Meal(models.Model):
    title = models.CharField(max_length=150)
    kcal = models.CharField(max_length=80)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class CatStatus(models.Model):
    title = models.CharField(max_length=150)
    value = models.DecimalField(max_digits=4, decimal_places=2)

    def __str__(self):
        return self.title
