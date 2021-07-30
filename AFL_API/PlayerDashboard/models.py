from django.db import models
import requests
import json
from seleniumwire import webdriver
from selenium.webdriver.chrome.options import Options

class Venue(models.Model):
    venueId = models.CharField(max_length=50, primary_key=True)
    abbreviation = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    timezone = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Round(models.Model):
    roundId = models.CharField(max_length=50, primary_key=True)
    abbreviation = models.CharField(max_length=50)
    roundNumber = models.IntegerField()
    year = models.IntegerField()

    def __str__(self):
        return f'Round {self.roundNumber}'

class ScoreBoard(models.Model):
    behinds = models.IntegerField(default=0)
    goals = models.IntegerField(default=0)
    totalScore = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.goals}.{self.behinds}.{self.totalScore}'

class Team(models.Model):
    teamId = models.CharField(max_length=50, primary_key=True)
    abbreviation = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    nickname = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class PlayerGameStats(models.Model):
    player = models.ForeignKey('Player', on_delete=models.CASCADE)
    playerStats = models.ForeignKey('PlayerStats', on_delete=models.CASCADE)

    def __str__(self):
        return f'Game stats for {self.player}'

class PlayerStats(models.Model):
    behinds = models.FloatField(default=0.0)
    bounces = models.FloatField(default=0.0)
    centreBounceAttendances = models.FloatField(default=0.0)
    centreClearances = models.FloatField(default=0.0)
    clangers = models.FloatField(default=0.0)
    contestDefLossPercentage = models.FloatField(default=0.0)
    contestDefLosses = models.FloatField(default=0.0)
    contestDefOneOnOnes = models.FloatField(default=0.0)
    contestOffOneOnOnes = models.FloatField(default=0.0)
    contestOffWins = models.FloatField(default=0.0)
    contestOffWinsPercentage = models.FloatField(default=0.0)
    contestedMarks = models.FloatField(default=0.0)
    contestedPossessionRate = models.FloatField(default=0.0)
    contestedPossessions = models.FloatField(default=0.0)
    defHalfPressureActs = models.FloatField(default=0.0)
    disposalEfficiency = models.FloatField(default=0.0)
    disposals = models.FloatField(default=0.0)
    dreamTeamPoints = models.FloatField(default=0.0)
    effectiveDisposals = models.FloatField(default=0.0)
    effectiveKicks = models.FloatField(default=0.0)
    f50GroundBallGets = models.FloatField(default=0.0)
    freesAgainst = models.FloatField(default=0.0)
    freesFor = models.FloatField(default=0.0)
    goalAccuracy = models.FloatField(default=0.0)
    goalAssists = models.FloatField(default=0.0)
    goals = models.FloatField(default=0.0)
    groundBallGets = models.FloatField(default=0.0)
    handballs = models.FloatField(default=0.0)
    hitoutToAdvantageRate = models.FloatField(default=0.0)
    hitoutWinPercentage = models.FloatField(default=0.0)
    hitouts = models.FloatField(default=0.0)
    hitoutsToAdvantage = models.FloatField(default=0.0)
    inside50s = models.FloatField(default=0.0)
    interceptMarks = models.FloatField(default=0.0)
    intercepts = models.FloatField(default=0.0)
    kickEfficiency = models.FloatField(default=0.0)
    kickToHandballRatio = models.FloatField(default=0.0)
    kickins = models.FloatField(default=0.0)
    kickinsPlayon = models.FloatField(default=0.0)
    kicks = models.FloatField(default=0.0)
    marks = models.FloatField(default=0.0)
    marksInside50 = models.FloatField(default=0.0)
    marksOnLead = models.FloatField(default=0.0)
    matchesPlayed = models.FloatField(default=0.0)
    metresGained = models.FloatField(default=0.0)
    onePercenters = models.FloatField(default=0.0)
    pressureActs = models.FloatField(default=0.0)
    ranking = models.FloatField(default=0.0)
    ratingPoints = models.FloatField(default=0.0)
    rebound50s = models.FloatField(default=0.0)
    ruckContests = models.FloatField(default=0.0)
    scoreInvolvements = models.FloatField(default=0.0)
    scoreLaunches = models.FloatField(default=0.0)
    shotsAtGoal = models.FloatField(default=0.0)
    spoils = models.FloatField(default=0.0)
    stoppageClearances = models.FloatField(default=0.0)
    tackles = models.FloatField(default=0.0)
    tacklesInside50 = models.FloatField(default=0.0)
    timeOnGroundPercentage = models.FloatField(default=0.0)
    totalClearances = models.FloatField(default=0.0)
    totalPossessions = models.FloatField(default=0.0)
    turnovers = models.FloatField(default=0.0)
    uncontestedPossessions = models.FloatField(default=0.0)


