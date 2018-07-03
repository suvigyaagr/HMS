from django.views import generic
from django.views.generic import TemplateView
from .models import Staff, AttendanceType


class IndexView(TemplateView):
    template_name = 'mainsite/index.html'

class AttendanceListView(TemplateView):
    template_name = 'mainsite/attendance.html'

    def get_context_data(self, **kwargs):
        context = super(AttendanceListView, self).get_context_data(**kwargs)
        context['all_staffs'] = Staff.objects.all()
        context['all_attendance_types'] = AttendanceType.objects.all()
        return context



    #
    # template_name = ''
    # context_object_name = 'all_staffs'
    #
    # def get_queryset(self):
    #     return Staff.objects.all()

class DetailView(generic.DetailView):
    model = Staff
    template_name = 'mainsite/staff_detail.html'