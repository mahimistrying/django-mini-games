from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from .models import Game, GameSession
import json

def home(request):
    games = Game.objects.filter(is_active=True)
    return render(request, 'games/home.html', {'games': games})

def game_list(request):
    games = Game.objects.filter(is_active=True)
    return render(request, 'games/game_list.html', {'games': games})

def tic_tac_toe(request):
    game = get_object_or_404(Game, name="Tic Tac Toe")
    return render(request, 'games/tic_tac_toe.html', {'game': game})

def rock_paper_scissors(request):
    game = get_object_or_404(Game, name="Rock Paper Scissors")
    return render(request, 'games/rock_paper_scissors.html', {'game': game})

def number_guessing(request):
    game = get_object_or_404(Game, name="Number Guessing Game")
    return render(request, 'games/number_guessing.html', {'game': game})

def snake(request):
    game = get_object_or_404(Game, name="Snake")
    return render(request, 'games/snake.html', {'game': game})

@csrf_exempt
@login_required
def save_game_score(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        game_name = data.get('game_name')
        score = data.get('score', 0)
        
        try:
            game = Game.objects.get(name=game_name)
            game_session = GameSession.objects.create(
                user=request.user,
                game=game,
                score=score,
                completed=True
            )
            return JsonResponse({'success': True, 'session_id': game_session.id})
        except Game.DoesNotExist:
            return JsonResponse({'success': False, 'error': 'Game not found'})
    
    return JsonResponse({'success': False, 'error': 'Invalid request'})
