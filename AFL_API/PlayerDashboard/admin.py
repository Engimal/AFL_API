from django.contrib import admin
from .models import *
# Register your models here.

for m in [PlayerStats, Venue, Round, ScoreBoard, Team, Player, ScoringEvent, ScoreWorm, Score, PlayerScore, APIData, APIHeaderField, API, Match, PlayerGameStats]:
    admin.site.register(m)