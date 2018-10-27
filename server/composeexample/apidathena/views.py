from django.shortcuts import render
from django.http import HttpResponse
import json

from rest_framework import generics
from .models import Confidentiality
from .serializers import ConfidentialitySerializer

# Create your views here.
def index(request):
    return HttpResponse("Hey there, you're on the apidathena !")

class ListConfidentialityView(generics.ListAPIView):
    """
    Provides a get method handler.
    """
    queryset = Confidentiality.objects.all()
    serializer_class = ConfidentialitySerializer

def init(request):
    # Read the JSON
    confidentiality_data = json.load(open('/code/composeexample/apidathena/data/confidentiality_data.json'))

    len_data = 0
    # Create a Django model object for each object in the JSON 
    for confidentiality in confidentiality_data:
        Confidentiality.objects.create(name=confidentiality['name'], total_docs=confidentiality['total_docs'])
        len_data += 1

    # No replicated data
    Confidentiality.objects.filter(id__gt=len_data).delete()

    return HttpResponse("New rows created in Confidentiality with %i elements"%len_data)


