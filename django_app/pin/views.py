from django.shortcuts import render


def add_pin(request):
    return render(request, 'pin/pin.html')
