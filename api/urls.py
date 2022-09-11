from rest_framework.routers import DefaultRouter
from api.viewsets.impressorasVS import ImpressorasViewSet

app_name = 'app'
router = DefaultRouter(trailing_slash=False)

router.register(r'impressoras', ImpressorasViewSet)

urlpatterns = router.urls


