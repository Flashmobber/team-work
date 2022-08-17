from django.db import models


class Author(models.Model):
    full_name = models.CharField(max_length=255)

    def __str__(self):
        return self.full_name


class Tag(models.Model):
    name = models.CharField(max_length=63)

    def __str__(self):
        return self.name


class Quote(models.Model):
    content = models.TextField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag, related_name="quotes")

    def __str__(self):
        return self.content
