from django import forms
from .models import Poem, ShortStory, Novel, NovelChapter

class PoemForm(forms.ModelForm):
    class Meta:
        model = Poem
        fields = ['title', 'category', 'image', 'content', 'status']


class ShortStoryForm(forms.ModelForm):
    class Meta:
        model = ShortStory
        fields = ['title', 'category', 'image', 'content', 'status']


class NovelForm(forms.ModelForm):
    class Meta:
        model = Novel
        fields = ['title', 'category', 'image', 'description', 'content', 'status']

class ChapterForm(forms.ModelForm):
    class Meta:
        model = NovelChapter
        fields = ['under', 'chapter', 'title', 'content', 'status']