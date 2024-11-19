from django.core.management.base import BaseCommand
from bookings.models import Place  # Make sure Place is the correct model for your places

class Command(BaseCommand):
    help = 'Populates the tourist places into the database'

    def handle(self, *args, **kwargs):
        places = [
            {"name": "Rock Beach", "description": "Rock Beach (or, known as, 'Pondicherry Beach'. French: Plage de la promenade) is the popular stretch of beachfront in the city of Puducherry, India, along the Bay of Bengal. It is a 1.2-kilometre-long stretch in Pondicherry, starts from War Memorial and end at Dupleix Park on the Goubert Avenue."},
            {"name": "Auroville", "description": "Auroville - An experimental township promoting human unity, featuring the iconic Matrimandir, a golden globe symbolizing peace and meditation."},
            {"name": "Serenity Beach", "description": "Serenity Beach - A peaceful beach popular for surfing and sunbathing, offering a quieter alternative to more crowded spots."},
            {"name": "Basilica of the Sacred Heart of Jesus", "description": "Basilica of the Sacred Heart of Jesus - A beautiful church showcasing Gothic architecture, famous for its intricate stained glass windows."},
            {"name": "Manakula Vinayagar Temple", "description": "Manakula Vinayagar Temple - A vibrant Hindu temple dedicated to Lord Ganesha, known for its unique architecture and spiritual significance."},
            {"name": "Goubert Market", "description": "Goubert Market - A lively market where visitors can shop for local produce, handicrafts, and souvenirs."},
            {"name": "Pondicherry Botanical Garden", "description": "Pondicherry Botanical Garden - A serene garden featuring a variety of exotic plants, fountains, and a musical fountain show on weekends."},
            {"name": "Ousteri Lake", "description": "Ousteri Lake - A picturesque lake known for its rich biodiversity and birdwatching opportunities, perfect for nature lovers."},
            {"name": "EDEN Beach", "description": "EDEN Beach - A lesser-known beach with a long coastline, ideal for peaceful walks and enjoying nature."},
        ]

        for place in places:
            Place.objects.create(name=place['name'], description=place['description'])

        self.stdout.write(self.style.SUCCESS('Successfully populated places data'))