class playerBio(models.Model):
    age= models.IntegerField(default=0)
    dateOfBirth= models.CharField(max_length=200, default='')
    debutYear= models.CharField(max_length=200, default='')
    draftPosition= models.CharField(max_length=200, default='')
    draftType= models.CharField(max_length=200, default='')
    draftYear= models.CharField(max_length=200, default='')
    givenName= models.CharField(max_length=200, default='')
    heightCm= models.IntegerField(default=0)
    jumperNumber= models.IntegerField(default=0)
    kickingFoot= models.CharField(max_length=200, default='')
    photoURL= models.CharField(max_length=200, default='')
    position= models.CharField(max_length=200, default='')
    recruitedFrom= models.CharField(max_length=200, default='')
    stateOfOrigin= models.CharField(max_length=200, default='')
    surname= models.CharField(max_length=200, default='')
    weightKg= models.IntegerField(default=0)


class Season(models.Model):
    seasonId = models.CharField(max_length=4, primary_key=True)


class Player(models.Model):
    playerId = models.CharField(max_length=50, primary_key=True)
    careerAverages = models.ForeignKey(PlayerStats, on_delete=models.CASCADE, related_name='careerAverages')
    careerTotals = models.ForeignKey(PlayerStats, on_delete=models.CASCADE, related_name='careerTotals')
    seasonAverages = models.ForeignKey(PlayerStats, on_delete=models.CASCADE, related_name='seasonAverages')
    seasonTotals = models.ForeignKey(PlayerStats, on_delete=models.CASCADE, related_name='seasonTotals')
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    bio = models.ForeignKey(playerBio, on_delete=models.CASCADE)

    matches = models.ManyToManyField('Match')



    def __str__(self):
        return f'{self.bio.givenName} {self.bio.surname}'


class PlayerScore(models.Model):
    scoreBreakdown = models.ForeignKey(ScoreBoard, on_delete=models.CASCADE)
    player = models.ForeignKey(Player, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.player} ({self.scoreBreakdown})'

class ScoringEvent(models.Model):
    aggregateAwayScore = models.IntegerField()
    aggregateHomeScore = models.IntegerField()
    homeOrAway = models.CharField(max_length=50)
    periodNumber = models.IntegerField()
    periodSeconds = models.IntegerField()
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    playerScore = models.ForeignKey(PlayerScore, on_delete=models.CASCADE)




    def __str__(self):
        return f'{self.team} scores at {round(self.periodSeconds/60,2)} min of Q{self.periodNumber}'

class ScoreWorm(models.Model):
    scoringEvents = models.ManyToManyField(ScoringEvent)

class Score(models.Model):
    awayTeamScore = models.ForeignKey(ScoreBoard, on_delete=models.CASCADE, related_name='awayTeamScore')
    homeTeamScore = models.ForeignKey(ScoreBoard, on_delete=models.CASCADE, related_name='homeTeamScore')
    scoreWorm = models.ForeignKey(ScoreWorm, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.homeTeamScore} v {self.awayTeamScore}'

class Match(models.Model):
    matchId = models.CharField(max_length=50, primary_key=True)
    abbreviation = models.CharField(max_length=50)
    awayTeam = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='awayTeam')
    homeTeam = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='homeTeam')
    date = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    round = models.ForeignKey(Round, on_delete=models.CASCADE)
    status = models.CharField(max_length=50)
    venue = models.ForeignKey(Venue, on_delete=models.CASCADE)
    score = models.ForeignKey(Score, on_delete=models.CASCADE) #added. Technicaly isn't this way in API, but makes sense I think
    players = models.ManyToManyField(PlayerGameStats, null=True, blank=True)


    def __str__(self):
        return f'{self.name} {self.round} ({self.date})'

class APIHeaderField(models.Model):
    key = models.CharField(max_length=150)
    value = models.CharField(max_length=500)

    def __str__(self):
        return f'{self.key}: {self.value}'

class APIData(models.Model):
    data = models.ManyToManyField(APIHeaderField, related_name='data')

    def __str__(self):
        to_return = '{'
        for hf in self.data.all():
            to_return += f'{hf.key}: {hf.value},'
        to_return += '}'
        return to_return

