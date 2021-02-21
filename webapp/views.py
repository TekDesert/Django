from django.shortcuts import render

from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from . models import Person
from . models import Country
from . serializers import PersonSerializer, CountrySerializer


class personList(APIView):

    def get(self, request):
        person1 = Person.objects.all() #GetAllPersons
        serializer = PersonSerializer(person1, many= True)
        return Response(serializer.data)

    def post(self):
        pass

class countryList(APIView):

    def get(self, request):
        country1 = Country.objects.all() #GetAllPersons
        serializer = CountrySerializer(country1, many= True)
        return Response(serializer.data)

    def post(self):
        pass