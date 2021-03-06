from django import forms
from webapp.models import Review


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['text_review', 'rating']