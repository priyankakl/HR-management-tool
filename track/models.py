from django.db import models

# Create your models here.
class Employee(models.Model):
    name=models.CharField(max_length=100)
    dob=models.DateField(blank=True, auto_now=True)
    doj=models.DateField(blank=True, auto_now=True)
    ecode=models.IntegerField()
    email=models.EmailField()
    department=models.CharField(max_length=100)
    designation=models.CharField(max_length=100)
    location=models.CharField(max_length=100)

    def __str__(self):
        return self.name 

class Suggestion(models.Model):
    subject=models.TextField()
    description=models.TextField()

    def __str__(self):
        return self.subject

class Star(models.Model):
    who=models.CharField(max_length=20)
    why=models.CharField(max_length=200)

    def __str__(self):
        return self.who