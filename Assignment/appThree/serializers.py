from rest_framework import serializers
from appThree.models import UserInfo

class UserInfoSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserInfo
        fields = '__all__'