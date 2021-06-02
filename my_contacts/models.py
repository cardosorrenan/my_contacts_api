from django.db import models

# Create your models here.
class Person(models.Model):

  class Meta:
    db_table = "person"

  name = models.CharField(max_length=30)
  favorite = models.BooleanField(default=False)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)


class Phone(models.Model):

  class Meta:
    db_table = "phone"
    
  person = models.ForeignKey(Person, on_delete=models.CASCADE)
  number = models.CharField(max_length=15)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)