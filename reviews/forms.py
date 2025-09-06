from django import forms
from .models import Review

class SearchForm(forms.Form):
    query = forms.CharField(max_length=200, required=False, label="Search Book")

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['rating', 'comment']
        widgets = {
            'rating': forms.NumberInput(attrs={'min': 1, 'max': 5}),
            'comment': forms.Textarea(attrs={'rows': 3}),
        }
