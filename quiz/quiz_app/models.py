from django.db import models

# Create your models here.
class quizDB(models.Model):
    question = models.CharField(max_length = 250)
    option1 = models.CharField(max_length = 25)
    option2 = models.CharField(max_length = 25)
    option3 = models.CharField(max_length = 25)
    option4 = models.CharField(max_length = 25)
    answer = models.CharField(max_length = 25)
    class Meta:
        db_table = "quest"


