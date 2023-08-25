from django.db import models

from education.models.question import Question

class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)

    text = models.CharField(max_length=255)

    # For multiple choice questions
    is_correct = models.BooleanField(default=False)

    # For matching questions
    match = models.PositiveIntegerField(null=True, blank=True, help_text='The answer to match with')
