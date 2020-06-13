from rest_framework import serializers
from .models import StudentI


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentI
        fields = ('id','created_at', 'updated_at', 'name', 'age', 'roll_number')

