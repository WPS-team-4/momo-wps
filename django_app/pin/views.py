from django.shortcuts import render, redirect

from pin.forms import CreateMapForm
from pin.models import Map, Pin
from place.models import Place


def add_pin(request):
    if request.method == 'POST':
        form = CreateMapForm(request.POST)
        place_id = request.POST['place_id']
        prev_path = request.POST['prev_path']

        if form.is_valid():
            name = request.POST['name']
            description = request.POST['description']

            defaults = {
                'author': request.user,
                'name': name,
                'description': description,
            }
            map, _ = Map.objects.get_or_create(
                defaults=defaults,
                name=name,
            )

            place = Place.objects.filter(place_id=place_id)

            # request.user.pin_set.create(
            #     palce=place,
            #     map=map,
            #     name=name,
            # )
            Pin.objects.create(
                author=request.user,
                place=place,
                map=map,
                name=name,
            )

    return redirect('place:search')
