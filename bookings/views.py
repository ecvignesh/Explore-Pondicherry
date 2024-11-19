from django.shortcuts import render, get_object_or_404, redirect
from .models import Place, Booking
from .forms import BookingForm

from django.shortcuts import render

import stripe
from django.conf import settings
from django.shortcuts import render, redirect
from .forms import PaymentForm



from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required


stripe.api_key = settings.STRIPE_TEST_SECRET_KEY


def bookings(request):
    # Your logic for the bookings page
    return render(request, 'bookings.html')  # Replace 'bookings.html' with the actual template name


def place_list(request):
    places = Place.objects.all()
    return render(request, 'bookings/place_list.html', {'places': places})

def place_detail(request, place_id):
    place = get_object_or_404(Place, id=place_id)
    if request.method == "POST":
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.place = place
            booking.save()
            return redirect('place_list')
    else:
        form = BookingForm()
    return render(request, 'bookings/place_detail.html', {'place': place, 'form': form})




def payment(request):
    if request.method == 'POST':
        form = PaymentForm(request.POST)
        if form.is_valid():
            stripe_token = form.cleaned_data['stripeToken']
            # charge the user's card
            charge = stripe.Charge.create(
                amount=5000,  # Amount in cents
                currency='usd',
                description='Booking payment',
                source=stripe_token,
            )
            return redirect('payment_success')
    else:
        form = PaymentForm()
    return render(request, 'bookings/payment.html', {'form': form})



def payment_success(request):
    return render(request, 'bookings/payment_success.html')


@login_required
def booking_edit(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id, user=request.user)
    if request.method == 'POST':
        form = BookingForm(request.POST, instance=booking)
        if form.is_valid():
            form.save()
            return redirect('booking_list')
    else:
        form = BookingForm(instance=booking)
    return render(request, 'bookings/booking_form.html', {'form': form})

@login_required
def booking_cancel(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id, user=request.user)
    booking.delete()
    return redirect('booking_list')
