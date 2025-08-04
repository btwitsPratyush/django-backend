from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Payout  # 👈 Make sure your models.py has Payout

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name', 'password', 'date_joined']
        read_only_fields = ['id', 'date_joined']

    def create(self, validated_data):
        return User.objects.create_user(
            username=validated_data['username'],
            email=validated_data.get('email'),
            password=validated_data['password'],
            first_name=validated_data.get('first_name', ''),
            last_name=validated_data.get('last_name', '')
        )


class HealthCheckSerializer(serializers.Serializer):
    status = serializers.CharField()
    message = serializers.CharField()
    timestamp = serializers.DateTimeField()


class PayoutSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payout
        fields = '__all__'
        read_only_fields = ['status', 'created_at']