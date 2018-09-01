from django.urls import path
from .views import ProfileListView, ProfileDetailView, ProfileDetailApiView

profiles_patterns = ([
    path('', ProfileListView.as_view(), name='list'),
    path('<username>/', ProfileDetailView.as_view(), name='detail'),
    path('api/<dni>/', ProfileDetailApiView, name='detailApi'),
    
], "profiles")
