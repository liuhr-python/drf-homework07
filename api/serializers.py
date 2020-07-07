
from rest_framework.serializers import ModelSerializer

from api.models import  Computer


class ComputerModelSerializer(ModelSerializer):
    class Meta:
        model = Computer
        # 代表与模型所有字段进行映射
        # 大多数情况下都需要声明序列化去反序列化字段
        fields = ("name", "price", "brand")
