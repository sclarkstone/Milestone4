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
            'subject': 'Title',
            'review': 'review',
            'rating': 'rating',

        }

        self.fields['subject'].widget.attrs['autofocus'] = True
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black rounded-0'