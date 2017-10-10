from django.conf.urls import url

from .views import HomePageView, ProjectMainView

app_name = 'sturdy'
urlpatterns = [
    url(r'^$', HomePageView.as_view(), name='home'),
    url(r'^project/(?P<project_id>[0-9]+)$', ProjectMainView.as_view(), name='project'),
]