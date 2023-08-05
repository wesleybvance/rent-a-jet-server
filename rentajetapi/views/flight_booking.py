from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from rest_framework.decorators import action
from rentajetapi.models import FlightBooking, Flight, Customer

class FlightBookingView(ViewSet):
    """Rent a Jet flight bookings typesview"""

    def retrieve(self, request, pk):
        """Gets a flight booking by its pk

        Returns:
            Response --  single JSON serialized flight booking dictionary
        """
        flight_booking = FlightBooking.objects.get(pk=pk)
        serializer = FlightBookingSerializer(flight_booking)
        return Response(serializer.data)

    def list(self, request):
        """Gets all flight bookings

        Returns:
            Response -- JSON serialized list of flight bookings
        """
        flight_bookings = FlightBooking.objects.all()
        """filter by customer id"""
        customer = request.query_params.get('customer_id', None)
        if customer is not None:
                flight_bookings = flight_bookings.filter(customer_id=customer)
        """serialize all list requests"""
        serializer = FlightBookingSerializer(flight_bookings, many=True)
        return Response(serializer.data)

    def create(self, request):
        """Handles POST operations

        Returns:
            Response -- JSON serialized flight booking instance
        """
        flight = Flight.objects.get(pk=request.data["flightId"])
        customer = Customer.objects.get(pk=request.data["customerId"])
        flight_booking = FlightBooking.objects.create(
            flight_id=flight,
            customer_id=customer,
            date=request.data["date"],
            payment_method=request.data["paymentMethod"],
        )
        serializer = FlightBookingSerializer(flight_booking)
        return Response(serializer.data)
    
    def update(self, request, pk):
        """Handles PUT requests for a flight booking

        Returns:
            Response -- Empty body with 204 status code
        """
        flight_booking = FlightBooking.objects.get(pk=pk)
        customer = Customer.objects.get(pk=request.data["customerId"])
        flight_booking.customer_id=customer
        flight = Flight.objects.get(pk=request.data["flightId"])
        flight_booking.category_id=flight
        flight_booking.date=request.data["date"]
        flight_booking.payment_method=request.data["paymentMethod"]

        flight_booking.save()

        return Response(None, status=status.HTTP_204_NO_CONTENT)

    def destroy(self, request, pk):
        """Handles DELETE requests for a flight booking

        Returns:
            Response -- Empty body with 204 status code
        """
        flight_booking = FlightBooking.objects.get(pk=pk)
        flight_booking.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)

class FlightBookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = FlightBooking
        fields = ('id', 'customer_id', 'flight_id', 'date', 'payment_method')
        depth = 2
