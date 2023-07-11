from ...models import UserModel, GoalModel


class CreateGoalService:

    def create_goal(self, user_id: str):
        try:
            user = UserModel.objects.get(id=user_id)
            goal_dict = {"goal": user.weight * 35, "user_id": user.id}
            goal = GoalModel.objects.create(**goal_dict)
            return goal
        except UserModel.DoesNotExist:
            raise UserModel.DoesNotExist