class API(models.Model):
    name = models.CharField(max_length=50) #Will have {0} fields for parameters (I think)
    description = models.CharField(max_length=150)
    url = models.CharField(max_length=300)

    request_headers = models.ForeignKey(APIData, on_delete=models.CASCADE, related_name='request_headers', blank=True, null=True)
    request_data = models.ForeignKey(APIData, on_delete=models.CASCADE, related_name='request_data', blank=True, null=True)

    def __str__(self):
        return self.name

    def create_obj_from_dict(self, obj_type, dictionary):
        id_data = None
        for ss in list(dictionary):
            if ss[-2:] == 'Id' and type(dictionary[ss]) not in [list, dict]:
                id_data = {ss:dictionary[ss]}
        try:
            #print(f'Updating {obj_type}')
            x = obj_type.objects.get(**id_data)
        except:
            #print(f'New {obj_type}')
            x = obj_type()
        for key, value in dictionary.items():
            if hasattr(x, key) and type(value) not in [list, dict] and value != None:
                setattr(x, key, value)
        return x

    def process_afl_round(self, input_data):
        player_data = input_data['players']
        rid = input_data['search']['context']['identifier']
        for player in player_data:
            pid = player['playerId']
            tid = player['team']['teamId']
            extracted_player = Player.objects.get(playerId=pid)

            try:
                extracted_match = Match.objects.get(round=rid, awayTeam=tid)

            except:
                extracted_match = Match.objects.get(round=rid, homeTeam=tid)

            stats = self.create_obj_from_dict(PlayerStats, player['totals'])
            stats.save()

            my_player_game_stats = PlayerGameStats(player=extracted_player, playerStats=stats)
            my_player_game_stats.save()

            extracted_match.players.add(my_player_game_stats)
            extracted_match.save()




    def process_afl_season(self, input_data):

        player_data = input_data['players']
        #print(player_data[0])
        for player in player_data:
            my_current_player = self.create_obj_from_dict(Player, player)
            totals_data = player['totals']
            averages_data = player['averages']
            playerdetails_data = player['playerDetails']
            my_totals = self.create_obj_from_dict(PlayerStats, totals_data)
            my_averages = self.create_obj_from_dict(PlayerStats, averages_data)
            my_details = self.create_obj_from_dict(playerBio, playerdetails_data)
            #print(playerdetails_data)
            #print(my_details.debutYear)
            my_totals.save()
            my_averages.save()
            my_details.save()

            my_current_player.seasonTotals = my_totals
            my_current_player.seasonAverages = my_averages
            my_current_player.careerTotals = my_totals
            my_current_player.careerAverages = my_averages
            my_current_player.bio = my_details

            team = player['team']
            team_data = {}
            team_data['name'] = team['teamName']
            team_data['abbreviation'] = team['teamAbbr']
            team_data['nickname'] = team['teamNickname']
            team_data['teamId'] = team['teamId']

            my_team = self.create_obj_from_dict(Team, team_data)
            my_team.save()

            my_current_player.team = my_team



            my_current_player.save()

        #TODO: update player model
        #todo: create players

    def process_afl_match(self, input_data):
        player_list = []
        match_data = input_data['match']
        venue_data = input_data['venue']
        round_data = input_data['round']
        video_data = input_data['liveVideos']
        score_data = input_data['score']

        home_team_data = match_data['homeTeam']
        away_team_data = match_data['awayTeam']
        my_home_team = self.create_obj_from_dict(Team, home_team_data)
        my_away_team = self.create_obj_from_dict(Team, away_team_data)

        my_venue = self.create_obj_from_dict(Venue, venue_data)
        my_round = self.create_obj_from_dict(Round, round_data)

        my_venue.save()
        my_round.save()
        my_home_team.save()
        my_away_team.save()

        #ROUND

        scoreworm_data = score_data['scoreWorm']
        my_scoreworm = ScoreWorm()
        my_scoreworm.save()
        score_breakdown_dict = {}
        score_breakdown_tracker = 1

        fake_team = Team()
        fake_team.save()
        for scoringEvent in scoreworm_data['scoringEvents']:


            extracted_team = Team.objects.get(teamId=scoringEvent['teamId'])

            player_score_data = scoringEvent['playerScore']

            if player_score_data != None:

                    score_breakdown_data = player_score_data['scoreBreakdown']
                    #player_data = player_score_data['player']  # Foreign Key

                    my_current_score_breakdown = self.create_obj_from_dict(ScoreBoard, score_breakdown_data)
                    my_current_score_breakdown.save()
                    player_id = player_score_data['player']['playerId']
                    extracted_player = Player.objects.get(playerId=player_id)
                    player_list.append(extracted_player)
            else:
                #Won't happen when scoreType is RUSHED_BEHIND
                fakePlayerStats = PlayerStats()
                fakePlayerStats.save()
                fakeBio = playerBio()
                fakeBio.save()
                extracted_player = Player(careerAverages=fakePlayerStats, careerTotals=fakePlayerStats,
                                           seasonAverages=fakePlayerStats, seasonTotals=fakePlayerStats, team=extracted_team, bio=fakeBio)
                extracted_player.save()

                my_current_score_breakdown = ScoreBoard()
                my_current_score_breakdown.save()




            my_player_score = PlayerScore(player=extracted_player, scoreBreakdown=my_current_score_breakdown)
            my_player_score.save()







            my_player_score.scoreBreakdown = my_current_score_breakdown
            my_player_score.player = extracted_player

            my_scoring_event = self.create_obj_from_dict(ScoringEvent, scoringEvent)
            my_scoring_event.playerScore = my_player_score
            my_scoring_event.team = extracted_team
            my_scoring_event.save()

            my_scoring_event.playerScore = my_player_score

            team_id = scoringEvent['teamId']

            my_scoring_event.team = fake_team #TODO: Fix. Must be a real team

            my_scoreworm.scoringEvents.add(my_scoring_event)




        home_team_score_data = score_data['homeTeamScore']['matchScore']
        away_team_score_data = score_data['awayTeamScore']['matchScore']

        my_home_team_scoreboard = self.create_obj_from_dict(ScoreBoard, home_team_score_data)
        my_away_team_scoreboard = self.create_obj_from_dict(ScoreBoard, away_team_score_data)


        my_home_team_scoreboard.save()
        my_away_team_scoreboard.save()

        my_score = self.create_obj_from_dict(Score, {'awayTeamScore':my_away_team_scoreboard, 'homeTeamScore':my_home_team_scoreboard,'scoreWorm':my_scoreworm})
        my_score.homeTeamScore = my_away_team_scoreboard
        my_score.awayTeamScore = my_home_team_scoreboard
        my_score.scoreWorm = my_scoreworm


        my_score.save()

        my_match = self.create_obj_from_dict(Match, match_data)
        my_match.venue = my_venue
        my_match.round = my_round
        my_match.homeTeam = my_home_team
        my_match.awayTeam = my_away_team
        my_match.score = my_score
        my_match.save()

        for p in player_list:
            if p.team.teamId in [my_match.homeTeam.teamId, my_match.awayTeam.teamId]:
                p.matches.add(my_match)
                p.save()

        return True

    def generate_afl_website_token(self):
        chrome_options = Options()
        #chrome_options.add_argument("--headless")
        driver = webdriver.Chrome(options=chrome_options)

        url = 'https://www.afl.com.au/stats/stats-pro#/Discover/CD_I297373/Bontempelli-Marcus'
        driver.get(url)

        token = None
        for request in driver.requests:
            if request.response:
                if 'x-media-mis-token' in request.headers:
                    token = request.headers['x-media-mis-token']

        api_data_headers = self.request_headers
        for header_obj in api_data_headers.data.all():
            if header_obj.key == 'x-media-mis-token':
                header_obj.value = token
                header_obj.save()
        driver.quit()

    def make_get_request(self, var):
        formatted_url = str(self.url).format(var)

        headers = {}
        if headers != None:
            api_data_headers = self.request_headers
            for header_obj in api_data_headers.data.all():
                headers[header_obj.key] = header_obj.value



        for attempt in [1, 2]:
            request = requests.get(formatted_url, headers=headers)
            if request.status_code != 200:
                self.generate_afl_website_token()
            else:
                break

        returned_data = json.loads(request.text)

        if self.name == 'AFL Match':
            next = self.process_afl_match(returned_data)
        elif self.name == 'AFL Player Season':
            next = self.process_afl_season(returned_data)
        elif self.name == "AFL Round":
            next = self.process_afl_round(returned_data)

        return True



    def make_post_request(self, var=[]):
        formatted_url = str(self.url).format(*var)

        headers = {}
        if self.request_headers != None:
            api_data_headers = self.request_headers
            for header_obj in api_data_headers.data.all():
                headers[header_obj.key] = header_obj.value

        data = {}
        if self.request_data != None:
            api_data_data = self.request_data
            for data_obj in api_data_data.data.all():
                data[data_obj.key] = data_obj.value

        request = requests.post(formatted_url, headers=headers, data=data, verify=False)
        if request.status_code != 200:
            return {False: f'Status code is {request.status_code}'}

        returned_data = request.text
        return returned_data

    def process_request_returned_data(self, returned_data, json_type=True):
        if json_type:
            json_ = json.loads(returned_data.text)

class Service(models.Model):
    test = models.CharField(max_length=50)

    def clean_afl_data(self):
       for m in [Venue, Round, ScoreBoard, Team, PlayerStats, Player, PlayerScore,ScoringEvent, ScoreWorm, Score, Match, playerBio, PlayerGameStats]:
           m.objects.all().delete()