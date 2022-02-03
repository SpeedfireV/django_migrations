from django import forms

from products.models import ProductType, Product


class ProductForm(forms.Form):
    color = forms.ChoiceField(label='Kolor')

    def __init__(self, *args, product, **kwargs):
        #color_choices = kwargs.pop('color_choices') # wyrzuc z kwargs color_choices
        super().__init__(*args, **kwargs)

        product_types = ProductType.objects.filter(product=product)

        colors = [(None, 'Wybierz kolor')]
        colors += [(product_type.id, product_type.color) for product_type in product_types]

        self.fields['color'].choices = colors
