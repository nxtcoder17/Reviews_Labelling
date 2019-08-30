from django.db import models

# Create your models here.
class Review (models.Model):
    review_text = models.CharField (max_length=10000)
    sentiment = models.IntegerField (default = 100);

    def repr_sentiment (self):
        if (self.sentiment == 100):
            return "Not-Assigned"
        if (self.sentiment == 1):
            return "POSITIVE (+ve)"
        elif (self.sentiment == 0):
            return "NEUTRAL (0)"
        elif (self.sentiment == -1):
            return "NEGATIVE (-ve)"

    def is_valid (self):
        return self.sentiment == 100

    def __str__ (self):
        return f"REVIEW: {self.review_text}\nSENTIMENT: {self.repr_sentiment()}"
