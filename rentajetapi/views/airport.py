from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from rentajetapi.models import Airport

class AirportView(ViewSet):
    """Rent-a-jet airports view"""

    def retrieve(self, request, pk):
        """Handle GET requests for single airport

        Returns:
            Response -- JSON serialized airport
        """
        airport = Airport.objects.get(pk=pk)
        serializer = AirportSerializer(airport)
        return Response(serializer.data)


    def list(self, request):
        """Handle GET requests to get all airports

        Returns:
            Response -- JSON serialized list of airports
        """
        airports = Airport.objects.all()
        serializer = AirportSerializer(airports, many=True)
        return Response(serializer.data)

class AirportSerializer(serializers.ModelSerializer):
    """JSON serializer for airports
    """
    class Meta:
        model = Airport
        fields = ('id', 'city', 'code')
