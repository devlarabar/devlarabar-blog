from django import forms
from blog.models import Post


class CreatePost(forms.Form):
    title = forms.CharField(
        label='Title',
        min_length=3,
        max_length=100
    )
    content = forms.CharField(
        label='Content',
    )
    tags = forms.CharField(
        label='Tags (comma-separated)',
    )

    def clean_title(self):
        title = self.cleaned_data['title']
        title_exists = Post.objects.filter(title__iexact=title)
        if title_exists.count():
            raise forms.ValidationError("Title already exists.")
        return title
