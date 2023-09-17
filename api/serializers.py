from rest_framework import serializers
from .models import EfoTerm, EfoTermSynonym, EfoTermOntology


class EfoTermSerializer(serializers.ModelSerializer):
    class Meta:
        model = EfoTerm
        fields = '__all__'


class EfoTermSynonymSerializer(serializers.ModelSerializer):
    class Meta:
        model = EfoTermSynonym
        fields = '__all__'


class EfoTermOntologySerializer(serializers.ModelSerializer):
    class Meta:
        model = EfoTermOntology
        fields = '__all__'
