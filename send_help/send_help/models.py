from django.db import models
from django.contrib.auth.models import User
from address.models import AddressField


class Helper(User):
    suscribe_date = models.DateTimeField('subscription date')

    def __str__(self):
        return self.username


class Needer(User):
    address = AddressField()
    suscribe_date = models.DateTimeField('subscription date')
    nb_members = models.IntegerField(default=1)

    def __str__(self):
        return self.username


class Choice(models.Model):
    helper = models.ForeignKey(Helper)
    needer = models.ForeignKey(Needer)
    contract_date = models.DateTimeField()
    received = models.BooleanField(default=False)
