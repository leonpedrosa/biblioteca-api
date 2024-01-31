from rest_framework import routers
from unicodedata import name
from api.views import *


router = routers.DefaultRouter()
router.register(r'user', UserViewSet, basename='user')
# router.register(r'log', LogViewSet, basename='log')
# router.register(r'rent', RentViewSet, basename='rent')
urlpatterns = router.urls
