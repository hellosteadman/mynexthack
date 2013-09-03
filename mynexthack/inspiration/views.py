from django.db.models import Sum
from django.template.response import TemplateResponse
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect, Http404
from django.core.urlresolvers import reverse
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.sites.models import Site
from django.contrib.contenttypes.models import ContentType
from django.conf import settings
from mynexthack.inspiration.models import Idea
from mynexthack.inspiration.forms import IdeaForm
from mynexthack.comments.models import Comment
from mynexthack.comments.forms import CommentForm
from social_auth.models import UserSocialAuth
from twitter import Twitter, OAuth

SITE = Site.objects.get_current()

@login_required
def my_ideas(request):
	return HttpResponseRedirect(
		reverse('ideas', args = [request.user.username])
	)

def ideas(request, username = None):
	if username:
		user = get_object_or_404(User, username = username)
	
	if request.user.is_authenticated():
		try:
			auth = UserSocialAuth.objects.get(provider = 'twitter', user = request.user)
		except UserSocialAuth.DoesNotExist:
			auth = None
		
		if username and auth:
			form = IdeaForm(request.POST or None,
				instance = Idea(
					sender = request.user,
					recipient = user
				)
			)
		else:
			form = None
		
		if auth and form and request.method == 'POST' and form.is_valid():
			idea = form.save()
			if request.POST.get('tweet'):
				tokens = auth.tokens
				
				Twitter(
					auth = OAuth(
						tokens['oauth_token'],
						tokens['oauth_token_secret'],
						settings.TWITTER_CONSUMER_KEY,
						settings.TWITTER_CONSUMER_SECRET
					)
				).statuses.update(
					status = '.@%s Here\'s an idea for your next hack: http://%s%s' %(
						idea.recipient.username, SITE.domain, idea.get_absolute_url()
					)
				)
			
			messages.success(request,
				u'Thanks! Your idea has been posted to %s.' % idea.recipient.first_name or idea.recipient.username
			)
			
			return HttpResponseRedirect(
				idea.get_absolute_url()
			)
	else:
		form = None
	
	qs = Idea.objects.all()
	if username:
		qs = qs.filter(recipient = user)
	
	qs = qs.annotate(
		vote_value = Sum('votes__value')
	).order_by('vote_value', '-sent')
	
	paginator = Paginator(qs, 10)
	page = request.GET.get('page')
	
	try:
		page = paginator.page(page)
	except PageNotAnInteger:
		page = paginator.page(1)
	except EmptyPage:
		page = paginator.page(paginator.num_pages)
	
	return TemplateResponse(
		request,
		'inspiration/ideas.html',
		{
			'recipient': username and user or None,
			'ideas': page,
			'form': form,
			'me': username and (request.user.is_authenticated() and request.user.pk == user.pk) or False,
			'title_parts': (username and (user.get_full_name() or user.username) or u'All ideas',)
		}
	)

def idea(request, username, slug):
	user = get_object_or_404(User, username = username)
	idea = get_object_or_404(Idea,
		slug = slug,
		recipient = user
	)
	
	if request.user.is_authenticated():
		try:
			auth = UserSocialAuth.objects.get(provider = 'twitter', user = request.user)
		except UserSocialAuth.DoesNotExist:
			auth = None
		
		form = CommentForm(request.POST or None,
			instance = Comment(
				sender = request.user,
				content_type = ContentType.objects.get_for_model(idea),
				object_id = idea.pk
			)
		)
		
		if auth and request.method == 'POST' and form.is_valid():
			comment = form.save()
			if request.POST.get('tweet'):
				tokens = auth.tokens
				
				Twitter(
					auth = OAuth(
						tokens['oauth_token'],
						tokens['oauth_token_secret'],
						settings.TWITTER_CONSUMER_KEY,
						settings.TWITTER_CONSUMER_SECRET
					)
				).statuses.update(
					status = '.@%s Here are my thoughts on one of your hacks: http://%s%s' %(
						idea.recipient.username, SITE.domain, comment.get_absolute_url()
					)
				)
			
			messages.success(request,u'Thanks for your comment.')
			
			return HttpResponseRedirect(
				idea.get_absolute_url()
			)
	else:
		form = None
		
	return TemplateResponse(
		request,
		'inspiration/idea.html',
		{
			'idea': idea,
			'form': form,
			'own_idea': idea.sender.pk == idea.recipient.pk,
			'me': request.user.is_authenticated() and request.user.pk == idea.recipient.pk,
			'title_parts': (idea.title, user.get_full_name() or user.username)
		}
	)

@login_required
def vote(request, username, slug, value):
	user = get_object_or_404(User, username = username)
	idea = get_object_or_404(Idea,
		slug = slug,
		recipient = user
	)
	
	idea.votes.filter(voter = request.user).delete()
	idea.votes.create(
		voter = request.user,
		value = value
	)
	
	messages.success(request, 'Thanks for your vote!')
	return HttpResponseRedirect(
		reverse('ideas', args = [idea.recipient.username])
	)

@login_required
def use(request, username, slug):
	user = get_object_or_404(User, username = username)
	
	if user.pk != request.user.pk:
		raise Http404()
	
	idea = get_object_or_404(Idea,
		slug = slug,
		recipient = user
	)
	
	idea.used = True
	idea.save()
	
	messages.success(request, 'Thanks for telling us you\'ll use the idea.')
	return HttpResponseRedirect(
		idea.get_absolute_url()
	)