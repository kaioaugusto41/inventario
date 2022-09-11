from dataclasses import field
from msilib.schema import SelfReg
from rest_framework import serializers
from app.models import Impressoras

class ImpressorasSerializer(serializers.ModelSerializer):

    class Meta:
        model = Impressoras
        fields = '__all__'

        