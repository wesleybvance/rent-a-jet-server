from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework import status
from rentajetapi.models import Customer

class CustomerView(ViewSet):
    def retrieve(self, request, pk):
        """Handle GET requests for a single customer"""
        
        customer
