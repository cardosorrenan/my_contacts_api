from my_contacts.viewsets import PersonViewset, PhoneViewset
from rest_framework import routers

router = routers.DefaultRouter()
router.register('persons', PersonViewset)
router.register('phones', PhoneViewset)