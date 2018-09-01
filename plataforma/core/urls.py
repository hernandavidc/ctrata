from django.urls import path
from .views import HomePageView, MapPageView, CasosListView, PregApiList, PerfilVictimaApiPost, AntecedentesApiGet #, SampleView

urlpatterns = [
    path('', HomePageView.as_view(), name="home"),
    path('api/preguntas/<str:motivo>', PregApiList, name="preg"),
    path('casos-reales/', CasosListView.as_view(), name="casos_reales"),
    path('api/antecedentes/<int:cc>/', AntecedentesApiGet, name="ant_api"),
    path('api/save/perfil-victima/', PerfilVictimaApiPost, name="Perfil victima"),
    path('mapa/', MapPageView.as_view(), name="Map"),
    #path('sample/', SampleView.as_view(), name="sample"),
]