from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^progress/(?P<task_id>[\w-]+)/$', views.ProgressView.as_view(),
        name='progress'),
]
