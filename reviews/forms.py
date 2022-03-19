from django import forms
from .models import Review


class UserReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes, remove auto-generated
        labels and set autofocus on first field
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            'name': 'Username',
            'subject': 'Title',
            'review': 'review',
            'rating': 'rating',
            'product_id': 'product_id',
            'order_number': 'order_number',

        }

        self.fields['name'].widget.attrs['autofocus'] = True
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black rounded-0'