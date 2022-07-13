from rest_framework.serializers import ModelSerializer
from .models import Bonus

class BonusSerializer(ModelSerializer):
    class Meta:
        model = Bonus
        fields = "__all__"
        read_only_fields = ["id"]