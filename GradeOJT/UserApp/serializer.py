from rest_framework import serializers
from UserApp.models import Roles, Sections, Users

class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Roles
        fields = ('RoleId',
                'RoleName')
class SectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sections
        fields = ('SectionId', 'SectionYear', 'SectionName')

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = ('UserId', 'UserName', 'Role', 'PhotoFileName', 'Section')