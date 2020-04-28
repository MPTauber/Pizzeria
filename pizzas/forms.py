from django import forms

from .models import Review

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['review']
        labels = {'review': ''}
        # This makes the text area wider:
        widgets = {'review': forms.Textarea(attrs={'cols':80})}
