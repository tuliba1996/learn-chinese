from rest_framework import serializers

from backend.api.models import CommonChinese


class CommonChineseSerializer(serializers.ModelSerializer):
    class Meta:
        model = CommonChinese
        fields = '__all__'

