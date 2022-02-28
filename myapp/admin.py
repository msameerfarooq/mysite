from django.contrib import admin
from .models import BookingDetails as BookingModel, Room as RoomModel, Hotel as HotelModel, Countries as CountryModel

admin.site.register(CountryModel)
admin.site.register(HotelModel)
admin.site.register(RoomModel)
admin.site.register(BookingModel)
