from rest_framework import serializers
from .models import User


class UserSerializer(serializers.ModelSerializer):

    def to_representation(self, value):
        return value.__str__

    class Meta:
        model = User
        fields = ('email', 'last_login', 'date_joined', 'is_staff')