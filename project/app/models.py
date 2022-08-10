from django.db import models

class Contact(models.Model):
    email = models.EmailField(max_length=50)
    mobile = models.IntegerField()
    massage = models.CharField(max_length=100)



