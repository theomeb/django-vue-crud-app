from rest_framework import serializers
from .models import Confidentiality


class ConfidentialitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Confidentiality
        fields = ("id", "name", "total_docs")