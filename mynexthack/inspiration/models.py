from django.db import models
from django.contrib.contenttypes import generic
import random, string

class Idea(models.Model):
	sender = models.ForeignKey('auth.User', related_name = 'sent_ideas')
	recipient = models.ForeignKey('auth.User', related_name = 'received_ideas')
	slug = models.CharField(max_length = 10, unique = True)
	title = models.CharField(max_length = 100)
	description = models.TextField(null = True, blank = True)
	sent = models.DateTimeField(auto_now_add = True)
	used = models.BooleanField()
	comments = generic.GenericRelation('comments.Comment')
	
	def __unicode__(self):
		return self.title
	
	@models.permalink
	def get_absolute_url(self):
		return ('idea', [self.recipient.username, self.slug])
	
	def save(self, *args, **kwargs):
		if not self.slug:
			while True:
				self.slug = u''.join(random.sample(string.digits + string.letters, 10))
				if not Idea.objects.filter(slug = self.slug).exists():
					break
		
		super(Idea, self).save(*args, **kwargs)
	
	class Meta:
		ordering = ('-sent',)
		get_latest_by = 'sent'

class Vote(models.Model):
	idea = models.ForeignKey(Idea, related_name = 'votes')
	voter = models.ForeignKey('auth.User', related_name = 'votes')
	value = models.IntegerField(
		choices = (
			(-1, u'up'),
			(1, u'down')
		)
	)