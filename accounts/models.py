from django.db import models
from django.contrib.auth.models import User

class userprofile(models.Model):
    gender_choices=[
        ('male','male'),
        ('female','female'),
        ('other','other'),
    ]
    activity_choices=[
        ('sedementary','sedementary'),
        ('light','light activity'),
        ('moderate','moderate activity'),
        ('active','very active')
    ]

    goal_choices=[
        ('weight_gain','weight_gain'),
        ('weight_loss','weight_loss'),
        ('maintain','maintain')
    ]

    user =models.OneToOneField(User,on_delete=models.CASCADE)
    age=models.PositiveIntegerField()
    gender=models.CharField(max_length=10,choices=gender_choices)
    height=models.FloatField(help_text="height in cm")
    weight=models.FloatField(help_text="weight in kg")
    activity_level=models.CharField(max_length=50,choices=activity_choices)
    fitness_goal = models.CharField(
        max_length=20,
        choices=goal_choices,
        default='maintenance'
    )

    def __str__(self):
        return self.user.username


