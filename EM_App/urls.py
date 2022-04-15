from django.urls import path
from . import views

urlpatterns=[
    path('/',views.homepage),
    path('/Mathematics1/',views.Mathematics1),
    path('/Mathematics2/',views.Mathematics2),
    path('/Mathematics3/',views.Mathematics3)
]