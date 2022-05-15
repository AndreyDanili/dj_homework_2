from django.urls import path, include

from articles.views import articles_list
from website import settings

urlpatterns = [
    path('', articles_list, name='articles'),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns