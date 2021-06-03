from django.db import models

# Create your models here.
class Person(models.Model):
  name = models.CharField(max_length=30)
  favorite = models.BooleanField(default=False)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

  class Meta:
    db_table = "person"

  def __str__(self):
    return '%d: %s' % (self.id, self.name)



class Phone(models.Model):
  person = models.ForeignKey(Person, related_name='phones', on_delete=models.CASCADE)
  number = models.CharField(max_length=15)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

  class Meta:
    db_table = "phone"

  def __str__(self):
    return '%d: %s' % (self.id, self.number)