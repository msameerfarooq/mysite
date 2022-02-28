from dataclasses import field, fields
from pyexpat import model
from rest_framework import serializers
from .models import BookingDetails as BookingModel, Room as RoomModel, Hotel as HotelModel, Countries as CountryModel

class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = CountryModel
        fields = ['CountryID', 'Country_Name']
        
class HotelSerializer(serializers.ModelSerializer):
    class Meta:
        model = HotelModel
        fields = ['HotelID', 'Country_ID', 'Address', 'HotelName', 'FreeWifi', 'Bar', 'FitnessCenter']
        
class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = RoomModel
        fields = ['RoomID', 'Hotel_ID', 'BookingPrice', 'BedCount', 'Furnished', 'SmokingAllow', 'TelevisionAvailable', 'AirConditioned']

class BookingDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookingModel
        fields = ['BookingID', 'Room_ID', 'StartDate', 'EndDate', 'PersonName', 'CNIC', 'ContactNo']