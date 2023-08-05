from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from rest_framework.decorators import action
from rentajetapi.models import Flight

class FlightView(ViewSet):
    """Rent a Jet flights typesview"""

    def retrieve(self, request, pk):
        """Gets a flight by its pk

        Returns:
            Response --  single JSON serialized flight dictionary
        """
        flight = Flight.objects.get(pk=pk)
        serializer = FlightSerializer(flight)
        return Response(serializer.data)

    def list(self, request):
        """Gets all flights

        Returns:
            Response -- JSON serialized list of flights
        """
        flights = Flight.objects.all()
        """filter by departure airport"""
        departure_airport = request.query_params.get('departure_airport_id', None)
        if departure_airport is not None:
                flights = flights.filter(departure_airport_id=departure_airport)
        """filter by destination airport"""
        destination_airport = request.query_params.get('destination_airport_id', None)
        if destination_airport is not None:
                flights = flights.filter(destination_airport_id=destination_airport)
        """serialize all list requests"""
        serializer = FlightSerializer(flights, many=True)
        return Response(serializer.data)

class FlightSerializer(serializers.ModelSerializer):
    class Meta:
        model = Flight
        fields = ('id', 'departure_airport_id', 'destination_airport_id', 'price')
        depth = 1
