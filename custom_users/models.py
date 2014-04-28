from django.db import models

class CustomUser(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50, blank=True, null=True)
    email = models.EmailField()

    # Giving myself a convenient way to create from the command line
    @classmethod
    def create(cls, first_name, last_name, email):
        user_ = cls(first_name=first_name, last_name=last_name, email=email)
        return user_

    def __unicode__(self):
        return self.first_name
