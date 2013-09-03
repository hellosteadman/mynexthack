from django.contrib import admin
from django.contrib.contenttypes.generic import GenericStackedInline
from mynexthack.inspiration.models import Idea
from mynexthack.comments.models import Comment

class CommentInline(GenericStackedInline):
	model = Comment
	extra = 0

class IdeaAdmin(admin.ModelAdmin):
	list_display = ('title', 'sender', 'recipient', 'sent')
	date_hierarchy = 'sent'
	list_filter = ('recipient',)
	readonly_fields = ('slug', 'sent', 'used')
	inlines = (CommentInline,)
	
	def has_add_permission(self, request):
		return False

admin.site.register(Idea, IdeaAdmin)