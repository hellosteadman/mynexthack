from django import forms
from bambu.comments.models import Comment
from bambu.comments.helpers import sanitise

class CommentForm(forms.ModelForm):
	def __init__(self, *args, **kwargs):
		super(CommentForm, self).__init__(*args, **kwargs)
		self.fields['body'].widget.attrs['placeholder'] = 'What\'s your comment?'
		self.fields['body'].widget.attrs['class'] = 'form-control'
	
	def save(self, commit = True):
		obj = super(CommentForm, self).save(commit = False)
		obj.body = sanitise(self.cleaned_data['body'], True)
		
		if commit:
			obj.save()
		
		return obj
	
	class Meta:
		model = Comment
		fields = ('body',)