from rest_framework.generics import ListAPIView

from api.filter import LimitFilter                  # 导入自定义分页器
from api.paginations import MyPageNumberPagination  # 导入基础分页器
from api.paginations import MyLimitPagination       # 导入偏移分页器
from api.paginations import MyCoursePagination      # 导入游标分页器
from api.serializers import ComputerModelSerializer  # 反序列化器

from api.models import Computer

from rest_framework.filters import SearchFilter # 导入搜索模块
from rest_framework.filters import OrderingFilter # 导入排序模块

class ComputerListAPIView(ListAPIView):

    queryset = Computer.objects.all()
    serializer_class = ComputerModelSerializer

    # 通过此参数配置过滤的器类
    filter_backends = [SearchFilter, OrderingFilter,LimitFilter] #搜素、排序、自定义分页
    # 指定当前搜索条件
    search_fields = ["name", "price"]
    # 指定排序的条件
    ordering = ["price"]

    # 指定分页器   不能使用列表 或 元祖指定
    pagination_class = MyPageNumberPagination    #基础分页器
    # pagination_class = MyLimitPagination       #偏移分页器
    # pagination_class = MyCoursePagination      #游标分页器 必须有 ordering = ["price"]的前提下