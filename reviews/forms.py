from django import forms
from .models import Review


class UserReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        exclude = ('user','product_id', 'order_number')
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes, remove auto-generated
        labels and set autofocus on first field
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            'subject': 'Subject/title',
            'review': 'Add your review here',
            'rating': 'Rating',

        }

        self.fields['subject'].widget.attrs['autofocus'] = True
        for field in self.fields:
            if self.fields[field].required:
                placeholder = f'{placeholders[field]} *'
            else:
                placeholder = placeholders[field]
            self.fields[field].widget.attrs['placeholder'] = placeholder
        self.fields[field].widget.attrs['class'] = 'border-black rounded-0'
        self.fields[field].label = False