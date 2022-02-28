from email.headerregistry import Address
from pyexpat import model
from django.db import models
import datetime
from django.shortcuts import render
from django.contrib.auth.models import User


class Countries(models.Model):

    # Attributes
    CountryID = models.IntegerField(primary_key=True, default=1)
    Country_Name = models.CharField(default='', max_length=30, )


class Hotel(models.Model):

    # Attributes
    HotelID = models.IntegerField(default=1, )
    Country_ID = models.ForeignKey(
        Countries, related_name="Country_ID", on_delete=models.CASCADE, )
    Address = models.CharField(default='', max_length=100, )
    HotelName = models.CharField(default='', max_length=50, )

    # Hotel Features
    FreeWifi = models.BooleanField(default=True, )
    Bar = models.BooleanField(default=True, )
    FitnessCenter = models.BooleanField(default=True, )

    class Meta:
        unique_together = (('HotelID', 'Country_ID'), )


class Room(models.Model):

    # Attributes
    RoomID = models.IntegerField(default=1, )
    Hotel_ID = models.ForeignKey(
        Hotel, related_name="Hotel_ID", on_delete=models.CASCADE)
    BookingPrice = models.IntegerField(default=1, )

    # Facilities
    BedCount = models.IntegerField(default=1, )
    Furnished = models.BooleanField(default=True, )
    SmokingAllow = models.BooleanField(default=True, )
    TelevisionAvailable = models.BooleanField(default=True, )
    AirConditioned = models.BooleanField(default=True, )

    class Meta:
        unique_together = (('RoomID', 'Hotel_ID'), )


class BookingDetails(models.Model):

    #Details and Attributes
    BookingID = models.IntegerField(default=1, )
    Room_ID = models.ForeignKey(
        Room, default=1, related_name="Room_ID", on_delete=models.CASCADE)
    StartDate = models.DateField(default=datetime.date.today(), )
    EndDate = models.DateField(default=datetime.date.today(), )
    PersonName = models.CharField(default='', max_length=50, )
    CNIC = models.CharField(default='', max_length=13, )
    ContactNo = models.CharField(default='', max_length=15, )

    class Meta:
        unique_together = (('BookingID', 'Room_ID'), )
