from django.db import models
from django.contrib.auth.models import User

class Game(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class GameSession(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    score = models.IntegerField(default=0)
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    completed_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.user.username if self.user else 'Anonymous'} - {self.game.name} - {self.score}"
