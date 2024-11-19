from django.db import models
from django.conf import settings

class Review(models.Model):
    place = models.ForeignKey('Place', on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    rating = models.IntegerField(choices=[(i, i) for i in range(1, 6)])  # Rating choices from 1 to 5
    comment = models.TextField(blank=True)  # Allow blank if only rating is given
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Review for {self.place} by {self.user} ({self.rating} stars)"
