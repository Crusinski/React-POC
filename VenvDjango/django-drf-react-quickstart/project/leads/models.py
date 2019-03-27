from django.db import models

class Lead(models.Model) :
    name = models.CharField(maxlength=100)
    email = models.EmailFeild()
    message = models.CharField(maxlength=300)
    created_at = models.DateTimeField(auto_now_add=True)
