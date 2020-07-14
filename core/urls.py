from django.urls import path
from . import views

app_name = 'core'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    path('<int:q_id>/vote/', views.vote, name='vote'),
    path('stats', views.stats, name='stats'),
    path('players', views.PlayerView.as_view(), name='players'),
    path('player/<int:pk>', views.player, name='player')
]