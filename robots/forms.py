import re

from django import forms
from django.core.exceptions import ValidationError
from django.utils import timezone

from constants import PATTERN_CHECK, RobotFormMessages

from .models import Robot


class RobotForm(forms.ModelForm):
    class Meta:
        model = Robot
        fields = ['model', 'version', 'created']

    def clean_created(self):
        created = self.cleaned_data.get('created')

        if created and created > timezone.now():
            raise ValidationError(RobotFormMessages.ERROR_INVALID_DATE)

        return created

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
