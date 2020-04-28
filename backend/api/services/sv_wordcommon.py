from rest_framework import viewsets, filters
from rest_framework.permissions import IsAuthenticated

from backend.api.models import CommonChinese
from backend.api.serializers.word import CommonChineseSerializer


class CustomSearch(filters.SearchFilter):
    def get_search_fields(self, view, request):
        # if request.query_params.get('vi'):
            # return ['vietnamese']
        return request.GET.getlist('search_fields', [])


class WordCommonViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)

    queryset = CommonChinese.objects.all()
    serializer_class = CommonChineseSerializer
    filter_backends = (CustomSearch,)
    # search_fields = ['chinese', 'pinyin', 'vietnamese']
    # print('fil', filter_backends[0])
    # def get_search_fields(self, view, request):
    #     print('req', request)
    #     if request.query_params.get('vi'):
    #         return ['vietnamese']

