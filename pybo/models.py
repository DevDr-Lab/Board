from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.
"""
질문모델: subject, content, create_date
답변모델: question, content, create_date
"""

class Question(models.Model):
    subject = models.CharField(max_length=200)
    content = models.TextField()
    create_date = models.DateTimeField()

    def __str__(self): # Object 1 이렇게 반환되는게 아니라 subject가 바로 나오도록 magic method 구현
        return self.subject


class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete = models.CASCADE)
    content = models.TextField()
    create_date = models.DateTimeField()


