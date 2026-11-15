import datetime
 
from django.db import models
from django.utils import timezone
 
 
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")
 
    def __str__(self):
        return self.question_text
 
    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now
 
 
class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
 
    def __str__(self):
        return self.choice_text

class Feedback(models.Model):
    # Link it to the Choice selected (or use Question if it's per poll instead of per choice)
    choice = models.ForeignKey(Choice, on_delete=models.CASCADE, null=True, blank=True)
    feedback_text = models.CharField(max_length=500)
     
    def __str__(self):
        # Return a clean string representation (e.g., first 50 characters of feedback)
        return self.feedback_text[:50]    