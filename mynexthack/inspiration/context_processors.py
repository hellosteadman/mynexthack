from mynexthack.inspiration.models import Idea
from django.db.models import Sum

def ideas(request):
	def get_latest_ideas():
		return Idea.objects.all()[:3]
	
	def get_popular_ideas():
		return Idea.objects.annotate(
			vote_value = Sum('votes__value')
		).order_by('vote_value')[:3]
	
	return {
		'latest_ideas': get_latest_ideas,
		'popular_ideas': get_popular_ideas
	}