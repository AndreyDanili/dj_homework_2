from django.urls import path, include

from school.views import students_list
from website import settings

urlpatterns = [
    path('', students_list, name='students'),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),
# For django versions before 2.0:
# url(r'^__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns