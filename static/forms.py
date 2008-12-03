from django.forms.models import ModelForm
from django.forms import forms

from healingcirclemassage.static.models import Appointment

class AppointmentForm(ModelForm):
    """ Provides the appointment request form
    """

    class Meta:
        model = Appointment

    def save(self, commit=True):
        appointment = super(AppointmentForm, self).save()
        return appointment
