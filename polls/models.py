from django.db import models


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    type = models.BooleanField(default=True);

class Answer(models.Model):
    question = models.ForeignKey(Question,on_delete=models.CASCADE)
    userAnswer = models.CharField(default="Empty Answer", max_length=100)


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)