import re

from django import forms

from constants import (
    EXM_EMAIL, EXM_MODEL, EXM_VERSION, MAX_LEN_EMAIL,
    MAX_LEN_MODEL, MAX_LEN_VERSION, PATTERN_CHECK,
    RobotFormMessages
)


class OrderForm(forms.Form):
    email = forms.EmailField(
        label='Ваш email',
        max_length=MAX_LEN_EMAIL,
        widget=forms.EmailInput(attrs={'placeholder': EXM_EMAIL})
    )
    model = forms.CharField(
        label='Модель робота',
        max_length=MAX_LEN_MODEL,
        widget=forms.TextInput(attrs={'placeholder': EXM_MODEL})
    )
    version = forms.CharField(
        label='Версия робота',
        max_length=MAX_LEN_VERSION,
        widget=forms.TextInput(attrs={'placeholder': EXM_VERSION})
    )

    def clean_model(self):
        model = self.cleaned_data.get('model')

        if not re.match(PATTERN_CHECK, model):
            raise forms.ValidationError(
                RobotFormMessages.ERROR_INVALID_MODEL
            )

        return model

    def clean_version(self):
        version = self.cleaned_data.get('version')

        if not re.match(PATTERN_CHECK, version):
            raise forms.ValidationError(
                RobotFormMessages.ERROR_INVALID_VERSION
            )

        return version
