from django.shortcuts import render
from django.http import HttpResponse
import json

from rest_framework import generics
from .models import Confidentiality, Language, Doctype
from .serializers import ConfidentialitySerializer, LanguageSerializer, DoctypeSerializer

# Main endpoint
def index(request):
    name = request.GET.get('name', 'buddy')
    return HttpResponse("Hey there "+name+", you're on the apidathena ! Get your data on /confidentiality, /languages and /doctype routes.")

class ListConfidentialityView(generics.ListAPIView):
    """
    Provides a get method handler.
    """
    queryset = Confidentiality.objects.all()
    serializer_class = ConfidentialitySerializer

class ListLanguageView(generics.ListAPIView):
    """
    Provides a get method handler.
    """
    queryset = Language.objects.all()
    serializer_class = LanguageSerializer

class ListDoctypeView(generics.ListAPIView):
    """
    Provides a get method handler.
    """
    queryset = Doctype.objects.all()
    serializer_class = DoctypeSerializer

def initTable(table, file):
    # Read the JSON
    data = json.load(open('/code/composeexample/apidathena/data/'+file))
    # Clear tables
    table.objects.all().delete()
    # Create a Django model object for each object in the JSON 
    if table == Language: 
        for row in data:
            table.objects.create(short_name=row['short_name'], name=row['name'], total_docs=row['total_docs'])
    else: 
        for row in data:
            table.objects.create(name=row['name'], total_docs=row['total_docs'])

    return len(data)

def init(request):
    len_data_confidentiality = initTable(Confidentiality, 'confidentiality_data.json')
    len_data_language = initTable(Language, 'language_data.json')
    len_data_doctype = initTable(Doctype, 'doctype_data.json')

    response = "Table initialized with %i rows in Confidentiality, %i rows in Language and %i rows in Doctype."%(len_data_confidentiality, len_data_language, len_data_doctype)
    return HttpResponse(response)


