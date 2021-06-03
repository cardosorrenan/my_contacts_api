from .models import Person, Phone
from rest_framework import serializers


class PersonSerializer(serializers.HyperlinkedModelSerializer):
    phones = serializers.StringRelatedField(many=True, read_only=True)

    class Meta:
        model = Person
        fields = ['id', 'name', 'favorite', 'phones', 'created_at', 'updated_at']


class PhoneSerializer(serializers.HyperlinkedModelSerializer):
    person = serializers.PrimaryKeyRelatedField(queryset=Person.objects.all())

    class Meta:
        model = Phone
        fields = ['id', 'number', 'person', 'created_at', 'updated_at']