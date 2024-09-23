from django.urls import path
from . import views

urlpatterns = [
    path('', views.tic_tac_toe, name='tic_tac_toe'),
    path('move/<int:row>/<int:col>/', views.tic_tac_toe_move, name='tic_tac_toe_move'),
    path('reset/', views.tic_tac_toe_reset, name='tic_tac_toe_reset'),
]
