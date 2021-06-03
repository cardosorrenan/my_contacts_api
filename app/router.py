from my_contacts.viewsets import PersonViewset
from rest_framework import routers

router = routers.DefaultRouter()
router.register('person', PersonViewset)