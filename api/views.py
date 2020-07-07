from rest_framework.generics import ListAPIView

from api.serializers import ComputerModelSerializer  # 反序列化器

from api.models import Computer

from rest_framework.filters import SearchFilter # 导入搜索模块
from rest_framework.filters import OrderingFilter # 导入排序模块

class ComputerListAPIView(ListAPIView):

    queryset = Computer.objects.all()
    serializer_class = ComputerModelSerializer

    # 通过此参数配置过滤的器类
    filter_backends = [SearchFilter, OrderingFilter]
    # 指定当前搜索条件
    search_fields = ["name", "price"]
    # 指定排序的条件
    ordering = ["price"]
