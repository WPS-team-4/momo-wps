import requests
from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from config.settings import config
from pin.forms import MapCreateForm
from place.forms import SearchPlaceForm
from place.models import Place


def search_from_google_place(keyword):
    params = {
        'key': config['google_place_api']['key'],
        'query': keyword
    }
    r = requests.get('https://maps.googleapis.com/maps/api/place/textsearch/json?', params=params)
    r_to_json = r.json()
    results = r_to_json['results']
    return results


def search(request):
    places = []
    form = SearchPlaceForm()
    context = {
        'form': form,
    }

    keyword = request.GET.get('keyword', '').strip()

    if keyword != '':
        search_results = search_from_google_place(keyword)

        for result in search_results:
            formatted_address = result['formatted_address']
            lat = result['geometry']['location']['lat']
            lng = result['geometry']['location']['lng']
            name = result['name']
            place_id = result['place_id']

            # pin을 한 장소인지 판단
            # is_exist = Pin.objects.filter(
            #     author=request.user,
            #     place__place_id=place_id
            # ).exists()

            data = {
                'address': formatted_address,
                'lat': lat,
                'lng': lng,
                'name': name,
                'place_id': place_id,
                # 'is_exist': is_exist
            }
            # print(data)
            places.append(data)
            form = SearchPlaceForm()
            context = {
                'form': form,
                'places': places,
            }

    return render(request, 'place/search.html', context)


@login_required
def create_place(request):
    if request.method == 'POST':
        place_id = request.POST['place_id']
        name = request.POST['name']
        address = request.POST['address']
        lat = request.POST['lat']
        lng = request.POST['lng']

        defaults = {
            'place_id': place_id,
            'name': name,
            'address': address,
            'lat': lat,
            'lng': lng
        }
        place, _ = Place.objects.get_or_create(
            defaults=defaults,
            place_id=place_id,
        )

        form = MapCreateForm()
        context = {
            'form': form,
            'place': place,
        }
        return render(request, 'pin/pin.html', context)
