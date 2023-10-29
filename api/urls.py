from rest_framework import routers
from unicodedata import name
from api.views import * 


router = routers.DefaultRouter()
router.register(r'user', UserViewSet, basename='user')
urlpatterns = router.urls
