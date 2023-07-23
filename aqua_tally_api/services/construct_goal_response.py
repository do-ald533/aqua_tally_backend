from ..models import GoalModel, UserModel

def construct_goal_response(goal: GoalModel, user: UserModel):
    return {
        "date": goal.date,
        "id": goal.id,
        "ml_remaining": user.goal - goal.ml_consumed,
        "ml_consumed": goal.ml_consumed,
        "goal_achieved": True if goal.ml_consumed == user.goal else False,
        "last_time_consumed": goal.last_taken_at
    }