from django.db import models
from django.utils import timezone
import datetime

# Create your models here.
class Question(models.Model):
	question_text = models.CharField(max_length=200)
	pub_data= models.DateTimeField('date published')

	def __str__(self):
		return self.question_text

	def was_published_recently(self):
		return self.pub_data >= timezone.now() - datetime.timedelta(days=1)
		# check if it's the last 24 hours

	was_published_recently.short_description = 'Published in last 24 hours?'
	was_published_recently.boolean = True

class Choice(models.Model):
	question = models.ForeignKey(Question, on_delete=models.CASCADE)
	# neu minh delete question, no se delete toan bo cai gi lien quan den no
	choice_text = models.CharField(max_length=200)
	votes = models.IntegerField(default=0)

	def __str__(self):
		return self.choice_text