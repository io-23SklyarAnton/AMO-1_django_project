from django.urls import path, re_path
from . import views

app_name = 'algorithm'

urlpatterns = [
    path('', views.home, name='home'),
    re_path('(?P<algorithm>linear|branches|cyclic)/', views.AlgorithmView.as_view(), name="algorithm"),
]
