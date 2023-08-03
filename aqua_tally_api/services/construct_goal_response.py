from ..models import GoalModel, UserModel


def construct_goal_response(goal: GoalModel, user: UserModel):
    return {
        "date": goal.date.isoformat(),
        "id": goal.id.hex,
        "ml_remaining": user.goal - goal.ml_consumed,
        "ml_consumed": goal.ml_consumed,
        "goal_achieved": goal.goal_achieved,
        # "last_time_consumed": ,
    }
