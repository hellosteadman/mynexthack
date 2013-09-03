from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes import generic
from django.contrib.sites.models import Site
from django.conf import settings
from bambu.mail.shortcuts import render_to_mail
import requests, logging

class Comment(models.Model):
	sender = models.ForeignKey('auth.User', related_name = 'comments')
	sent = models.DateTimeField(auto_now_add = True, db_index = True)
	body = models.TextField()
	content_type = models.ForeignKey(ContentType)
	object_id = models.PositiveIntegerField(db_index = True)
	content_object = generic.GenericForeignKey()
	
	def __unicode__(self):
		return u'Re: %s' % unicode(self.content_object)
	
	def get_absolute_url(self):
		return self.content_object.get_absolute_url() + '#comment-%d' % self.pk
	
	def save(self, *args, **kwargs):
		notify = kwargs.pop('notify', True)
		new = not self.pk
		
		super(Comment, self).save(*args, **kwargs)
	
	class Meta:
		ordering = ('-sent',)
		get_latest_by = 'sent'