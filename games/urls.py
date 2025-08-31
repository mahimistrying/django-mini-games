from django.urls import path
from . import views

app_name = 'games'

urlpatterns = [
    path('', views.game_list, name='list'),
    path('tic-tac-toe/', views.tic_tac_toe, name='tic_tac_toe'),
    path('rock-paper-scissors/', views.rock_paper_scissors, name='rock_paper_scissors'),
    path('number-guessing/', views.number_guessing, name='number_guessing'),
    path('snake/', views.snake, name='snake'),
    path('save-score/', views.save_game_score, name='save_score'),
]