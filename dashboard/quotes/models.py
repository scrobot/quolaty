from django.db import models


class Quote(models.Model):
    original = models.TextField()
    author = models.CharField(max_length=250, blank=True, null=True)

    def __str__(self):
        return self.original


class Language(models.Model):
    code = models.CharField(max_length=5)
    name = models.CharField(max_length=50)
    iso = models.CharField(max_length=5, blank=True, null=True)

    def __str__(self):
        return self.name


class Translate(models.Model):
    quote = models.ForeignKey(Quote, on_delete=models.CASCADE)
    language = models.ForeignKey(Language, on_delete=models.CASCADE)
    text = models.TextField()

    def __str__(self):
        return self.text
