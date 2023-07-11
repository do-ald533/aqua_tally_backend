from django.db import models
from uuid import uuid4


class UserModel(models.Model):
    class Meta:
        db_table = "user"

    id = models.UUIDField(name="id" , primary_key=True, default=uuid4)
    name = models.CharField(max_length=200, name="name", null=False)
    weight = models.FloatField(name="weight", null=False)
