from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import FormView

from pin.forms import MapCreateForm
from pin.models import Map
from place.models import Place


#
# class PinCreate(FormView):
#     template_name = 'pin/pin-create.html'
#     form_class = PinCreateForm
#     success_url = reverse_lazy('place:search')
#
#     def form_valid(self, form):
#
#         name = form.cleaned_data.get('name', '').strip()
#         Pin.objects.create(
#             author=self.request.user,
#             name=name
#         )
#
#         return super().form_valid(form)
#
# class MapCreate(FormView):
#     template_name = 'pin/map-create.html'
#     form_class = MapCreateForm
#     success_url = reverse_lazy('pin:pin-create')
#
#     def form_valid(self, form):
#         name = form.cleaned_data.get('name', '').strip()
#         description = form.cleaned_data.get('description', '').strip()
#         Map.objects.create(
#             author=self.request.user,
#             name=name,
#             description=description,
#         )
#         return super().form_valid(form)
#
# class MapDelete()


def create_pin(request):
    if request.method == 'POST':
        form = MapCreateForm(request.POST)
        place_id = request.POST['place_id']

        if form.is_valid():
            map_name = request.POST['name']
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
        # map_form = CreateMapForm(request.POST, prefix='map')
        # pin_form = CreatePinForm(request.POST, prefix='pin')
        #
        # if map_form.is_valid():
        #     if pin_form.is_valid():
        #         map_name = request.POST['map-name']
        #         description = request.POST['map-description']
        #
        #         map = Map.objects.create(
        #             author=request.user,
        #             name=map_name,
        #             description=description
        #         )
        #
        #         pin_name = request.POST['pin-name']
        #
        #         place = Place.objects.get(
        #             place_id=place_id
        #         )
        #
        #         request.user.pin_set.create(
        #             name=pin_name,
        #             place=place,
        #             map=map,
        #         )
