import datetime

from django.db import models
from django.urls import reverse
from django.utils import timezone

# Create your models here.
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.question_text    

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text
    
class Player(models.Model):
    name = models.CharField(max_length=300)
    season = models.CharField(blank=True, max_length=5)
    position = models.CharField(blank=True, max_length=5)
    games = models.CharField(blank=True, max_length=5)
    era = models.CharField(blank=True, max_length=10)
    wins = models.CharField(blank=True, max_length=5)
    whip = models.CharField(blank=True, max_length=10)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('player_detail', args=[str(self.id)])
    

class Year(models.Model):
    season = models.CharField(max_length=6)
    players = models.ManyToManyField(Player)

    def __str__(self):
        return self.year
    