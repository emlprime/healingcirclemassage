from django.conf.urls.defaults import *
from django.contrib import admin

from healingcirclemassage.settings import MEDIA_ROOT
from healingcirclemassage.static.models import Service, Faq, Testimonial, Event, NewsItem, HomeText, Resume, Writing, Appointment
from healingcirclemassage.static.forms import AppointmentForm


admin.autodiscover()

urlpatterns = patterns('django.views.generic.simple',
    (r'^$', 'direct_to_template', {'template': 'home.html', 'extra_context': {'home_text': HomeText.objects.latest()}}),
    (r'^resume/$', 'direct_to_template', {'template': 'resume.html', 'extra_context': {'resume': Resume.objects.latest()}}),
    (r'^consultation/$', 'direct_to_template', {'template': 'consultation.html'}),
    (r'^intake/$', 'direct_to_template', {'template': 'intake.html'}),
    (r'^help/$', 'direct_to_template', {'template': 'help.html'}),
    (r'^appointment/confirm/$', 'direct_to_template', {'template': 'appointment_confirmation.html'}),                       
)

urlpatterns += patterns('healingcirclemassage.static.views',
    (r'^appointments/$', 'appointment'),
    (r'^appointment/create/$', 'appointment'),
)


urlpatterns += patterns('django.views.generic.list_detail',
    (r'^services/$', 'object_list',{'queryset': Service.objects.all(), 'template_name': 'services.html'}),
    (r'^faq/$', 'object_list',{'queryset': Faq.objects.all(), 'template_name': 'faq.html'}),
    (r'^events/$', 'object_list',{'queryset': Event.objects.all(), 'template_name': 'event.html'}),
    (r'^testimonials/$', 'object_list',{'queryset': Testimonial.objects.all(), 'template_name': 'testimonials.html'}),
    (r'^news/$', 'object_list',{'queryset': NewsItem.objects.all(), 'template_name': 'inthenews.html'}),
    (r'^writings/$', 'object_list',{'queryset': Writing.objects.all(), 'template_name': 'writing.html'}),
)

urlpatterns += patterns('',
    (r'^media/(.*)$', 'django.views.static.serve', {'document_root': MEDIA_ROOT}),
    (r'^admin/(.*)$', admin.site.root),
)
