from django import forms



PRODUCT_QUANTITY_CHOICES = [(i, str(i)) for i in range(1, 100)]

class CartAddProductForm(forms.Form):

    plus = forms.BooleanField(required=False,
                                initial=False,
                              widget=forms.HiddenInput)
    quantity = forms.TypedChoiceField(
        choices=PRODUCT_QUANTITY_CHOICES,
        coerce=int,
        label=('Quantity'),
        widget= forms.NumberInput
    )

    minus = forms.BooleanField(required=False,
                                initial=False,
                               widget=forms.HiddenInput)


    update = forms.BooleanField(required=False,
                                initial=False,
                                widget=forms.HiddenInput)




