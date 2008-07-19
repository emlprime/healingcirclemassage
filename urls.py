from django.conf.urls.defaults import *
from healingcirclenaturalhealth.settings import MEDIA_ROOT

urlpatterns = patterns('django.views.generic.simple',
    (r'^$', 'direct_to_template', {'template': 'home.html'}),
    (r'^services/$', 'direct_to_template', {'template': 'services.html'}),
    (r'^consultation/$', 'direct_to_template', {'template': 'consultation.html'}),
    (r'^resume/$', 'direct_to_template', {'template': 'resume.html'}),
    (r'^intake/$', 'direct_to_template', {'template': 'intake.html'}),
    (r'^help/$', 'direct_to_template', {'template': 'help.html'}),
)

urlpatterns += patterns('',
    (r'^media/(.*)$', 'django.views.static.serve', {'document_root': MEDIA_ROOT}),
)
