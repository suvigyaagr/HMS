from django.conf.urls import url
from . import views

app_name = 'mainsite'

urlpatterns = [

    # /mainsite/
    url(r'^$', views.IndexView.as_view(), name='index'),

    # /mainsite/attendance/
    url(r'^attendance/$', views.AttendanceListView.as_view(), name='attendance'),

    # /mainsite/attendance/<staff_id>/
    url(r'^attendance/(?P<pk>[0-9a-f]{8}\-[0-9a-f]{4}\-4[0-9a-f]{3}\-[89ab][0-9a-f]{3}\-[0-9a-f]{12})/$', views.DetailView.as_view(), name='staff_detail'),
]
