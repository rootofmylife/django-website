from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100)
    date = models.DateField()
    genre = models.CharField(max_length=100)

    def __str__(self):
        return self.name + ' - ' + self.genre

class News(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    headline = models.CharField(max_length=100)
    body = models.CharField(max_length=100000)

    def __str__(self):
        return self.headline