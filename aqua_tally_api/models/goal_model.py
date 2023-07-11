from django.db import models

from .user_model import UserModel

class GoalModel(models.Model):
    class Meta:
        db_table = 'goal'

    date = models.DateField(primary_key=True, auto_now_add=True)
    goal_achieved = models.BooleanField(default=False)
    ml_consumed = models.IntegerField(default=0)
    goal = models.IntegerField(blank=False)
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE)
