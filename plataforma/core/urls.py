from django.urls import path
from .views import HomePageView, MapPageView, PregApiList, PerfilVictimaApiPost #, SampleView

urlpatterns = [
    path('', HomePageView.as_view(), name="home"),
    path('api/preguntas/<str:motivo>', PregApiList, name="preg"),
    path('api/save/perfil-victima/', PerfilVictimaApiPost, name="Perfil victima"),
    path('mapa/', MapPageView.as_view(), name="Map"),
    #path('sample/', SampleView.as_view(), name="sample"),
]