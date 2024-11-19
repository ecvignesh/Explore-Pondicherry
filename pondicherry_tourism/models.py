from django.db import models

class Place(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    location = models.CharField(max_length=200)
    category = models.CharField(max_length=100, choices=[
        ('beach', 'Beach'),
        ('temple', 'Temple'),
        ('church', 'Church'),
        ('market', 'Market'),
        ('garden', 'Garden'),
        ('lake', 'Lake'),
    ])
    opening_hours = models.CharField(max_length=100, blank=True, null=True)
    entry_fee = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    image = models.ImageField(upload_to='places/', blank=True, null=True)

    def __str__(self):
        return self.name

class Booking(models.Model):
    place = models.ForeignKey(Place, on_delete=models.CASCADE, related_name='bookings')
    user_name = models.CharField(max_length=100)
    user_email = models.EmailField()
    booking_date = models.DateField()
    number_of_people = models.PositiveIntegerField()
    special_requests = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Booking for {self.user_name} at {self.place.name} on {self.booking_date}"
