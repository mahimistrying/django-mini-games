from django.core.management.base import BaseCommand
from games.models import Game

class Command(BaseCommand):
    help = 'Creates initial games in the database'

    def handle(self, *args, **options):
        games_data = [
            {
                'name': 'Tic Tac Toe',
                'description': 'Classic 3x3 grid game where you try to get three in a row. Play against yourself or challenge a friend!'
            },
            {
                'name': 'Rock Paper Scissors',
                'description': 'Classic hand game! Choose rock, paper, or scissors and try to beat the computer.'
            },
            {
                'name': 'Number Guessing Game',
                'description': 'I\'m thinking of a number... Can you guess it? Choose your difficulty level and see how few attempts you need!'
            },
            {
                'name': 'Snake',
                'description': 'Classic arcade game! Control the snake to eat food and grow longer. Don\'t hit the walls or yourself!'
            },
            {
                'name': 'Memory Game',
                'description': 'Test your memory! Flip cards to find matching pairs. Complete all matches with the fewest moves possible!'
            },
        ]

        for game_data in games_data:
            game, created = Game.objects.get_or_create(
                name=game_data['name'],
                defaults={'description': game_data['description']}
            )
            if created:
                self.stdout.write(
                    self.style.SUCCESS(f'Successfully created game: {game.name}')
                )
            else:
                self.stdout.write(
                    self.style.WARNING(f'Game already exists: {game.name}')
                )