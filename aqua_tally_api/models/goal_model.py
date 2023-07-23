from django.db import models
from uuid import uuid4
from datetime import datetime

from .user_model import UserModel

class GoalModel(models.Model):
    class Meta:
        db_table = 'goal'

    id = models.UUIDField(name="id" , primary_key=True, default=uuid4)
    date = models.DateField(db_index=True)
    goal_achieved: models.BooleanField = models.BooleanField(default=False)
    ml_consumed = models.IntegerField(default=0)
    last_taken_at = models.DateTimeField(default=datetime.today())
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE, db_index=True)
