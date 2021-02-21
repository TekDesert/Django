from rest_framework import serializers
from . models import Person
from . models import Country

class PersonSerializer(serializers.ModelSerializer):

    class Meta: 
        model= Person
#        fields=('firstname','country')
        fields= '__all__'

class CountrySerializer(serializers.ModelSerializer):

    class Meta: 
        model= Country
#        fields=('firstname','country')
        fields= '__all__'