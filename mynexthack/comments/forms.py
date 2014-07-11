from django import forms
from bambu_comments.models import Comment
from bambu_comments.helpers import sanitise

class CommentForm(forms.ModelForm):
	def __init__(self, *args, **kwargs):
		super(CommentForm, self).__init__(*args, **kwargs)
		self.fields['body'].widget.attrs['placeholder'] = 'What\'s your comment?'
		self.fields['body'].widget.attrs['class'] = 'input-block-level'

	def save(self, commit = True):
		obj = super(CommentForm, self).save(commit = False)
		obj.body = sanitise(self.cleaned_data['body'], True)

		if commit:
			obj.save()

		return obj

	class Meta:
		model = Comment
		fields = ('body',)
