from django import forms
from .models import Post, Comment

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = [
            'title',
            'content',
            'thumbnail',
            'category',
        ]
        
class CommentForm(forms.ModelForm):
    content = forms.CharField(required=True,widget=forms.Textarea(attrs={
        'rows':4
    }))
    class Meta:
        model = Comment
        fields = ('content', )