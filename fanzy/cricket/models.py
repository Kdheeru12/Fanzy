from django.db import models

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

    def __str__(self):
        return f'{self.player} =>({self.match})'

