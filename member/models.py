from django.db import models

# Create your models here.

class Member(models.Model):
    firstname = models.CharField(max_length = 255)
    lastname = models.CharField(max_length = 255)

    def __str__(self):
        return self.firstname


# member1 = Member(firstname="Sevinch", lastname="Rahmatillayeva")
# member2 = Member(firstname="Farrux", lastname="Rahmatillayev")
# member3 = Member(firstname="Anvar", lastname="Narzullayev")
# member4 = Member(firstname="Cristiano", lastname="Ronaldo")