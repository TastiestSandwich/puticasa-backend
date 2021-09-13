from rest_framework import serializers
from .models import House, Resident
from users.models import User
from users.serializers import UserSerializer


class HouseSerializer(serializers.ModelSerializer):

    def to_representation(self, value):
        return value.__str__

    class Meta:
        model = House
        fields = ('id', 'name', 'description', 'status', 'last_modified_date', 'start_date', 'end_date')


class ResidentSerializer(serializers.ModelSerializer):
    house = HouseSerializer(read_only=True, many=True)
    user = UserSerializer(read_only=True, many=True)

    class Meta:
        model = Resident
        fields = ('id', 'user', 'house', 'type', 'status', 'last_modified_date', 'start_date', 'end_date')

