from django import forms
from mynexthack.inspiration.models import Idea

class IdeaForm(forms.ModelForm):
	def __init__(self, *args, **kwargs):
		super(IdeaForm, self).__init__(*args, **kwargs)
		self.fields['title'].widget.attrs['placeholder'] = 'What\'s your idea?'
		self.fields['title'].widget.attrs['class'] = 'form-control input-large'
		self.fields['title'].widget.attrs['required'] = self.fields['title'].required and 'required' or ''
		self.fields['description'].widget.attrs['placeholder'] = 'Give us a bit more detail'
		self.fields['description'].widget.attrs['class'] = 'form-control'
	
	class Meta:
		fields = ('title', 'description')
		model = Idea