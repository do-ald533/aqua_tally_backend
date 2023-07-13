from ..models import UserModel, GoalModel

def calculate_goal(user: UserModel):
    return GoalModel.objects.create(user=user, goal=user.weight * 35)