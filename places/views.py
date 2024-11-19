
from django.shortcuts import render
from .models import Place
from django.shortcuts import render, get_object_or_404
from .models import Place, Rating
from .forms import RatingForm


def place_map(request):
    places = Place.objects.all()
    return render(request, 'places/place_map.html', {'places': places})


def place_detail(request, place_id):
    place = get_object_or_404(Place, id=place_id)
    if request.method == 'POST':
        form = RatingForm(request.POST)
        if form.is_valid():
            form.instance.user = request.user
            form.instance.place = place
            form.save()
    else:
        form = RatingForm()
    return render(request, 'places/place_detail.html', {'place': place, 'form': form})
