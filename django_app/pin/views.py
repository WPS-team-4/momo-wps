from django.shortcuts import redirect

from pin.forms import CreateMapForm
from pin.models import Map
from place.models import Place


def add_pin(request):
    if request.method == 'POST':
        form = CreateMapForm(request.POST)
        place_id = request.POST['place_id']

        if form.is_valid():
            map_name = request.POST['map_name']
            description = request.POST['description']

            map = Map.objects.create(
                author=request.user,
                name=map_name,
                description=description
            )

            place = Place.objects.get(
                place_id=place_id
            )

            request.user.pin_set.create(
                place=place,
                map=map,
            )

    return redirect('place:search')
