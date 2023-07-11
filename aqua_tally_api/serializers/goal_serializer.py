from rest_framework import serializers

from ..models import GoalModel


class GoalSerializer(serializers.ModelSerializer):
    class Meta:
        model = GoalModel
        fields = '__all__'
