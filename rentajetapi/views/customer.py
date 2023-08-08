from rest_framework.viewsets import ViewSet
from rest_framework import serializers
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework import status
from rentajetapi.models import Customer, Airport

class CustomerView(ViewSet):
    def retrieve(self, request, pk):
        """Handle GET requests for a single customer"""
        
        customer = Customer.objects.get(pk=pk)
        serializer = CustomerSerializer(customer)
        return Response(serializer.data)
    
    def create(self, request):
        """POST request to create a customer"""
        uid = request.META["HTTP_AUTHORIZATION"]
        airport = Airport.objects.get(pk=request.data["homeAirport"])
        
        customer = Customer(
            uid = uid,
            first_name = request.data['firstName'],
            last_name = request.data['lastName'],
            email = request.data['username'],
            phone_number = request.data['phoneNumber'],
            profile_image = request.data['profileImage'],
            home_airport = airport,
        )
        
        serializer = CustomerSerializer(customer)
        serializer.is_valid(raise_exception=True)
        serializer.save(uid=uid)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def update(self, request, pk):
        """PUT request to update a customer"""
        customer = Customer.objects.get(pk=pk)
        uid = request.META["HTTP_AUTHORIZATION"]
        customer.first_name = request.data['firstName']
        customer.last_name = request.data['lastName']
        customer.email = request.data['email']
        customer.phone_number = request.data['phoneNumber']
        customer.profile_image = request.data['profileImage']
        customer.home_airport = request.data['homeAirport']
        customer.uid = uid
        customer.save()
        return Response({'message': 'Customer Updated'}, status=status.HTTP_204_NO_CONTENT)
    
    def destroy(self, request, pk):
        """Handles DELETE requests for a customer

        Returns:
            Response -- Empty body with 204 status code
        """
        customer = Customer.objects.get(pk=pk)
        customer.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)

class CustomerSerializer(serializers.ModelSerializer):
    """JSON serializer for customer
    """
    class Meta:
        model = Customer
        fields = ('id', 'first_name', 'last_name', 'email', 'phone_number', 'profile_image', 'home_airport', 'uid')
        depth = 1
