from django import forms
from product.models import Product
from django.core.exceptions import ValidationError


class ReviewForms(forms.Form):
    review = forms.CharField(label="Product review")
    rate = forms.IntegerField(label="Product rate", max_value=5, min_value=1)
    product = forms.ModelChoiceField(required=False, queryset=Product.objects.all())

    def clean_review(self):
        review = self.cleaned_data.get("review")
        if not review:
            raise ValidationError("review text required")
        else:
            return review

    def clean_rate(self):
        rate = self.cleaned_data.get("rate")
        if rate < 1 or rate > 5:
            raise ValidationError("rate should be between 1 or 5")

    def clean(self):
        super().clean()
