from rest_framework import viewsets
from .models import Person, Phone
from .serializers import PersonSerializer, PhoneSerializer


class PersonViewset(viewsets.ModelViewSet):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer


class PhoneViewset(viewsets.ModelViewSet):
    queryset = Phone.objects.all()
    serializer_class = PhoneSerializer