from rest_framework import serializers
from home.models import Password

class PasswordSerializer(serializers.ModelSerializer):
    class Meta:
        model = Password
        fields = '__all__'

    # def create(self, validated_data):
    #     return self.create(validated_data)
    #
    # def update(self, instance, validated_data):
    #     return self.update(instance, validated_data)