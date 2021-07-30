# Generated by Django 3.2.5 on 2021-07-24 12:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='APIHeaderField',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('key', models.CharField(max_length=150)),
                ('value', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Player',
            fields=[
                ('playerId', models.CharField(max_length=50, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='playerBio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('aflAwards', models.CharField(max_length=200)),
                ('age', models.IntegerField()),
                ('bio', models.CharField(max_length=200)),
                ('dateOfBirth', models.CharField(max_length=200)),
                ('debutYear', models.IntegerField()),
                ('draftPosition', models.IntegerField()),
                ('draftType', models.CharField(max_length=200)),
                ('draftYear', models.CharField(max_length=200)),
                ('givenName', models.CharField(max_length=200)),
                ('heightCm', models.IntegerField()),
                ('jumperNumber', models.IntegerField()),
                ('kickingFoot', models.CharField(max_length=200)),
                ('photoURL', models.CharField(max_length=200)),
                ('position', models.CharField(max_length=200)),
                ('recruitedFrom', models.CharField(max_length=200)),
                ('stateOfOrigin', models.CharField(max_length=200)),
                ('surname', models.CharField(max_length=200)),
                ('weightKg', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='PlayerScore',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('player', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='PlayerDashboard.player')),
            ],
        ),
        migrations.CreateModel(
            name='PlayerStats',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('behinds', models.FloatField(default=0.0)),
                ('bounces', models.FloatField(default=0.0)),
                ('centreBounceAttendances', models.FloatField(default=0.0)),
                ('centreClearances', models.FloatField(default=0.0)),
                ('clangers', models.FloatField(default=0.0)),
                ('contestDefLossPercentage', models.FloatField(default=0.0)),
                ('contestDefLosses', models.FloatField(default=0.0)),
                ('contestDefOneOnOnes', models.FloatField(default=0.0)),
                ('contestOffOneOnOnes', models.FloatField(default=0.0)),
                ('contestOffWins', models.FloatField(default=0.0)),
                ('contestOffWinsPercentage', models.FloatField(default=0.0)),
                ('contestedMarks', models.FloatField(default=0.0)),
                ('contestedPossessionRate', models.FloatField(default=0.0)),
                ('contestedPossessions', models.FloatField(default=0.0)),
                ('defHalfPressureActs', models.FloatField(default=0.0)),
                ('disposalEfficiency', models.FloatField(default=0.0)),
                ('disposals', models.FloatField(default=0.0)),
                ('dreamTeamPoints', models.FloatField(default=0.0)),
                ('effectiveDisposals', models.FloatField(default=0.0)),
                ('effectiveKicks', models.FloatField(default=0.0)),
                ('f50GroundBallGets', models.FloatField(default=0.0)),
                ('freesAgainst', models.FloatField(default=0.0)),
                ('freesFor', models.FloatField(default=0.0)),
                ('goalAccuracy', models.FloatField(default=0.0)),
                ('goalAssists', models.FloatField(default=0.0)),
                ('goals', models.FloatField(default=0.0)),
                ('groundBallGets', models.FloatField(default=0.0)),
                ('handballs', models.FloatField(default=0.0)),
                ('hitoutToAdvantageRate', models.FloatField(default=0.0)),
                ('hitoutWinPercentage', models.FloatField(default=0.0)),
                ('hitouts', models.FloatField(default=0.0)),
                ('hitoutsToAdvantage', models.FloatField(default=0.0)),
                ('inside50s', models.FloatField(default=0.0)),
                ('interceptMarks', models.FloatField(default=0.0)),
                ('intercepts', models.FloatField(default=0.0)),
                ('kickEfficiency', models.FloatField(default=0.0)),
                ('kickToHandballRatio', models.FloatField(default=0.0)),
                ('kickins', models.FloatField(default=0.0)),
                ('kickinsPlayon', models.FloatField(default=0.0)),
                ('kicks', models.FloatField(default=0.0)),
                ('marks', models.FloatField(default=0.0)),
                ('marksInside50', models.FloatField(default=0.0)),
                ('marksOnLead', models.FloatField(default=0.0)),
                ('matchesPlayed', models.FloatField(default=0.0)),
                ('metresGained', models.FloatField(default=0.0)),
                ('onePercenters', models.FloatField(default=0.0)),
                ('pressureActs', models.FloatField(default=0.0)),
                ('ranking', models.FloatField(default=0.0)),
                ('ratingPoints', models.FloatField(default=0.0)),
                ('rebound50s', models.FloatField(default=0.0)),
                ('ruckContests', models.FloatField(default=0.0)),
                ('scoreInvolvements', models.FloatField(default=0.0)),
                ('scoreLaunches', models.FloatField(default=0.0)),
                ('shotsAtGoal', models.FloatField(default=0.0)),
                ('spoils', models.FloatField(default=0.0)),
                ('stoppageClearances', models.FloatField(default=0.0)),
                ('tackles', models.FloatField(default=0.0)),
                ('tacklesInside50', models.FloatField(default=0.0)),
                ('timeOnGroundPercentage', models.FloatField(default=0.0)),
                ('totalClearances', models.FloatField(default=0.0)),
                ('totalPossessions', models.FloatField(default=0.0)),
                ('turnovers', models.FloatField(default=0.0)),
                ('uncontestedPossessions', models.FloatField(default=0.0)),
            ],
        ),
        migrations.CreateModel(
            name='Round',
            fields=[
                ('roundId', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('abbreviation', models.CharField(max_length=50)),
                ('roundNumber', models.IntegerField()),
                ('year', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='ScoreBoard',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('behinds', models.IntegerField(default=0)),
                ('goals', models.IntegerField(default=0)),
                ('totalScore', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('test', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('teamId', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('abbreviation', models.CharField(max_length=50)),
                ('name', models.CharField(max_length=50)),
                ('nickname', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Venue',
            fields=[
                ('venueId', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('abbreviation', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=50)),
                ('name', models.CharField(max_length=50)),
                ('state', models.CharField(max_length=50)),
                ('timezone', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='ScoringEvent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('aggregateAwayScore', models.IntegerField()),
                ('aggregateHomeScore', models.IntegerField()),
                ('homeOrAway', models.CharField(max_length=50)),
                ('periodNumber', models.IntegerField()),
                ('periodSeconds', models.IntegerField()),
                ('playerScore', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='PlayerDashboard.playerscore')),
                ('team', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='PlayerDashboard.team')),
            ],
        ),
        migrations.CreateModel(
            name='ScoreWorm',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('scoringEvents', models.ManyToManyField(to='PlayerDashboard.ScoringEvent')),
            ],
        ),
        migrations.CreateModel(
            name='Score',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('awayTeamScore', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='awayTeamScore', to='PlayerDashboard.scoreboard')),
                ('homeTeamScore', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='homeTeamScore', to='PlayerDashboard.scoreboard')),
                ('scoreWorm', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='PlayerDashboard.scoreworm')),
            ],
        ),
        migrations.AddField(
            model_name='playerscore',
            name='scoreBreakdown',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='PlayerDashboard.scoreboard'),
        ),
        migrations.AddField(
            model_name='player',
            name='bio',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='PlayerDashboard.playerbio'),
        ),
        migrations.AddField(
            model_name='player',
            name='careerAverages',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='careerAverages', to='PlayerDashboard.playerstats'),
        ),
        migrations.AddField(
            model_name='player',
            name='careerTotals',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='careerTotals', to='PlayerDashboard.playerstats'),
        ),
        migrations.AddField(
            model_name='player',
            name='seasonAverages',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='seasonAverages', to='PlayerDashboard.playerstats'),
        ),
        migrations.AddField(
            model_name='player',
            name='seasonTotals',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='seasonTotals', to='PlayerDashboard.playerstats'),
        ),
        migrations.AddField(
            model_name='player',
            name='team',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='PlayerDashboard.team'),
        ),
        migrations.CreateModel(
            name='Match',
            fields=[
                ('matchId', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('abbreviation', models.CharField(max_length=50)),
                ('date', models.CharField(max_length=50)),
                ('name', models.CharField(max_length=50)),
                ('status', models.CharField(max_length=50)),
                ('awayTeam', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='awayTeam', to='PlayerDashboard.team')),
                ('homeTeam', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='homeTeam', to='PlayerDashboard.team')),
                ('round', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='PlayerDashboard.round')),
                ('score', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='PlayerDashboard.score')),
                ('venue', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='PlayerDashboard.venue')),
            ],
        ),
        migrations.CreateModel(
            name='APIData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.ManyToManyField(related_name='data', to='PlayerDashboard.APIHeaderField')),
            ],
        ),
        migrations.CreateModel(
            name='API',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=150)),
                ('url', models.CharField(max_length=300)),
                ('request_data', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='request_data', to='PlayerDashboard.apidata')),
                ('request_headers', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='request_headers', to='PlayerDashboard.apidata')),
            ],
        ),
    ]