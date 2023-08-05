from rest_framework.viewsets import ViewSet
from rest_framework import serializers
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework import status
from rentajetapi.models import Customer

class CustomerView(ViewSet):
    def retrieve(self, request, pk):
        """Handle GET requests for a single customer"""
        
        customer = Customer.objects.get(pk=pk)
        serializer = CustomerSerializer(customer)
        return Response(serializer.data)
    
    def create(self, request):
        """POST request to create a customer"""
        uid = request.META["HTTP_AUTHORIZATION"]
        serializer = CustomerSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(uid=uid)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def update(self, request, pk):
        """PUT request to update a customer"""
        customer = Customer.objects.get(pk=pk)
        uid = request.META["HTTP_AUTHORIZATION"]
        customer.first_name = request.data['firstName']
        customer.last_name = request.data['lastName']
        customer.email = request.data['username']
        customer.phone_number = request.data['imageUrl']
        customer.profile_image = request.data['address']
        customer.home_airport = uid
        customer.save()
        return Response({'message': 'Customer Updated'}, status=status.HTTP_204_NO_CONTENT)

class CustomerSerializer(serializers.ModelSerializer):
    """JSON serializer for customer
    """
    class Meta:
        model = Customer
        fields = ('id', 'first_name', 'last_name', 'email', 'phone_number', 'profile_image', 'home_airport', 'uid')
