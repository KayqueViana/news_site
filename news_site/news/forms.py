from django import forms

from .models import Newsletter, Comment

class NewsletterForm(forms.ModelForm):
    
    class Meta:
        model = Newsletter
        fields = ('email',)
        
class CommentForm(forms.ModelForm):
    
    class Meta:
        model = Comment
        fields = ('photo', 'name', 'surname', 'comment',)