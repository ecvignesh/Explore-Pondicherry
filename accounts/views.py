from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm

# accounts/views.py (User Dashboard)
from django.contrib.auth.decorators import login_required
from bookings.models import Booking
from places.models import Review


def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = CustomUserCreationForm()
    return render(request, 'accounts/register.html', {'form': form})




@login_required
def user_dashboard(request):
    bookings = Booking.objects.filter(user=request.user)
    reviews = Review.objects.filter(user=request.user)
    return render(request, 'accounts/user_dashboard.html', {'bookings': bookings, 'reviews': reviews})
