from django.conf.urls import url

from .views import HomePageView, ProjectMainView, TaskDetailsView

app_name = 'sturdy'
urlpatterns = [
    url(r'^$', HomePageView.as_view(), name='home'),
    url(r'^project/(?P<project_id>[0-9]+)$', ProjectMainView.as_view(), name='project'),
    url(r'^project/(?P<project_id>[0-9]+)/task/(?P<task_id>[0-9]+)$', TaskDetailsView.as_view(), name='task_details'),
]