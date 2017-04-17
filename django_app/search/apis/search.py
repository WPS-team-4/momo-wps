import requests
from django.db.models import Q
from rest_framework.response import Response
from rest_framework.views import APIView

from config.settings import config
from map.models import Map
from member.models import MomoUser
from search.serializers import SearchResultSerializer

__all__ = (
    'SearchMapAndUserAPI',
    'SearchPlaceAPI',
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


class SearchPlaceAPI(APIView):
    def parseGoogleJsonToMomoJson(self, google_json):
        places = []
        results = google_json['results']
        for result in results:
            place_id = result['place_id']
            name = result['name']
            formatted_address = result['formatted_address']
            lat = result['geometry']['location']['lat']
            lng = result['geometry']['location']['lng']

            momo_json = {
                'place_id': place_id,
                'name': name,
                'address': formatted_address,
                'lat': lat,
                'lng': lng,
            }
            places.append(momo_json)
        return places

    def get(self, request, format='None'):
        url = 'https://maps.googleapis.com/maps/api/place/textsearch/json?'
        keyword = self.request.query_params.get('keyword', '')

        if keyword != '':
            keyword = keyword.strip()
            params = {
                'key': config['google_place_api']['key'],
                'query': keyword
            }
            search_result = requests.get(url, params=params).json()
            data = self.parseGoogleJsonToMomoJson(search_result)

            return Response(data)
