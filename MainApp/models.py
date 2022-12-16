from django.db import models


class CountryModel(models.Model):
    country = models.CharField(max_length=100)
    languages = models.ManyToManyField("LanguagesModel")

    def __str__(self):
        return self.country

    class Meta:
        verbose_name = "country"
        verbose_name_plural = "countries"


class LanguagesModel(models.Model):
    languages = models.CharField(max_length=100)

    def __str__(self):
        return self.languages

    class Meta:
        verbose_name = "language"
        verbose_name_plural = "languages"
