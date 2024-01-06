from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
class Note(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    categories = models.ManyToManyField(Category, related_name='notes',blank=True)
    is_archived = models.BooleanField(default=False)

    def __str__(self):
        return self.title




