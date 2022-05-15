from django.views.generic import ListView
from django.shortcuts import render

from .models import Student


def students_list(request):
    # используйте этот параметр для упорядочивания результатов
    # https://docs.djangoproject.com/en/2.2/ref/models/querysets/#django.db.models.query.QuerySet.order_by
    ordering = 'group'
    template = 'school/students_list.html'
    all_students = Student.objects.all().prefetch_related('teacher')
    order_all_student = all_students.order_by(ordering)
    context = {
        'object_list': order_all_student
    }
    return render(request, template, context)
