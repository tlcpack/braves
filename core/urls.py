from django.urls import path
from . import views
from .views import line_chart, line_chart_json

urlpatterns = [
    path('', line_chart, name='index'),
    path('chartJSON', line_chart_json, name='line_chart_json'),
]