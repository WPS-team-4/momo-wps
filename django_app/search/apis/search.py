from django.db.models import Q
from rest_framework.response import Response
from rest_framework.views import APIView

from map.models import Map
from member.models import MomoUser
from search.serializers import SearchResultSerializer

__all__ = (
    'SearchMapAndUserAPI',
)


class SearchResult():
    def __init__(self, maps, users):
        self.maps = maps
        self.users = users


class SearchMapAndUserAPI(APIView):
    def get(self, request, format='None'):
        keyword = self.request.query_params.get('keyword', None)
        print('keyword: {}'.format(keyword))
        map_list = list(Map.objects.all().filter(Q(map_name__icontains=keyword) | Q(description__icontains=keyword)))
        user_list = list(MomoUser.objects.all().filter(username__icontains=keyword))

        result = SearchResult(map_list, user_list)

        results = SearchResultSerializer(result).data

        return Response(results)
