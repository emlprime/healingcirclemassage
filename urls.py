from django.conf.urls.defaults import *
from django.contrib import admin

from healingcirclemassage.settings import MEDIA_ROOT
from healingcirclemassage.static.models import Service, Faq, Testimonial, Event, NewsItem, HomeText, Resume, Appointment
from healingcirclemassage.static.forms import AppointmentForm


admin.autodiscover()

urlpatterns = patterns('django.views.generic.simple',
    (r'^consultation/$', 'direct_to_template', {'template': 'consultation.html'}),
    (r'^intake/$', 'direct_to_template', {'template': 'intake.html'}),
    (r'^help/$', 'direct_to_template', {'template': 'help.html'}),
    (r'^appointment/confirm/$', 'direct_to_template', {'template': 'appointment_confirmation.html'}),                       
    (r'^instructional_dvd/$', 'direct_to_template', {'template': 'instructional_dvd.html'}),                       
)

urlpatterns += patterns('healingcirclemassage.static.views',
    (r'^$', 'hometext'),
    (r'^resume/$', 'resume'),
    (r'^appointments/$', 'appointment'),
    (r'^appointment/create/$', 'appointment'),
    (r'^news/$', 'news_items'),
    (r'^writings/$', 'writings'),
)


urlpatterns += patterns('django.views.generic.list_detail',
    (r'^services/$', 'object_list',{'queryset': Service.objects.all(), 'template_name': 'services.html'}),
    (r'^faq/$', 'object_list',{'queryset': Faq.objects.all(), 'template_name': 'faq.html'}),
    (r'^events/$', 'object_list',{'queryset': Event.objects.all(), 'template_name': 'event.html'}),
    (r'^testimonials/$', 'object_list',{'queryset': Testimonial.objects.all(), 'template_name': 'testimonials.html'}),
)

urlpatterns += patterns('',
    (r'^media/(.*)$', 'django.views.static.serve', {'document_root': MEDIA_ROOT}),
    (r'^admin/(.*)$', admin.site.root),
)
