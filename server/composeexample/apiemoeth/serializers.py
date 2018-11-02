from rest_framework import serializers
from .models import Confidentiality, Language, Doctype


class ConfidentialitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Confidentiality
        fields = ("id", "name", "total_docs")

class LanguageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Language
        fields = ("id", "short_name", "name", "total_docs")

class DoctypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctype
        fields = ("id", "name", "total_docs")