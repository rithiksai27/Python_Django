from django.db import models

# Create your models here.
class Organiser(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField()
    category=models.CharField(max_length=25)
    class Meta:
        db_table="Organiser"
    def __str__(self):
        return str(self.name)
class Attendee(models.Model):
    name=models.CharField(max_length=100)
    age=models.IntegerField()
    gender_choices = (("male", "m"), ("female", "f"))
    gender = models.CharField(max_length=100, blank=False, choices=gender_choices)
    interest=models.CharField(max_length=25)
    country_choices = (("India", "India"), ("foreign", "foreign"))
    country = models.CharField(max_length=100, blank=False, choices=country_choices)


    class Meta:
        db_table="Attendee"
    def __str__(self):
        return str(self.name)


class Events(models.Model):
    name = models.CharField(max_length=100)
    date = models.DateField()
    time = models.TimeField()
    description = models.TextField()
    class Meta:
        db_table="Events"
    def __str__(self):
        return str(self.name)

    def __str__(self):
        return self.name
class Admin(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    class Meta:
        db_table="Admin"