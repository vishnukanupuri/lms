from django.db import models

# Create your models here.

class Exams(models.Model):
    exam_id=models.CharField(max_length=200)
    exam_name=models.CharField(max_length=200)



class Question(models.Model):
    exam = models.ForeignKey(Exams, on_delete=models.CASCADE)
    que_id=models.CharField(max_length=200)
    que_content=models.TextField()
    ansid=models.CharField(max_length=200)


class Answer(models.Model):
    que = models.ForeignKey(Question, on_delete=models.CASCADE)
    ans_content=models.CharField(max_length=200)
    ans_id=models.CharField(max_length=200)




