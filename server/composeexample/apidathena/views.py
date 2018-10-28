from django.shortcuts import render
from django.http import HttpResponse
import json

from rest_framework import generics
from .models import Confidentiality, Language, Doctype
from .serializers import ConfidentialitySerializer, LanguageSerializer, DoctypeSerializer

# Main endpoint
def index(request):
    name = request.GET.get('name', 'buddy')
    return HttpResponse("<center><h2>Hey there "+name+"!</h2> <p>You're on the apidathena ! Get your data on <b>/confidentiality, /languages</b> and <b>/doctype</b> routes.</p><p>Wann to manage the API ? Execute <i>python manage.py createsuperuser --email admin@example.com --username admin</i> in your docker and go on <b>/admin</b> with your credentials.</p></center>")

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

#For actions
table_mapping = {'language': Language, 'doctype': Doctype, 'confidentiality': Confidentiality}

def delete(request):
    table_param = request.GET.get('table', '')
    name_param = request.GET.get('name', '')

    if table_param in table_mapping:
        (table_mapping[table_param]).objects.filter(name=name_param).delete()
        response = "Item with name %s in table %s deleted."%(name_param, table_param.upper())
        return HttpResponse(response)

    return HttpResponse("Bad params to delete the item !")

def create(request):
    table_param = request.GET.get('table', '')
    name_param = request.GET.get('name', '')
    total_docs_param = request.GET.get('total_docs', '')

    if table_param in table_mapping:
        if table_param=='language':
            short_name_param = request.GET.get('short_name', '')
            Language.objects.create(short_name=short_name_param ,name=name_param, total_docs=total_docs_param)
        else :
            (table_mapping[table_param]).objects.create(name=name_param, total_docs=total_docs_param)
        response = "Item with name %s in table %s created."%(name_param.upper(), table_param.upper())
        return HttpResponse(response)

    return HttpResponse("Bad params to create the item !")

def edit(request):
    table_param = request.GET.get('table', '')
    name_to_changed_param = request.GET.get('name_to_changed', '')
    name_param = request.GET.get('name', '')
    total_docs_param = request.GET.get('total_docs', '')

    if table_param in table_mapping:
        if table_param=='language':
            short_name_param = request.GET.get('short_name', '')
            Language.objects.filter(name=name_to_changed_param).update(short_name=short_name_param ,name=name_param, total_docs=total_docs_param)
        else :
            (table_mapping[table_param]).objects.filter(name=name_to_changed_param).update(name=name_param, total_docs=(total_docs_param))
        response = "Item with name %s in table %s edited."%(name_param.upper(), table_param.upper())
        return HttpResponse(response)

    return HttpResponse("Bad params to edit the item !")
