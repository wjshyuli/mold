from django.urls import path ,include
from rest_framework.routers import DefaultRouter
from .views import Specification,WeekCard,MoldStatus,StopStatus,StopReport,StockViewSet,StockCorViewSet,stock_show

router = DefaultRouter()
router.register("stock_base", StockViewSet)
router.register("stock_Cor", StockCorViewSet)


urlpatterns = [
    path("specification", Specification.as_view()),
    path("weekcard", WeekCard.as_view()),
    path("mold_status", MoldStatus.as_view()),
    path("stop_status", StopStatus.as_view()),
    path("stop_report", StopReport.as_view()),
    path("", include(router.urls)),
    path("stock_show/", stock_show),

]