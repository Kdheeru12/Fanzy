from django.db import models
from django.db.models.signals import post_save,post_delete
from django.dispatch import receiver


# Create your models here.
class Teams(models.Model):
    name = models.CharField(max_length=300)
    logo = models.ImageField(blank=True, null=True)
    
    def __str__(self):
        return self.name

class Player(models.Model):
    name = models.CharField(max_length=300)
    image = models.ImageField(blank=True, null=True)
    team = models.ForeignKey(Teams,on_delete=models.CASCADE)
    foreignplayer = models.BooleanField(default=False)
    price = models.IntegerField(default=0)
    fantasypoints = models.FloatField(default=0)
    runs = models.IntegerField(default=0)
    balls_faced = models.IntegerField(default=0)
    fours = models.IntegerField(default=0)
    sixes = models.IntegerField(default=0)
    catches = models.IntegerField(default=0)
    runouts = models.IntegerField(default=0)
    overs = models.IntegerField(default=0)
    runs_given = models.IntegerField(default=0)
    dots = models.IntegerField(default=0)

    def __str__(self):
        return self.name

class Matches(models.Model):
    team1 = models.ForeignKey(Teams,on_delete=models.CASCADE)
    team1_total = models.IntegerField(default=0)
    team2 = models.ForeignKey(Teams,related_name='Team2',on_delete=models.CASCADE)
    team2_total = models.IntegerField(default=0)
    date = models.DateField()

    def __str__(self):
        return f'{self.team1} vs {self.team2}'

class MatchPlayers(models.Model):
    match = models.ForeignKey(Matches,on_delete=models.CASCADE)
    player= models.ForeignKey(Player,on_delete=models.CASCADE)

    fantasypoints = models.FloatField(default=0)
    runs = models.IntegerField(default=0)
    balls_faced = models.IntegerField(default=0)
    fours = models.IntegerField(default=0)
    sixes = models.IntegerField(default=0)
    catches = models.IntegerField(default=0)
    runouts = models.IntegerField(default=0)
    overs = models.IntegerField(default=0)
    runs_given = models.IntegerField(default=0)
    dots = models.IntegerField(default=0)
    batted = models.BooleanField(default=False)

    class Meta:
        unique_together = ['match', 'player']



    def __str__(self):
        return f'{self.player} =>({self.match})'
    @property
    def total_fours(self):
        matches = self.player.matchplayers_set.all()
        fours = sum([player.fours for player in matches])
        return fours
    @property
    def total_sixes(self):
        matches = self.player.matchplayers_set.all()
        sixes = sum([player.sixes for player in matches])
        return sixes
    @property
    def total_balls_faced(self):
        matches = self.player.matchplayers_set.all()
        balls_faced = sum([player.balls_faced for player in matches])
        return balls_faced
    @property
    def total_catches(self):
        matches = self.player.matchplayers_set.all()
        catches = sum([player.catches for player in matches])
        return catches
    @property
    def total_runouts(self):
        matches = self.player.matchplayers_set.all()
        runouts = sum([player.runouts for player in matches])
        return runouts
    @property
    def total_overs(self):
        matches = self.player.matchplayers_set.all()
        overs = sum([player.overs for player in matches])
        return overs
    @property
    def total_runs_given(self):
        matches = self.player.matchplayers_set.all()
        runs_given = sum([player.runs_given for player in matches])
        return runs_given
    @property
    def total_dots(self):
        matches = self.player.matchplayers_set.all()
        dots = sum([player.dots for player in matches])
        return dots   
    @property
    def total_runs(self):
        matches = self.player.matchplayers_set.all()
        runs = sum([player.runs for player in matches])
        return runs
    @property        
    def match_strike_rate(self):
        return str(self.total_runs/self.total_balls_faced)
    @property
    def match_economy(self):
        return str(self.total_runs_given/self.total_overs)

@receiver([post_save, post_delete], sender=MatchPlayers)
def Players_signal(sender,instance,*args,**kwargs):
    print(instance.total_runs)
    player = instance.player
    player.runs = instance.total_runs
    player.balls_faced = instance.total_balls_faced
    player.fours = instance.total_fours
    player.sixes = instance.total_sixes
    player.catches = instance.total_catches
    player.runouts =instance.total_runouts
    player.overs = instance.total_overs
    player.runs_given = instance.total_runs_given
    player.dots = instance.total_dots
    player.save()

# post_save.connect(Players_signal,sender=MatchPlayers)
