from django.db import models

class Enquiry(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    service = models.CharField(max_length=50, choices=[
        ('visa', 'Visa Assistance'),
        ('passport', 'Passport Services'),
        ('ticket', 'Ticket Booking'),
        ('insurance', 'Travel Insurance'),
        ('forex', 'Forex Exchange'),
        ('package', 'Holiday Package'),
        ('other', 'Other'),
    ])
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.service}"

    class Meta:
        ordering = ['-created_at']