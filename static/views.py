from django.http import HttpResponseRedirect, HttpResponse
from django.core.mail import send_mail
from django.template import RequestContext
from django.shortcuts import render_to_response


from healingcirclemassage.static.models import Appointment
from healingcirclemassage.static.forms import AppointmentForm


def appointment(request):
    """ Creates an appointment object and emails to Kathy from the appointment form
    """
    template = "appointment.html"
    if request.method == 'POST':
        values = request.POST.copy()
        form = AppointmentForm(values)
        if form.is_valid():
            appointment=form.save()
            message =  "%s %s\n%s\n%s\n%s" % (appointment.first_name, appointment.last_name, appointment.phone_number, appointment.email, appointment.description)
            # try to send mail. If it fails print out an error
            try:
                send_mail('Appointment Request Submitted', message, 'appointments@healingcirclemassage.com', ['laura.m.madsen@gmail.com'], fail_silently=False)
            except:
                print "Error: could not send mail to admins"
            return HttpResponseRedirect("/appointment/confirm/")
        else:
            errors=form.errors
            assert False
    else:
        form = AppointmentForm()
    context = locals()
    return render_to_response(template, context, context_instance=RequestContext(request))

