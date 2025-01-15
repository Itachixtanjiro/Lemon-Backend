from django.db import models

# Model for Menu table
class Menu(models.Model):
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    inventory = models.SmallIntegerField()

    def __str__(self):
        return f'{self.title} : {str(self.price)}'


# Model for Booking table
class Booking(models.Model):
    name = models.CharField(max_length=255)  # Name of the person making the booking
    no_of_guests = models.IntegerField()  # Number of guests for the booking
    booking_date = models.DateTimeField()  # Date and time of the booking

    def __str__(self):
        return f"Booking for {self.name} on {self.booking_date}"

class MenuItem(models.Model):
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    inventory = models.SmallIntegerField()

    def get_item(self):
        return f'{self.title} : {str(self.price)}'
