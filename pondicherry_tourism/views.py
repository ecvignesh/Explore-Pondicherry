from django.shortcuts import render
from .models import Place, Booking

def place_list(request):
    places = Place.objects.all()
    return render(request, 'places/place_list.html', {'places': places})

def place_detail(request, place_id):
    place = Place.objects.get(id=place_id)
    return render(request, 'places/place_detail.html', {'place': place})

def bookings(request):
    bookings = Booking.objects.all()
    return render(request, 'bookings/booking_list.html', {'bookings': bookings})
