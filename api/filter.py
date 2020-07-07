from django_filters.rest_framework import FilterSet

from api.models import Computer

# 自定义分页器
class LimitFilter:

    def filter_queryset(self, request, queryset, view):
        limit = request.query_params.get("limit")
        if limit and queryset:
            limit = int(limit)
            return queryset[:limit]

        return queryset


# django-filter过滤器类

class ComputerFilterSet(FilterSet):
    from django_filters import filters  # 导入filters
    min_price = filters.NumberFilter(field_name="price", lookup_expr="gte")
    max_price = filters.NumberFilter(field_name="price", lookup_expr="lte")

    class Meta:
        model = Computer
        fields = ["price","brand", "min_price", "max_price"]  # 品牌（表内属性），最大大小价格（过滤器设置）
