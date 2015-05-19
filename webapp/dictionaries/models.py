from django.db import models


class FoodCategory(models.Model):
    name = models.CharField(max_length=100)

    def __unicode__(self):
        return self.name


class MeatIssues(models.Model):
    name = models.CharField(max_length=100)

    def __unicode__(self):
        return self.name


class ReligiousIssues(models.Model):
    name = models.CharField(max_length=100)

    def __unicode__(self):
        return self.name


class PackagingCategory(models.Model):
    name = models.CharField(max_length=100)

    def __unicode__(self):
        return self.name


class TemperatureCategory(models.Model):
    name = models.CharField(max_length=100)

    def __unicode__(self):
        return self.name


class FoodIngredients(models.Model):
    name = models.CharField(max_length=100)

    def __unicode__(self):
        return self.name


class DaysOfTheWeek(models.Model):
    name = models.CharField(max_length=100)
    order = models.IntegerField()

    def __unicode__(self):
        return self.name

