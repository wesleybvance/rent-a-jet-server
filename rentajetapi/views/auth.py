from rest_framework.decorators import api_view
from rest_framework.response import Response
from rentajetapi.models.customer import Customer
from rentajetapi.models.airport import Airport
from rest_framework import status
from rentajetapi.views.customer import CustomerSerializer
from rentajetapi.views.airport import AirportSerializer


@api_view(['POST'])
def check_user(request):
    '''Checks to see if User has Associated Customer

    Method arguments:
      request -- The full HTTP request object
    '''
    uid = request.data['uid']

    # Use the built-in authenticate method to verify
    # authenticate returns the user object or None if no user is found
    customer = Customer.objects.filter(uid=uid).first()

    # If authentication was successful, respond with their token
    if customer is not None:
        
        airport = AirportSerializer(Airport.objects.get(pk=customer.home_airport.id))
        
        data = {
            'id': customer.id,
            'uid': customer.uid,
            'first_name': customer.first_name,
            'last_name': customer.last_name,
            'phone_number': customer.phone_number,
            'email': customer.email,
            'profile_image': customer.profile_image,
            'home_airport': airport.data,
        }
        return Response(data)
    else:
        # Bad login details were provided. So we can't log the user in.
        data = { 'valid': False }
        return Response(data)


@api_view(['POST'])
def register_user(request):
    '''Handles the creation of a new customer for authentication

    Method arguments:
      request -- The full HTTP request object
    '''

    # # Now save the customer info
    # customer = Customer.objects.create(
    #     uid=request.data['uid'],
    #     first_name = request.data["firstName"],
    #     last_name = request.data["lastName"],
    #     email = request.data["email"],
    #     profile_image = request.data["profileImage"],
    #     phone_number = request.data["phoneNumber"],
    #     home_airport = Airport.objects.get(pk=request.data["homeAirport"])
    # )

    # # Return the customer info to the client
    # data = {
    #         'id': customer.id,
    #         'uid': customer.uid,
    #         'first_name': customer.first_name,
    #         'last_name': customer.last_name,
    #         'email': customer.email,
    #         'profile_image': customer.profile_image,
    #         'phone_number': customer.phone_number,
    #         'home_airport': customer.home_airport
    # }
    # uid = request.META["HTTP_AUTHORIZATION"]
    airport = Airport.objects.get(pk=request.data["homeAirport"])
        
    customer = Customer.objects.create(
        uid = request.data['uid'],
        first_name = request.data['firstName'],
        last_name = request.data['lastName'],
        email = request.data['email'],
        phone_number = request.data['phoneNumber'],
        profile_image = request.data['profileImage'],
        home_airport = airport,
        )
    
    data = {
        'id': customer.id,
        'uid': customer.uid,
        'first_name': customer.first_name,
        'last_name': customer.last_name,
        'email': customer.email,
        'phone_number': customer.phone_number,
        'profile_image': customer.profile_image,
        'home_airport': customer.home_airport
    }
    
    return Response(data)
        
    # serializer = CustomerSerializer(customer)
    # serializer.is_valid(raise_exception=True)
    # serializer.save(uid=uid)
    # return Response(serializer.data, status=status.HTTP_201_CREATED)
