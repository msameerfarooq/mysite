from asyncio.windows_events import NULL
from email.mime import base
from http.client import HTTPResponse
from tabnanny import check
from telnetlib import STATUS
from turtle import update
from urllib import response
from wsgiref.util import request_uri
from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated, AllowAny
from django.http import HttpResponse, JsonResponse
from django.core.serializers import serialize

import json
import _json
import numpy as np
import pandas as pd
import re
import random
import datetime

# Create your views here.
from rest_framework import viewsets, status, serializers
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import BookingDetails as BookingModel, Room as RoomModel, Hotel as HotelModel, Countries as CountryModel
from .Serializer import BookingDetailSerializer, RoomSerializer, HotelSerializer, CountrySerializer

# Helping Functions


def BadRequest():
    return Response({'message': 'Invalid Key/s'}, status=status.HTTP_400_BAD_REQUEST)


def getWholeList(querySet):
    return JsonResponse(list(querySet.values()), safe=False, status=status.HTTP_200_OK)


def TakeDecision(querySet, keyValue, checkKeyValue=True, isNotBookingDetails=True):
    try:
        if checkKeyValue:
            querySet = querySet.filter(pk=keyValue)
        if querySet.count() != 0:
            return getWholeList(querySet)
        else:
            return Response({'message': 'Element Not Found'}, status=status.HTTP_204_NO_CONTENT)

    except:
        return BadRequest()


class CountrySet(viewsets.ModelViewSet):
    queryset = CountryModel.objects.all()
    serializer_class = CountrySerializer

    def list(self, request, *args, **kwargs):
        if(len(request.data)):
            return TakeDecision(self.queryset.filter(
                CountryID=request.data['C_ID']), NULL, False)
        else:
            return getWholeList(self.queryset)
 
    def create(self, request, *args, **kwargs):
        if(len(request.data)):
            return TakeDecision(self.queryset.filter(
                CountryID=request.data['countID']), NULL, False)
        else:
            return getWholeList(self.queryset)    

    def retrieve(self, request, *args, **kwargs):
        return TakeDecision(self.queryset, NULL, False)


class HotelSet(viewsets.ModelViewSet):
    queryset = HotelModel.objects.all()
    serializer_class = HotelSerializer

    def create(self, request, *args, **kwargs):
        if(len(request.data)):
            try:
                return TakeDecision(HotelModel.objects.filter(HotelID=request.data['HotelID'], Country_ID=request.data['countID']), NULL, False)
            except:
                try:
                    return TakeDecision(HotelModel.objects.filter(Country_ID=request.data['countID']), NULL, False)
                except:
                    return BadRequest()
        else:
            return getWholeList(self.queryset)

    def retrieve(self, request, *args, **kwargs):
        return TakeDecision(self.queryset, NULL, False)


class RoomsSet(viewsets.ModelViewSet):
    queryset = RoomModel.objects.all()
    serializer_class = RoomSerializer

    def getRoomInstance(self, RoomNumber):
        return self.queryset.get(RoomID=RoomNumber)

    def create(self, request, *args, **kwargs):
        if(len(request.data)):
            try:
                return TakeDecision(self.queryset.filter(
                    RoomID=request.data['RoomID'], Hotel_ID=request.data['HotelID']), NULL, False)
            except:
                try:
                    return TakeDecision(self.queryset.filter(Hotel_ID=request.data['HotelID']), NULL, False)

                except:
                    return BadRequest()

        else:
            return getWholeList(self.queryset)


class BookingDetailsSet(viewsets.ModelViewSet):
    queryset = BookingModel.objects.all()
    serializer_class = BookingDetailSerializer

    def create(self, request, *args, **kwargs):
        if(len(request.data)):
            try:
                return TakeDecision(self.queryset.filter(
                    BookingID=request.data['BookingID'], Room_ID=request.data['RoomID']), NULL, False, False)
            except:
                try:
                    return TakeDecision(self.queryset.filter(Room_ID=request.data['RoomID']), NULL, False, False)
                except:
                    pass
        else:
            return getWholeList(self.queryset)
        return BadRequest()

    def put(self, request, *args, **kwargs):
        try:
            if(request.data['flag'] == 1):
                try:
                    self.queryset.create(BookingID=self.queryset.latest('BookingID').id+1, Room_ID=BookingModel.Room_ID.get_queryset().filter(RoomID=request.data['RoomID']).first(
                    ), StartDate=request.data['SDate'], PersonName=request.data['pName'], CNIC=request.data['Cnic'], ContactNo=request.data['C_No'])
                except:
                    return Response([{'message': 'Incorrect Data Formatting'}], status=status.HTTP_400_BAD_REQUEST)
            else:
                try:
                    self.queryset.get(
                        StartDate=request.data['SDate'], Room_ID=request.data['RoomID']).delete()
                    return Response([{'message': 'Un-Booked'}], status=status.HTTP_200_OK)
                except:
                    return Response([{'message': 'Error'}], status=status.HTTP_204_NO_CONTENT)
        except:
            return BadRequest()

