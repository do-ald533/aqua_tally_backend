from ..models import UserModel

def calculate_goal(user: UserModel):
    return user.weight * 35