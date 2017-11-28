from django import forms
from .models import Order


class OrderCreateForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['phone',
                  'city']

    def __init__(self, *args, **kwargs):
        super(OrderCreateForm, self).__init__(*args, **kwargs)
        # self.fields['first_name'].widget.attrs.update({'class': 'form-control', 'placeholder': "Имя"})
        # self.fields['last_name'].widget.attrs.update({'class': 'form-control', 'placeholder': "Фамилия"})
        # self.fields['email'].widget.attrs.update({'class': 'form-control', 'placeholder': "Email", 'type': 'email'})
        # self.fields['address'].widget.attrs.update({'class': 'form-control', 'placeholder': "Адрес"})
        self.fields['city'].widget.attrs.update({'class': 'form-control', 'placeholder': "Город"})
        self.fields['phone'].widget.attrs.update({'class': 'form-control', 'id': "phone1", 'placeholder': "Phone"})