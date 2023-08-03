from ..models import UserModel, GoalModel

def goal_achieved_verifier(goal: GoalModel, user: UserModel):
    if not (goal.ml_consumed == user.goal):
        return False
    return True